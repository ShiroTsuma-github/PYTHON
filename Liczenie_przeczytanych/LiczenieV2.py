import re as re
from time import time
from tqdm import tqdm
from pathlib import Path
from dataclasses import dataclass
from typing import Union, Generator
import json


@dataclass
class Book:
    title: str = None
    bookType: str = None
    position: int = None
    lastChapter: Union[str, int] = None
    totalChapters: int = None
    frequency: str = ''
    status: str = ''
    notes: str = ''
    priority: int = 0

    def __repr__(self) -> str:
        return f'{self.position}. {self.title[:25]} | {self.bookType} |{self.lastChapter} | {self.totalChapters}'


class ParseListV2:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.novelList = []
        self.startTimer = time()
        self.dump = ''

    def GetType(self, bookType: int) -> str:
        """Based on bookType returns type. If bookType is not valid returns empty string.

        Args:
            bookType (int): ID of book

        Returns:
            str: Book type
        """
        if bookType == 1:
            return 'Manga'
        elif bookType == 2:
            return 'Novel'
        elif bookType == 3:
            return 'H-manhwa'
        else:
            return ''

    def GetStatus(self, status: str) -> str:
        """Based on status (symbols) returns status as text. If status is not valid returns empty string.

        Args:
            status (str): Status of book

        Returns:
            str: Book status
        """
        if status == '✓':
            return 'Completed'
        elif status == '✓?':
            return 'Unknown'
        elif status == '✓❌?':
            return 'Unsure if discontinued'
        elif status == '✓❌':
            return 'Discontinued'
        elif status == '❌❌❌':
            return 'Avoid'
        else:
            return ''

    def GetPriority(self, priority: str) -> int:
        """Based on priority (symbols) returns priority as int. If priority is not valid returns 0.

        Args:
            priority (str): Priority of book

        Returns:
            int: Book priority
        """
        ratings = \
        {
            '💯': 20,
            '🌟': 10,
            '💩': -10,
            '⭐': 10
        }
        total = 0
        for pos in priority:
            if pos in ratings:
                total += ratings[pos]
        return total

    def SmallFixes(self, book: Book) -> Book:
        """Does small fixes to book object.

        Args:
            book (Book): Book object to fix.

        Returns:
            Book: Fixed book object.
        """
        if book.totalChapters is None:
            try:
                book.totalChapters = int(book.lastChapter.strip())
            except ValueError:
                raise TypeError(f'Book {book.title} has no total chapters and last chapter is not a number')
        return book

    def ReadFileLines(self) -> 'Generator[str]':
        """Yield each line in the file given to class to save memory

        Yields:
            Generator[str]: line of text
        """
        with (open(Path(self.filepath), 'r', encoding='utf-8')) as f:
            for line in f:
                yield line

    def ParseTypeAndPosition(self, line: str) -> Union[bool, 'tuple[str, int, str]']:
        """Takes string, parses it and if not successful
        the line is `added to dump` attribute and function returns False,
        else returns tuple `str` with altered line, `int` with position and `str` with type of book.

        Args:
            line (str): Line of text to parse.

        Returns:
            Union[bool, 'tuple[str, int, str]']: `bool` if unsuccessful else line, position and type.
        """
        pattern = r'((\d+)\.?)+'
        result = re.search(pattern, line)
        if result:
            position = int(result.group(2))
            if position == 65:
                print('test')
            bookType = result.group().count('.')
            bookType = self.GetType(bookType)
            if bookType != '':
                line = line.replace(result.group(), '')
                return (line, position, bookType)
            self.dump += f'Missing type:  {line[:20]}\n'
        else:
            self.dump += line
        return False

    def ParseFrequency(self, line: str) -> Union[bool, 'tuple[str, int]']:
        """Takes string, parses it and if not successful
         function returns False (frequency is not mandatory, so it's `not added to dump`)
        else returns tuple `str` with altered line and `int` frequency

        Args:
            line (str): Line of text to parse.

        Returns:
            Union[bool, 'tuple[str, int]': `bool` if unsuccessful else line, frequency.
        """
        pattern = r'([^()]~[\d?]+)'
        result = re.search(pattern, line)
        if result:
            frequency = result.group().replace('~', '').strip()
            line = line.replace(result.group(), ' ')
            return (line, frequency)
        return False

    def ParseLastChapter(self, line: str) -> Union[bool, 'tuple[str, str]']:
        """Takes string, parses it and if not successful
        the line is added to `dump` attribute and function returns False,
        else returns tuple `str` with altered line and `str` with chapter.

        Args:
            line (str): Line of text to parse.

        Returns:
            Union[bool, 'tuple[str, str]': `bool` if unsuccessful else line, chapter.
        """
        pattern = r'([\s][\dvc]+($|[\n\s])+)|([\s]\d+\.\d+($|[\s\n])+)'
        result = re.search(pattern, line)
        if result:
            chapter = result.group().strip()
            line = line.replace(result.group(), ' ')
            return (line, chapter)
        self.dump += f'Missing Actual Chapter:  {line[:20]}\n'
        return False

    def ParseTotalChapters(self, line: str) -> Union[bool, 'tuple[str, int]']:
        """Takes string, parses it and if not successful
        function returns False (total chapters is not mandatory, so it's `not added to dump`)
        else returns tuple `str` with altered line and `int` total chapters

        Args:
            line (str): Line of text to parse.

        Returns:
            Union[bool, 'tuple[str, int]': `bool` if unsuccessful else line, total chapters.
        """
        pattern = r'([\s]\([\d\s~]+\)($|[\s\n]))'
        result = re.search(pattern, line)
        if result:
            totalChapters = int(result.group().replace('(', '').replace(')', '').strip())
            line = line.replace(result.group(), ' ')
            return (line, totalChapters)
        return False

    def ParseStatus(self, line: str) -> Union[bool, 'tuple[str, str]']:
        """Takes string, parses it and if not successful
        function returns False (status is not mandatory, so it's `not added to dump`)
        else returns tuple `str` with altered line and `str` status

        Args:
            line (str): Line of text to parse.

        Returns:
            Union[bool, 'tuple[str, str]': `bool` if unsuccessful else line, status.
        """
        pattern = r'[?❌]*✓[?❌]*'
        result = re.search(pattern, line)
        if result:
            status = result.group()
            line = line.replace(result.group(), ' ')
            status = self.GetStatus(status)
            return (line, status)
        return False

    def ParseNotes(self, line: str) -> Union[bool, 'tuple[str, str]']:
        """Takes string, parses it and if not successful
        function returns False (notes is not mandatory, so it's `not added to dump`)
        else returns tuple `str` with altered line and `str` notes

        Args:
            line (str): Line of text to parse.

        Returns:
            Union[bool, 'tuple[str, str]': `bool` if unsuccessful else line, notes.
        """
        pattern = r'\(([a-zA-Zę,śćóżźął.\s]+\d*)*\s*'
        # \(([a-zA-Zę,śćóżźął.\s]+\d*)*\s* use this in case it's laggy. possible reason is recursion
        result = re.search(pattern, line)
        if result:
            notes = result.group().replace('(', '').replace(')', '').strip()
            line = line.replace(result.group(), ' %!@#')
            pos = line.index('%!@#')
            line = line[:pos] + line[pos + 5:]
            return (line, notes)

    def ParsePriority(self, line: str) -> Union[bool, 'tuple[str, str]']:
        """Takes string, parses it and if not successful
        function returns False (priority is not mandatory, so it's `not added to dump`)
        else returns tuple `str` with altered line and `str` priority

        Args:
            line (str): Line of text to parse.

        Returns:
            Union[bool, 'tuple[str, str]': `bool` if unsuccessful else line, priority.
        """
        pattern = r'([💯🌟💩⭐]+[\s]*)+'
        result = re.search(pattern, line)
        if result:
            priority = result.group().strip()
            line = line.replace(result.group(), ' ')
            priority = self.GetPriority(priority)
            return (line, priority)
        return False

    def ParseTitle(self, line: str) -> Union[bool, 'str']:
        """Takes string, parses it and if not successful
        the line is added to `dump` attribute and function returns False,
        else returns `str` with title.

        Args:
            line (str): Line of text to parse.

        Returns:
            Union[bool, str': `bool` if unsuccessful else title.
        """
        if line == '':
            self.dump += 'Somehow title is empty\n'
            return False
        title = line.strip()
        return title

    def ParseLine(self, line):
        book = Book()
        if line == '\n':
            return
        line = line.replace('\n', '')

        TypePosition = self.ParseTypeAndPosition(line)
        if not TypePosition:
            return
        line, book.position, book.bookType = TypePosition

        Frequency = self.ParseFrequency(line)
        if Frequency:
            line, book.frequency = Frequency

        LastChapter = self.ParseLastChapter(line)
        if not LastChapter:
            return
        line, book.lastChapter = LastChapter

        TotalChapters = self.ParseTotalChapters(line)
        if TotalChapters:
            line, book.totalChapters = TotalChapters

        Status = self.ParseStatus(line)
        if Status:
            line, book.status = Status

        Notes = self.ParseNotes(line)
        if Notes:
            line, book.notes = Notes

        Priority = self.ParsePriority(line)
        if Priority:
            line, book.priority = Priority

        ParseTitle = self.ParseTitle(line)
        if not ParseTitle:
            return
        book.title = ParseTitle
        book = self.SmallFixes(book)
        self.novelList.append(book)

    # sum of all chapters of each bookType
    def GetTotalChapters(self):
        totalManga = 0
        totalNovel = 0
        totalHmanhwa = 0
        for book in self.novelList:
            if book.bookType == 'Manga':
                totalManga += book.totalChapters
            elif book.bookType == 'Novel':
                totalNovel += book.totalChapters
            elif book.bookType == 'H-manhwa':
                totalHmanhwa += book.totalChapters
        return (totalManga, totalNovel, totalHmanhwa)

    def TimeSpentReading(self, Novel_time=10, Manga_time=5, Hmanga_time=10):
        manga, novel, hmanga = self.GetTotalChapters()
        counter = manga + novel + hmanga
        print(f'Total amount: [ {counter} ] ')
        print(f'With result of:   Manga/Webtoon/Manhwa : [{manga}]    Novel : [{novel}]   Manga^^ : [{hmanga}]')
        print(f'Amounting to:                            {round((manga/counter)*100,2)}%             {round((novel/counter)*100,2)}%             {round((hmanga/counter)*100,2)}%            \n\n')
        manga_t = manga * Manga_time
        novel_t = novel * Novel_time
        hmanga_t = hmanga * Hmanga_time
        total_t = manga_t + hmanga_t + novel_t
        print(F'Total time taken:                         {round((total_t)/1440,2)} D')
        print(f'Time taken in minutes:                    {manga*Manga_time} Min      {novel*Novel_time} Min      {hmanga*Hmanga_time} Min')
        print(f'Time taken in hours:                      {round((manga*Manga_time)/60,2)} H      {round((novel*Novel_time)/60,2)} H       {round((hmanga*Hmanga_time)/60,2)} H')
        print(f'Time taken in days:                       {round((manga*Manga_time)/1440,2)} D        {round((novel*Novel_time)/1440,2)} D        {round((hmanga*Hmanga_time)/1440,2)} D')
        print('\n')
        print(f'Amounting to:    :                        {round((manga_t/total_t)*100,3)} %       {round((novel_t/total_t)*100,3)} %        {round((hmanga_t/total_t)*100,3)} %')

    def ShowDump(self):
        print(60 * '=')
        print(self.dump)
        print(60 * '=')

    def SaveDump(self):
        with (open(Path('Liczenie_przeczytanych/dump.txt'), 'w+', encoding='utf-8')) as f:
            f.write(self.dump)

    # save classes from self.novelList to json
    def SaveToJson(self):
        with (open(Path('Liczenie_przeczytanych/lista.json'), 'w+', encoding='utf-8')) as f:
            json.dump([ob.__dict__ for ob in self.novelList], f, ensure_ascii=False)

    # read classes from json to self.novelList
    def ReadFromJson(self):
        with (open(Path('Liczenie_przeczytanych/lista.json'), 'r', encoding='utf-8')) as f:
            self.novelList = [Book(**ob) for ob in json.load(f)]

    def TimeElapsed(self):
        print('Time elapsed: {0:.2f} seconds'.format(time() - self.startTimer))
        return time() - self.startTimer

    # print all classes from self.novelList
    def PrintAll(self):
        for book in self.novelList:
            print(book)

    def ParseFile(self):
        for line in tqdm(self.ReadFileLines()):
            self.ParseLine(line)
        self.TimeElapsed()
        print(self.dump)

    # print all classes from self.novelList alpanumericly
    def PrintAllAlpha(self):
        for book in sorted(self.novelList, key=lambda x: x.title):
            print(f'[{book.position}.] : {book.bookType} : {book.title} : {book.totalChapters}\n{book.notes}')

    def PrintAllAlphaByType(self):
        for book in sorted(self.novelList, key=lambda x: x.bookType):
            print(f'[{book.position}.] {book.bookType} : {book.title}: {book.totalChapters}')

    def PrintAllAlphaByStatus(self):
        for book in sorted(self.novelList, key=lambda x: x.status):
            if book.status == '':
                continue
            print(f'[{book.position}.] {book.title}: {book.status}\n>>Total Chapters: {book.totalChapters}')

    def PrintAllAlphaByPriority(self):
        for book in sorted(self.novelList, key=lambda x: x.priority):
            if book.priority == 0:
                continue
            print(f'[{book.position}.] {book.title}: {book.priority}\n>>Total Chapters: {book.totalChapters}')

    def PrintAllAlphaByPosition(self):
        for book in sorted(self.novelList, key=lambda x: x.position):
            print(f'[{book.position}.] {book.bookType} : {book.title}: {book.priority}')

    def PrintAllAlphaByLastChapter(self):
        for book in sorted(self.novelList, key=lambda x: x.lastChapter):
            print(f'[{book.position}.] {book.title}: {book.priority}\n>>Last Chapter: {book.lastChapter}')

    def PrintAllAlphaByTotalChapters(self):
        for book in reversed(sorted(self.novelList, key=lambda x: x.totalChapters)):
            print(f'[{book.position}.] {book.title}: {book.priority}\n>>Total Chapters: {book.totalChapters}')

    def PrintAllAlphaByNotes(self):
        for book in sorted(self.novelList, key=lambda x: x.notes):
            if book.notes != '':
                print(f'{book.title}:\n>>Notes: {book.notes}\n')

if __name__ == '__main__':
    a = ParseListV2('Liczenie_przeczytanych/lista.txt')
    # a.ParseFile()
    # a.SaveToJson()
    a.ReadFromJson()
    # a.PrintAllAlphaByType()
    a.TimeSpentReading()