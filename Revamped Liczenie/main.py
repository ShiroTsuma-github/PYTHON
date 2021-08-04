#   IMPORTY
import re
from namedlist import namedlist         #PRZETRZYMUJE DANE DLA POZYCJI, BO SZYBSZE NIZ KLASA PRZY TYM JAK ROBILEM
from progressbar import progressbar     #DLA ESTETYKI
import os                               #DO POZYCJI AKTUALNEJ


#   PRZETWARZANIE POZYCJI
with open(example_file,'r',encoding='utf-8') as file:
    for line in file.readlines():
        print(line)
        
class ParseList():
    def __init__(self):
        self.root_folder=os.path.dirname(os.path.realpath(__file__))
        self.file_name='example list.txt'    
        self.full_file_path=f'{self.root_folder}\example\\{self.file_name}'
    @property   
    def file_name(self):
        return self.__file_name
    @file_name.setter
    def file_name(self,f_name):
        pattern=r'(\.txt)$'
        if re.search(pattern,f_name):
            self.__file_name=f_name
        else:
            self.__file_name='example list.txt'