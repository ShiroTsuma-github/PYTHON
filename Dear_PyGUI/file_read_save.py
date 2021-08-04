from dearpygui.core import *
from dearpygui.simple import *
import re
from namedlist import namedlist
import os
folder_path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
example_path=f'{folder_path}//Dear_PyGUI//example'
print(folder_path)
class OpenFile():
    
    def __init__(self):
        self.field_shown=False
        self.file_name=''
    @property
    def file_name(self):
        return self.__file_name
    @file_name.setter
    def file_name(self,f_name):
        pattern=r'(\.txt)$'
        if re.search(pattern,f_name):
            self.__file_name=f_name
        elif f_name.lower()=='example':
            self.__file_name='example.txt'
        else:
            self.__file_name=None
    def open_file_field(self,sender,data):
        if self.field_shown==False:
            print('pressed first time')
            add_input_text('file_name_input',label=': File name')
            self.field_shown=True
        elif self.field_shown==True:
            print('Pressed second time')
            self.file_name=get_value('file_name_input')
            delete_item('file_name_input')
            self.field_shown=False
            print(self.file_name)
        self.load_content()
    def load_content(self):
        if self.file_name!=None:
            try:
                
                with open(f'{example_path}//{self.file_name}','r') as f:
                    content=f.read()
                    table=self.split_text(content,40)
                    for i,j in enumerate(table):
                        if i==0:
                            add_input_text(f'content {i}',label=content[0:j],default_value='',readonly=True,width=1,height=window_percentage(Main_window_height,100))
                            continue
                        add_input_text(f'content {i}',label=content[table[i-1]:j],default_value='',readonly=True,width=1,height=window_percentage(Main_window_height,100))
            except FileNotFoundError:
                pass
    def close_file(self,sender,data):
        print(does_item_exist('content'))
        delete_item('content')
    def split_text(self,text,chars):
        table=[]
        corrected=chars
        while True:
            if text[corrected]!=' ':
                for i in range(corrected,corrected-chars,-1):
                    if text[i]==' ':
                        break
                table.append(i)
                
            else:
                table.append(corrected)
            corrected+=chars
            if corrected>=len(text):
                return table
        
            

def window_percentage(main_window,percentage):
    return int(main_window*percentage/100)
    
Main_window_width=720
Main_window_height=480
set_main_window_size(Main_window_width,Main_window_height)
set_global_font_scale(1.25)
set_theme('Cherry')
# set_style_frame_padding(10,10)

with window('Odczytywanie zawartosci pliku',width=window_percentage(Main_window_width,50),height=window_percentage(Main_window_height,50)):
    load_file=OpenFile()
    print(get_windows())
    set_window_pos('Odczytywanie zawartosci pliku',0,0)
    add_menu_bar('navbar1')
    add_menu_item('Open',callback=load_file.open_file_field)
    add_menu_item('Close',callback=load_file.close_file)
    add_spacing(count=100)
    show_documentation()
# set_main_window_resizable(True)
# start_dearpygui()


# ('NovelSiteData',[('SiteLink',''),('fix',''),('suffix',''),('AdditionalLinks',[]),('AdditionalActionNeeded',False)])



