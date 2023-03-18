import re as re
from time import time
from namedlist import namedlist
# from search_google import SearchInternet
from Check_Novel import NovelUpdatesInformation
from progressbar import progressbar
from os import path

folder_path=path.dirname(__file__)
folder=path.relpath(folder_path)


class ParseNovel():

    def __init__(self,filepath=None):
        """Initializes with filepath. In case of lack of filepath it does nothing. Couldn't bother at the moment to fix it.

        TODO:

                -Change filepath enforcing and maybe think about allowing to read from text input
                -Write function that allows to save the output in parsed format, and write parser for second format.
            

        Args:
            filepath (Path, optional): Format is as follows: `folder\\\\file.format`. Defaults to None.
        """
        self.__file=filepath
        self.__content=self.__LoadList()
        self.__NovelData=namedlist('value',[('title','None'), ('last_chapter',0), ('total_chapters',0), ('frequency','?'), ('status',''),('notes',''),('priority','')],default=None)
        self.__NovelList={}
        self.__start_time=time()
        self.__dump=''
        self.__get_id()
        self.__get_element()
        print(f'Initializing took: -----------{round(time()-self.__start_time,4)} seconds --------------')

    def __LoadList(self):
        """Reads from file and saves positions to table.

        Returns:
        
            list: list with practically lines from file.
        """
        with(open(self.__file,'r',encoding='utf-8')) as f:
            self.__content=f.read().split('\n')
        return self.__content
            
    def __get_id(self):
        """Reads header number `0` || `0.0` ||`0.0.0` depending on type of data that it reads. Then creates dictionary position with it as key and writes rest as value.
        
        Note:
        
            In case of line without it, line is saved to dump and can be invoked by using `instance.PrintDump()`
        """
        pattern=r'\d+[\d.]+'
        for item in self.__content:
            d=re.match(pattern,item)
            if d:
                d_prefix=d.group()
                
                if item=='' or item ==' ':
                    pass
                else:
                    val=self.__NovelData(title=item.lstrip(d_prefix))
                    self.__NovelList[d_prefix.strip('.')]=val
            else:
                self.__dump+=str(item)+'\n'   
        self.__content=None  
        
    def __get_element(self):
        """Using regexp and couple of predefined patterns searches title for needed data and then saves it to variable (`everything is stored in namedlist`) after which it removes that part from title.
        """
        try:
            pattern_last_chap=r'([ ]\d+($|[\n ])+)|([ ]\d+[.]\d+($|[ \n])+)'
            pattern_total_chap=r'([ ][(][\d ~]+[)]($|[ \n]))'
            pattern_freq=r'([^()]~[\d?x]+)'
            pattern_fin=r'[?❌]*✓[?❌]*'
            pattern_notes=r'[(]([\d\s]*([a-zA-Z,.\s?!]+[\d\s]*)+)[)]' #[(][\s]*[\d\s]?[\w\s]+[\d\s]*[\s]*[)]
            pattern_prio=r'([💯🌟💩]+[\s]*)+'
            pos=1
            for item in self.__NovelList:
                pos+=1
                self.__NovelList[item].title= self.__NovelList[item].title.replace('�', '')
                title= self.__NovelList[item].title
                last_chap=re.search(pattern_last_chap,title)
                total_chap=re.search(pattern_total_chap,title)
                freq_chap=re.search(pattern_freq,title)
                status_=re.search(pattern_fin,title)
                notes=re.search(pattern_notes,title)
                priorit=re.search(pattern_prio,title)
                print(f"Parsing {pos}")
                if last_chap:
                    self.__NovelList[item].last_chapter=last_chap.group().strip()
                    self.__NovelList[item].title= self.__NovelList[item].title.replace(last_chap.group(), ' ')
                if total_chap:
                    self.__NovelList[item].total_chapters=total_chap.group().strip().replace('(', '').replace(')', '')
                    self.__NovelList[item].title= self.__NovelList[item].title.replace(total_chap.group(), ' ')
                else:
                    self.__NovelList[item].total_chapters= self.__NovelList[item].last_chapter
                if freq_chap:
                    self.__NovelList[item].frequency=freq_chap.group().strip().replace('~', '')
                    self.__NovelList[item].title= self.__NovelList[item].title.replace(freq_chap.group(), ' ')
                if status_:
                    self.__NovelList[item].status=status_.group().strip()
                    self.__NovelList[item].title= self.__NovelList[item].title.replace(status_.group(), ' ')
                if notes:
                    self.__NovelList[item].notes=notes.group().replace('(', '').replace(')', '')
                    self.__NovelList[item].title= self.__NovelList[item].title.replace(notes.group(), ' ')
                if priorit:
                    self.__NovelList[item].priority=priorit.group().strip().replace('�', '')
                    self.__NovelList[item].title= self.__NovelList[item].title.replace(priorit.group(), ' ')
                self.__NovelList[item].title= self.__NovelList[item].title.strip()
        except:
            raise "There was error"
    
    def __CheckType(self,data):
        """just counts number of dots from key and because of it returns amount (done pretty stupidly)

        Args:
        
            data (str): just key name

        Returns:
        
            int: number of dots
        """
        dot_count=0
        dot_count=data.count('.')
        return dot_count
        
    def AmountOfNovels(self):
        """Prints total amount of each type and percentage it takes.
        """
        counter=0
        manga=0
        novel=0
        hmanga=0
        dot_count=0
        for item in self.__NovelList:
            counter+=1
            dot_count=item.count('.')
            if dot_count==0:
                manga+=1
            elif dot_count==1:
                novel+=1
            else:
                hmanga+=1
        print(f'Total amount: [{counter}]')
        print(f'With result of:   Manga/Webtoon/Manhwa : [{manga}]    Novel : [{novel}]   Manga^^ : [{hmanga}]')
        print(f'Amounting to:                            {round((manga/counter)*100,2)}%           {round((novel/counter)*100,2)}%            {round((hmanga/counter)*100,2)}%            \n\n')
    
    def PrintList(self,mode='minimal',sort='default',filter_mode='default'):
        """Prints list based on type of positions that user wants. Depending on mode it shows different amount of data for position. It has couple methods of sorting.

        Args:
        
            mode (str, optional): Decides how much information is shown for position. Defaults to 'minimal'. Other options are: 'half','full'
            sort (str, optional): Chooses on which criteria positions are shown. Defaults to 'default'. Other options are: 'inc_\chapter','dec_chapter','inc_priority','dec_priority'
            filter_mode (str, optional): [description]. Defaults to 'default'.

        Returns:
            [type]: [description]
        """
        start_time=time()
        
        # def check_type(data):
        #     dot_count=0
        #     dot_count=data.count('.')
        #     return dot_count
        
        def minimal(data,padd_size=100):
            padding=len(self.__NovelList[item].title)
            print(f'Name: [ {self.__NovelList[item].title} ]',end='')
            if padding>padd_size:
                print('     ↓')
                print((padd_size+10)*'→',end='')
            else:
                print((padd_size-padding)*' ',end='')
            print(f' Total Chapters: [ {self.__NovelList[item].total_chapters} ]   ',end='')
            padd2=len(self.__NovelList[item].status)
            print(f' Status: [ {self.__NovelList[item].status} ]    ',end='')
            
        def half(data,padd_size=0):
            print(f'   Last Chapter Mark: [ {self.__NovelList[item].last_chapter} ]')
            
        def full(data,padd_size=0):
            print(f'Note added: {self.__NovelList[item].notes}',end='')
            print((padd_size-len(self.__NovelList[item].notes))*' ',end='')
            print(f'Rating: {self.__NovelList[item].priority}            Frequency: [ {self.__NovelList[item].frequency} ]')
            
        def SortMechanism(array):
            less = []
            equal = []
            greater = []
            if len(array) > 1:
                pivot = array[0][0]
                for x in array:
                    if x[0] < pivot:
                        less.append(x)
                    elif x[0] == pivot:
                        equal.append(x)
                    elif x[0] > pivot:
                        greater.append(x)
                return SortMechanism(less)+equal+SortMechanism(greater)
            else:
                return array
            
        def SortByChapters(data):
            array=[]
            for item in data:
                try:
                    if (self.__NovelList[item].total_chapters).isdigit():
                        array.append([int(self.__NovelList[item].total_chapters),item])
                except:
                    print('THERE OCCURED AN ERROR WITH DATA')
                    print(self.__NovelList[item].total_chapters)
                    array.append([0,item])
            sorted_list=SortMechanism(array)
            array=[]
            for i in sorted_list:
                array.append(i[1])
            return array
                
        def SortByPriority(data):
            array=[]
            ratings={'💯':20,
                     '🌟':10,
                     '💩':-10,
                     }
            for item in data:
                rate=0
                for char in self.__NovelList[item].priority:
                    rate+=ratings.get(char,0)
                array.append([rate,item])
            sorted_list=SortMechanism(array)
            array=[]
            for i in sorted_list:
                array.append(i[1])
            return array
            
        cont=True
            
        if filter_mode=='default':
            _type=-1
        elif filter_mode.lower()=='manga':
            _type=0
        elif filter_mode.lower()=='novel':
            _type=1
        elif filter_mode.lower()=='hmanga':
            _type=2
        else:
            _type=-2
            print('Invalid mode. Choose from one of the following : [default]/[manga]/[novel]/[hmanga]')
            cont=False
        if _type>-1:
            data=list(filter(lambda item : self.__CheckType(item)==_type,self.__NovelList))
        elif _type==-1:
            data=self.__NovelList.keys()
        if cont:
            if sort.lower()=='inc_chapter':
                data=SortByChapters(data)
            elif sort.lower()=='default':
                pass
            elif sort.lower()=='dec_chapter':
                data=SortByChapters(data)
                data=reversed(data)
            elif sort.lower()=='inc_priority':
                data=SortByPriority(data)
            elif sort.lower()=='dec_priority':
                data=SortByPriority(data)
                data=reversed(data)
            else:
                print('Invalid mode. Choose from one of the following : [default]/[inc_chapter]/[dec_chapter]/[inc_priority]/[dec_priority]')
                cont=False
            if mode.lower()=='minimal' and cont==True:
                for item in data:
                    minimal(item)
                    print('')
            elif mode.lower()=='half' and cont==True:
                for item in data:
                    minimal(item,padd_size=60)
                    half(item)
            elif mode.lower()=='waves' and cont==True:
                for item in data:
                    minimal(item,padd_size=100)
            elif mode.lower()=='full' and cont==True:
                for item in data:
                    minimal(item,padd_size=60)
                    half(item)
                    full(item,padd_size=60)
            else:
                if cont==False:
                    pass
                else:
                    print('Invalid mode. Choose from one of the following : [minimal]/[half]/[full]')
        print(f'Sorting and printing took: -----------{round(time()-start_time,4)} seconds --------------')
    
    def PrintDump(self):
        print(60*'=')
        print(self.__dump)
        print(60*'=')
    
    def AmountOfChapters(self,Novel_time=10,Manga_time=5,Hmanga_time=10):
        manga=0
        novel=0
        hmanga=0
        dot_count=0
        for item in self.__NovelList:
            dot_count=item.count('.')
            if dot_count==0:
                manga+=int(self.__NovelList[item].total_chapters)
            elif dot_count==1:
                novel+=int(self.__NovelList[item].total_chapters)
            else:
                hmanga+=int(self.__NovelList[item].total_chapters)
        counter=manga+novel+hmanga
        print(f'Total amount: [ {counter} ] ')
        print(f'With result of:   Manga/Webtoon/Manhwa : [{manga}]    Novel : [{novel}]   Manga^^ : [{hmanga}]')
        print(f'Amounting to:                            {round((manga/counter)*100,2)}%             {round((novel/counter)*100,2)}%             {round((hmanga/counter)*100,2)}%            \n\n')
        manga_t=manga*Manga_time
        novel_t=novel*Novel_time
        hmanga_t=hmanga*Hmanga_time
        total_t=manga_t+hmanga_t+novel_t
        print(F'Total time taken:                         {round((total_t)/1440,2)} D')
        print(f'Time taken in minutes:                    {manga*Manga_time} Min      {novel*Novel_time} Min      {hmanga*Hmanga_time} Min')
        print(f'Time taken in hours:                      {round((manga*Manga_time)/60,2)} H      {round((novel*Novel_time)/60,2)} H       {round((hmanga*Hmanga_time)/60,2)} H')
        print(f'Time taken in days:                       {round((manga*Manga_time)/1440,2)} D        {round((novel*Novel_time)/1440,2)} D        {round((hmanga*Hmanga_time)/1440,2)} D')
        print('\n')
        print(f'Amounting to:    :                        {round((manga_t/total_t)*100,3)} %       {round((novel_t/total_t)*100,3)} %        {round((hmanga_t/total_t)*100,3)} %')

    def SearchForTitles(self,filter_mode='default'):
        Manga_Excluded=['']
        if filter_mode=='manga':
            _type=0
        elif filter_mode=='novel':
            _type=1
        elif filter_mode=='hmnaga':
            _type=2
        elif filter_mode=='default':
            pass
        else:
            print('Invalid mode. Choose from one of the following : [manga]/[novel]/[hmanga]/[default]')
        data=list(filter(lambda item : self.__CheckType(item)==_type,self.__NovelList))
        a=NovelUpdatesInformation()
        for i in progressbar(range(len(data)), redirect_stdout=True):
            f=open(f'{folder}\\wyniki.txt','a')
            f.write(f'\n[ {self.__NovelList[data[i]].title} ] :\n')
            a.title=self.__NovelList[data[i]].title
            a.FindCurrentChapterCount()
            f.write(f'{a.results}\n')
            a.results=[]
            f.close()
    def CompareFallback(self):
        pass
                
        
a=ParseNovel('Liczenie_przeczytanych\\lista.txt')
a.PrintList(mode='HALF',sort='inc_chapter')
a.PrintDump()
a.AmountOfNovels()


a.AmountOfChapters()
# a.SearchForTitles(filter_mode='novel')

# with ProgressBar(max_value=len(data)) as bar:
#     for item in data:
#         bar.update(iter_counter)
#         print(f'\n[ {self.__NovelList[item].title} ] :')
#         a.title=self.__NovelList[item].title
#         a.FindCurrentChapterCount()
#         print(a.results)
#         iter_counter+=1
