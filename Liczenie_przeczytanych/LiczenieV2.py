import re as re
from time import time
from tqdm import tqdm
from pathlib import Path
from dataclasses import dataclass
from typing import Union, Generator


@dataclass
class Book:
    title: str = None
    bookType: str = None
    position: int = None
    lastChapter: Union[str, int] = None
    totalChapters: int = None
    frequency: str = None
    status: str = None
    notes: str = None
    priority: int = None

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
            return 'manga'
        elif bookType == 2:
            return 'novel'
        elif bookType == 3:
            return 'H-manhwa'
        else:
            return ''

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
            bookType = result.group().count('.')
            bookType = self.GetType(bookType)
            if bookType != '':
                line = line.replace(result.group(), '')
                return (line, position, bookType)
            self.dump += f'Missing type:  {line[:20]}\n'
        else:
            self.dump += line
        return False

    def ParseTitle(self, line: str) -> Union[bool, 'tuple[str, str]']:
        """Takes string, parses it and if not successful
        the line is added to `dump` attribute and function returns False,
        else returns tuple `str` with altered line and `str` with title.

        Args:
            line (str): Line of text to parse.

        Returns:
            Union[bool, 'tuple[str, str]': `bool` if unsuccessful else line, title.
        """

        if line:
            return (line, line)
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

        ParseTitle = self.ParseTitle(line)
        if not ParseTitle:
            return

    def SaveDump(self):
        with(open(Path('Liczenie_przeczytanych/dump.txt'), 'w+', encoding='utf-8')) as f:
            f.write(self.dump)

    def TimeElapsed(self):
        print('Time elapsed: {0:.2f} seconds'.format(time() - self.startTimer))
        return time() - self.startTimer

    def ParseFile(self):
        for line in tqdm(self.ReadFileLines()):
            self.ParseLine(line)
        self.TimeElapsed()
        print(self.dump)


if __name__ == '__main__':
    a = ParseListV2('Liczenie_przeczytanych\lista.txt')
    a.ParseFile()