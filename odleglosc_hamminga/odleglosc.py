from colorama import init,deinit,reinit
from colored import fg,bg,attr
import threading
import time
import os
#========================================text color config=====================================
reset=attr('reset')
color_error=fg('#FF0000')
color_success=fg('#00FF00')
color_info=fg('#0000FF')
#=======================================input file config=======================================
hand_input=False
amount_of_files=1
for i in range(0,amount_of_files):  
    if hand_input:
        file_input=str(input(color_info+"Podaj nazwę pliku wraz z formatem (np. plik.txt ): "+ reset))
    else:
        file_input="lorem.txt"
        print(color_info+f'Wprowadzanie ręczne wyłączone. Wybieranie domyślnego zdefiniowanego pliku: {file_input}' +reset)
        
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, file_input)
#========================================functions config========================================

def count_lines(plik):
    try:
        plik=open(plik,'r')
        num_lines = sum(1 for line in plik)
        plik_jest=True
    except:
        plik_jest=False
        print(color_error+"Program nie może znaleźć pliku! Upewnij się,czy podałeś poprawną nazwę pliku i czy znajduje się w odpowiednim folderze.")
    finally:
        if plik_jest:
            plik.close()
            print(color_success+f'Ilość linijek w pliku to {num_lines}'+reset)
            return num_lines
        print ("Brak pliku do odczytu. Przerywanie programu."+reset)

def format_to_compare(plik):
    if count_lines(plik)>1: 
        try:
            formated=f'formated_{file_input}'
            write_file=open(f'{THIS_FOLDER}\{formated}','w')
            for line in open(my_file,'r').readlines():
                if line == '\n':
                    pass
                else:
                    write_file.write()
                    #write_file.write((line.replace(" ", "")))
        except FileNotFoundError:
            print(color_error+"Wystąpił błąd podczas próby formatowania tekstu."+reset)
        finally:
            write_file.close()
    else:
        pass
format_to_compare(my_file)
#count_lines(my_file)
