from colorama import init,deinit,reinit
from colored import fg,bg,attr
import threading
import time
import sys
import os
#========================================text color config=====================================
def color(color,text):
    get_color={
    'error':'#FF0000',
    'success':'#00FF00',
    'process':'#FFFF00',
    'info':'#0000FF',
    }
    reset=attr('reset')
    return (fg(get_color[color])+text+reset)
#===========================================input config=======================================
hand_input=False
amount_of_files=2
#=============================================tablice==========================================
sciezki_plikow=[]
nazwy_plikow=[]
ilosc_linijek=[]
formated_sciezki_plikow=[]
formated_nazwy_plikow=[]
#=======================================file config==========================================
ten_folder = os.path.dirname(os.path.abspath(__file__))

for i in range(0,amount_of_files):  
    if hand_input:
        file_input=str(input(color('info',"Podaj nazwę pliku wraz z formatem (np. plik.txt ): ")))
    else:
        file_input=f'lorem{i}.txt'
        print(color('info',f'Wprowadzanie ręczne wyłączone. Wybieranie domyślnego zdefiniowanego pliku {i+1}: ')+file_input)
    sciezki_plikow.append(os.path.join(ten_folder, file_input))
    nazwy_plikow.append(file_input)
        

#=========================================functions==============================================

def count_lines(plik,i):
    #LICZENIE LINIJEK UŻYTECZNE,JEŻELI PLANUJE NA KILKA THREADOW,ZEBY PODZIELIC KAZDEJ FRAGMENT PLIKU
    try:
        plik=open(plik,'r')
        print(color('process',f':::Liczenie linijek pliku {nazwy_plikow[i]}...'))
        num_lines = sum(1 for line in plik)
        plik_jest=True
    except:
        plik_jest=False
        print(color('error',f"Program nie może znaleźć pliku {nazwy_plikow[i]}! Upewnij się,czy podałeś poprawną nazwę pliku i czy znajduje się w folderze z programem."))
    finally:
        if plik_jest:
            plik.close()
            #print(color_success+f'Ilość linijek w pliku to {num_lines}'+reset)
            ilosc_linijek.append(num_lines)
            return num_lines
        print (color('error',"Brak pliku do odczytu. Przerywanie programu."))
        sys.exit()

def format_to_compare():
    for i in range(0,amount_of_files):
        plik=sciezki_plikow[i]
        if count_lines(plik,i)>1: 
            try:
                formated=f'formated_{nazwy_plikow[i]}'
                formated_nazwy_plikow.append(formated)
                print(color('process',f":::Formatowanie pliku {nazwy_plikow[i]}..."))
                write_file=open(f'{ten_folder}\{formated}','w')
                formated_sciezki_plikow.append(os.path.join(ten_folder,formated))
                for line in open(sciezki_plikow[i],'r').readlines():
                    write_file.write(line.replace("\n", ""))
                    #write_file.write((line.replace(" ", "")))
            except FileNotFoundError:
                print(color('error',"Wystąpił błąd podczas próby formatowania tekstu."))
            finally:
                write_file.close()
        else:
            return (color('error',"Podany plik jest pusty: ")+nazwy_plikow[i])
        
def compare_sentence(formated_file):
    pass
    
format_to_compare()
compare_sentence("a")
#count_lines(my_file)
