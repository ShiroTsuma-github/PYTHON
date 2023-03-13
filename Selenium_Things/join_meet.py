import os, sys
import re
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from MyModules.SitesData import SitesInformation as SI
from datetime import datetime
from time import sleep
"""
Zaprzestane ze względu na problemy google z obsługiwaniem logowania automatycznie na konto


"""


class Meet(SI):
    def __init__(self,headless=True,BrowserType='Firefox'):
        super().__init__(headless=headless,BrowserType=BrowserType)
        self.__lessons={}
        self.__load_links()
        self.__hours={}
        self.__load_hours()
        
    def __load_links(self):
        title_pattern=r'\w+:'
        with(open('H:\\Dokumenty\\GitHub\\PYTHON\\Selenium_Things\\files\\Meet_link_list.txt','r')) as f:
            for line in f.readlines():
                result=re.search(title_pattern,line)
                if result:
                    self.__lessons[result.group()[:-1]]=line.replace(result.group(),'').strip()

        
    def __load_hours(self):
        key_pattern=r'\d+:($|\s)+'
        subject_hour_pattern=r'(\w+):(\s?\d+$)'
        with(open('H:\\Dokumenty\\GitHub\\PYTHON\\Selenium_Things\\files\\hours.txt','r')) as f:
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
        self.AddChromeOption('--disable-web-security')
        self.AddChromeOption('--allow-running-insecure-content')
        self.browser=''
        print('Odpalone')
        self.browser.get('https:www.saucedemo.com')
        sleep(100)
        # username=self.browser.find_element_by_id('identifierId')
        # username.click()
        # username.send_keys('spam.shiro@gmail.com')

        # next=self.browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button/div[2]')
        # next.click()
        # sleep(2)
        # password=self.browser.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        # password.click()
        # password.send_keys('enter_your_password_here')
        # next=self.browser.find_element_by_xpath('//*[@id="passwordNext"]/div/button/div[2]')
        # next.click()
        # sleep(15)
        # sleep(100)
        # pass


    
        
a=Meet(headless=False,BrowserType='Chrome')
a.Start(datetime.now().weekday(),datetime.now().hour)
# # automatedshirotsuma@gmail.com
# Automated