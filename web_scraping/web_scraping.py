#-------------------------------------moduly-------------------------
from lxml import *
import os
import requests
from bs4 import BeautifulSoup
#-----------------------------------zmienne--------------------------
wszystkie_linki=[]

#-------------------Sciezka i otworzenie pliku------------------------
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'linki.txt')
linki=open(my_file,"r")


#-----------------Otworzenie zawartosci,poprawienie i wpisanie---------
for line in linki:
    wszystkie_linki.append(line.replace("\n", ""))

for line in wszystkie_linki:
    page=requests.get(line)
    content=page.text
    soup= BeautifulSoup(content,'html.parser')
    print(soup.find(class_="fm-notification-body"))








"""
page = requests.get('link')
tree = html.fromstring(page.content)
testowe_wyniki=tree.xpath('//p[@class=code]/code()')
print(testowe_wyniki)

#//tbody//tr//td/text()
"""