class DearPyGUI():
    """
    Class created for convenience with easing usage.
    """
    def __init__(self,MainWindowHeight,MainWindowWidth):
        self.Main_window_width=MainWindowWidth
        self.Main_window_height=MainWindowHeight
        self.SetWindowSize()
        """FileLinkParameters store in list data about path to file with specific ID for easing use of bigger amount of files.
        """
        self.__FileLinkParameters=namedlist('FileLinkParams',[('filename'),('file_ID'),('relative_path',None),('full_path',None)])
        self.FilesUsedList=[]
    @property
    def Main_window_width(self):
        return self.__Main_window_width
    @property 
    def Main_window_height(self):
        return self.__Main_window_height
    @property
    def FilesUsedList(self):
        return self.__FilesUsedList
    @Main_window_width.setter
    def Main_window_width(self,_input):
        if str(_input).isdigit():
            if int(_input)>100 and int(_input)<1920:
                self.__Main_window_width=_input
            else:
                print('Size Error:: Could not set width. Changing to default.')
                self.__Main_window_width=960
        else:
            print('Size Error:: Could not set width. Changing to default.')
            self.__Main_window_width=960
    @Main_window_height.setter
    def Main_window_height(self,_input):
        if str(_input).isdigit():
            if int(_input)>100 and int(_input)<1080:
                self.__Main_window_height=_input
            else:
                print('Size Error:: Could not set height. Changing to default.')
                self.__Main_window_height=720
        else:
            print('Size Error:: Could not set height. Changing to default.')
            self.__Main_window_height=720
    @FilesUsedList.setter
    def FilesUsedList(self,FileToAdd,File_ID=None):
        if FileToAdd==[] and len(FileToAdd)==0:
            self.__FilesUsedList=[]
            return
        full_path_pattern=r"^([A-Za-z]:\\)(([A-Z\]a-z.!#&^@()_ 0-9\[])+\\?){0,10}([\w\s])+\.txt$"   #grupa 4 to tytul pliku
        relative_path_pattern=r'(?!^[A-Za-z]:\\)(([A-Za-z0-9!@#$%^&\-_+=,. ([\])])+\\){0,10}(([\w\s])+\.txt)$'  #grupa 3 to tytul
        """Relative path will start following from folder two levels higher, than folder the python file is launched. (.\\.\\file.py)
        """
        full_result=re.match(full_path_pattern,FileToAdd)
        relative_result=re.match(relative_path_pattern,FileToAdd)
        if full_result:
            filename=full_result.group(4)
            self.__FilesUsedList.append(self.__FileLinkParameters(filename=filename,file_ID=File_ID,full_path=full_result.group()))
        if relative_result:
            filename=relative_result.group(3)
            self.__FilesUsedList.append(self.__FileLinkParameters(filename=filename,file_ID=File_ID,relative_path=relative_result.group()))
    def SetTheme(theme):
        """Choose one of the  themes available. 
        Choose from : `"Dark", "Light", "Classic", "Dark 2", "Grey", "Dark Grey", "Cherry", "Purple", "Gold", "Red"`

        Args:
            theme (str): name of the theme.
        """
        themes=["Dark", "Light", "Classic", "Dark 2", "Grey", "Dark Grey", "Cherry", "Purple", "Gold", "Red"]
        if theme in themes:
            set_theme(theme)
        else:
            print('Type Error:: Theme not included in available themes.')
    def SetWindowSize(self,Width=0,Ratio=None):
        """Sets Size of Main Application to specified by `Main_window_width` and `Main_window_height`. 

        Args:
        
            Width (int, optional): Works in pair with `ratio`.After specyfying ratio format height will be adjusted correctly .Specified in pixels  Defaults to 0.
            
            Ratio (str, optional): Takes format of ``"int:int"``. Defaults to None.
        """
        if Ratio==None:
            set_main_window_size(self.Main_window_width,self.Main_window_height)
        else:
            pattern=r'(^\d+):(\d+$)'
            match=re.match(pattern,Ratio)
            if match:
                if Width>100 and Width<1920:
                    Size_x=int(match.group(1))
                    Size_y=int(match.group(2))
                    Size_x=Width/Size_x
                    Size_y*=Size_x
                    self.Main_window_width=int(Width)
                    self.Main_window_height=int(Size_y)
                else:
                    print('Ratio Error:: Could not properly read|set ratio.')
                    
                    
            
    def window_percentage(main_window,percentage):
        return int(main_window*percentage/100)
    def Launch(self):
        start_dearpygui()
    
dear=DearPyGUI(100000,1000000)
dear.FilesUsedList="example.txt"
dear.SetWindowSize(Ratio='1:2',Width=500)
dear.Launch()