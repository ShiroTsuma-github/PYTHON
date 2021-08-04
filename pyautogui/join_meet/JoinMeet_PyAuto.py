import pyautogui
from time import sleep
import re
from datetime import datetime

"""
Po dolaczeniu na meet odcisza,puszcza audio wczesniej nagrane zarywajace,po czym po 1 min wysyla w chacie wiadomosc,ze zarywa,wiec 
nie bede dzis zbyt gadal

--Problem: jak aplikacja otworzy na fullscreen na 2 monitorze to traktuje jakby otworzyła dobrze na 1.
fix chyba:jezeli znajdzie,ze fullscreen,to sprawdzic  czy jest to widoczne w obszarze  1 ekranu
"""
    
class PyAutoGui_Meet:
    def __init__(self):
        self.__lessons={}
        self.__load_links()
        self.__hours={}
        self.__load_hours()
        
    def __load_links(self):
        title_pattern=r'\w+:'
        with(open('H:\\Dokumenty\\GitHub\\PYTHON\\pyautogui\\files\\Meet_link_list.txt','r')) as f:
            for line in f.readlines():
                result=re.search(title_pattern,line)
                if result:
                    self.__lessons[result.group()[:-1]]=line.replace(result.group(),'').strip()

        
    def __load_hours(self):
        key_pattern=r'\d+:($|\s)+'
        subject_hour_pattern=r'(\w+):((\s*)\d+$)'
        with(open('H:\\Dokumenty\\GitHub\\PYTHON\\pyautogui\\files\\hours.txt','r')) as f:
            table={}
            day=-1
            for line in f.readlines():
                result=re.search(key_pattern,line)
                if result:
                    if day==-1:
                        pass
                    else:
                        self.__hours[day]=table
                        table={}
                    day=result.group().strip()[:-1]
                    self.__hours[day]=''
                else:
                    subject=re.search(subject_hour_pattern,line)
                    if subject:
                        # self.__hours[day]={subject.group(1):subject.group(2).strip()}
                        table[subject.group(2).strip()]=subject.group(1).strip()
            else:
                self.__hours[day]=table
    def Start(self,day,hour):
        table=self.__hours[str(day)]
        if str(hour) in table.keys():
            self.Launch(table[str(hour)])
        else:
            print('Nie ta godzina')
            
    def Launch(self,subject):
        pyautogui.FAILSAFE=False
        pyautogui.moveTo(0, 1080,duration=2)
        sleep(0.2)
        pyautogui.click()
        pyautogui.moveTo(145,1016)
        pyautogui.click()
        pyautogui.write('Edge')
        sleep(0.5)  
        pyautogui.moveTo(113,491)
        sleep(0.2)
        pyautogui.click()
        sleep(1)
        cont=False
        button_location=pyautogui.locateOnScreen('H:\Dokumenty\GitHub\PYTHON\pyautogui\images\locate.png',confidence=0.7)
        if button_location:
            pyautogui.moveTo(button_location.left+300,button_location.top+20)
            sleep(0.2)
            pyautogui.dragTo(500, 0,duration=2,button='left')
            cont=True
        else:
            button_whole_screen=pyautogui.locateOnScreen('H:\Dokumenty\GitHub\PYTHON\pyautogui\images\locate_full.png',confidence=0.8)
            if button_whole_screen:
                cont=True
        if cont:
            pyautogui.moveTo(200,50,duration=1)
            sleep(0.2)
            pyautogui.click()
            pyautogui.write(self.__lessons[subject])
            pyautogui.click()
            pyautogui.press('enter')
            sleep(1)
            pyautogui.moveTo(600,750,duration=1)
            pyautogui.click()
            pyautogui.moveTo(1300,600)
            sleep(1)
            pyautogui.click()
        else:
            print('Couldn\'t open Window. Sorry')
            
    
print(datetime.now().weekday(),datetime.now().hour)      
a=PyAutoGui_Meet()
a.Start(datetime.now().weekday(),datetime.now().hour)