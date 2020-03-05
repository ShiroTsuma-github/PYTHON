#-------------------------------------moduly-------------------------
from lxml import *
import os
import requests
from bs4 import BeautifulSoup
#-----------------------------------zmienne--------------------------
rar_zip_etc=[]
Videos=[]
Photos=[]
Executables=[]
Audio=[]
Text=[]
PDFs=[]
Torrents=[]
Other=[]
wszystkie_linki=[]

#-------------------Sciezka i otworzenie pliku------------------------
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'linki.txt')
linki=open(my_file,"r")


#-----------------Otworzenie zawartosci,poprawienie i wpisanie---------
for line in linki:
    '''
    if line=="rar, zip, etc:\n":
        w_co_wysylac=rar_zip_etc
    elif line=="VIdeos:\n":
        w_co_wysylac=Videos
    elif line=="Photos:\n":
        w_co_wysylac=Photos
    elif line=="Executables:\n":
        w_co_wysylac=Executables
    elif line=="Audio:\n":
        w_co_wysylac=Audio
    elif line=="PDFs:\n":
        w_co_wysylac=PDFs
    elif line=="Torrents:\n":
        w_co_wysylac=Torrents
    elif line=="Other:\n":
        w_co_wysylac=Other
    else:
        if len(line)>3:
    '''
    wszystkie_linki.append(line.replace("\n", ""))












"""
page = requests.get('link')
tree = html.fromstring(page.content)
testowe_wyniki=tree.xpath('//p[@class=code]/code()')
print(testowe_wyniki)

#//tbody//tr//td/text()
"""