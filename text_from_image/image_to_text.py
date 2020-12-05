
#===================================określanie używanych modułów==============================
from urllib.parse import urlparse
from pathlib import Path
import cv2
import pytesseract
import urllib.request
import os
from os import listdir
import pdfkit
path_wkhtmltopdf = Path("H:/wkhtmltopdf/bin/wkhtmltopdf.exe")   #Wprowadzić trzeba ścieżkę do własnego
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
from os.path import isfile,join
pytesseract.pytesseract.tesseract_cmd=r'H:\\teseract\\tesseract.exe'   #Wprowadzić trzeba własną ścieżkę

#====================================określanie ścieżek w zmiennych===========================
_to_open=Path("text_from_image/links.txt")
_to_save=Path("text_from_image/images/")
_to_pdf=Path("text_from_image/pdf/")
_to_text=Path("text_from_image/txt/")
_txt_to_txt=Path("text_from_image/temp.txt")
_to_process=Path("text_from_image/To Process/")

#====================================tworzenie inkrementujacych folderow dla zdjec============
dirlist = [ item for item in os.listdir(_to_save) if os.path.isdir(os.path.join(_to_save,item))]
dirlist.append("0")
_max_dir=max(int(item) for item in dirlist)
_max_dir=int(_max_dir)+1
_num=_max_dir
os.makedirs(f'{_to_save}\{_num}',exist_ok=True)
_to_save=Path(f"text_from_image/images/{_num}/")
# ====================================znajdywanie najwyzszego pdf numera===================
#***************************************DOSTĘPNE,ALE CHWILOWO NIE UŻYWANE******************
onlyfiles = [f for f in listdir(_to_pdf) if isfile(join(_to_pdf,f))]
onlyfiles.append("0.pdf")
_max_file=max(int(item[:-4]) for item in onlyfiles)
_max_file=int(_max_file)+1
#====================================znajdywanie najwyższego pliku txt numeru=============
onlyfiles_txt = [f for f in listdir(_to_text) if isfile(join(_to_text,f))]
onlyfiles_txt.append("0.txt")
_max_file_txt=max(int(item[:-4]) for item in onlyfiles_txt)
_max_file_txt=int(_max_file_txt)+1
#====================================znajdywanie zdjęć do przetworzenia z folderu=========
to_process = [f for f in listdir(_to_process) if isfile(join(_to_process,f))]
to_process.insert(0,"*&%@#!.jpg")



#==========================================================================================
links=[]
images=[]

def _get_links():
    try: 
        f = open(_to_open)
        empty=True
        for line in f.readlines():
            empty=False
            if len(line)>3:
                link=urlparse(line)
                links.append(link.geturl())
    except FileNotFoundError: 
        print("File [links.txt] not Found")
        f = open(_to_open, "w+") 
    finally:
        if empty:
            _Clear_Session()
            print("File [links.txt] is empty")
            f.close()
            return False
        f.close()
        return True

def get_from_folder():
    if len(to_process)>1:
        for item in to_process[1:]:
            Path(f'{_to_process}\\{item}').rename(f'{_to_save}\\{item}')
            images.append(f'{_to_save}\\{item}')
    else:
        print("Folder is empty. Closing program")
        _Clear_Session()
        
def _Clear_Session():
    try:
        os.rmdir(f'{_to_save}')
        os.remove(f'{_to_text}\\{_max_file_txt}.txt')  
    except:
        pass    

def _download_image(url,fullname):
    urllib.request.urlretrieve(url,f'{_to_save}\\{fullname}\\') 

def images_from_links():
    if _get_links():
        counter=0
        print("DOWNLOADING IMAGES")
        print("==================")
        for img in links:
            fullname=str(counter)+".jpg"
            _download_image(img,fullname)
            images.append(f'{_to_save}\\{fullname}')
            print(f'Progress: {round(((counter+1)/len(links))*100,2)}%')
            counter+=1
        print("==================")


#========================Pozyskiwanie tekstu z zdjęć=========================
def _txt_from_img(img):
    with open(f'{_to_text}\\{_max_file_txt}.txt','a+',encoding="utf-8") as f:
        f.write((pytesseract.image_to_string(img,config='--psm 6')))

def get_text():
    try:
        print("PROCESSING IMAGES")
        print("==================")
        for i,img in enumerate(images):
            print(f"Progress: {round((i/len(images))*100,2)}%")
            _txt_from_img(img)
        print("==================")
    except pytesseract.pytesseract.TesseractError:
        print("Image is not in valid format") 
        _Clear_Session()

#=======================NIE UŻYWANE. POTRZEBNE LEPSZE ROZWIĄZANIE NA ZACHOWANIE FORMATOWANIA TEKSTU PRZY ROBIENIU W PDF
def txt_to_txt():
    counter=0
    f = open(f'{_to_text}\\{_max_file_txt}.txt','r',encoding="utf-8")
    txt=open(_txt_to_txt,'a+',encoding="utf-8")
    for line in f.readlines():
        for i,j in enumerate(line):
            if counter>100:
                if j==" ":
                    txt.write("<br>")
                    counter=0
            txt.write(j)            
            counter+=1               
    f.close()
    txt.close()
        
"""
txt_to_txt()
"""
        
#CHWILOWO UŻYTKOWE KOMENTY

#images_from_links()
#           /
get_from_folder()
# 
get_text()
