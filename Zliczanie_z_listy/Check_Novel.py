# IMPORTING SELENIUM COMPONENTS
from SitesData import SitesInformation
# IMPORTING SYSTEM CONTROL
from os import system,name,path
from time import sleep
# THIRD PARTY MODULES
from progressbar import ProgressBar,Bar
from namedlist import namedlist

# FILE AND SITE LINKS
folder_path=path.dirname(__file__)
folder=path.relpath(folder_path)




class NovelUpdatesInformation(SitesInformation):
    def __init__(self,title='DummyTitle',headless=True):
        super().__init__(headless=headless)
        self.__Novel_Site_Data=namedlist('NovelSiteData',[('SiteLink',''),('fix',''),('suffix',''),('AdditionalLinks',[]),('AdditionalActionNeeded',False)])
        self.__Domains_to_search={
            'Novel Updates':self.__Novel_Site_Data(SiteLink='https://www.novelupdates.com/series/',fix='-'), #nie jest na czasie z duza iloscia novelek
            'Webnovel':self.__Novel_Site_Data(SiteLink='https://www.webnovel.com',AdditionalActionNeeded=True),  #trzeba wyszukiwac w search-bar tytul,wybierac pozycje i dopiero sprawdzac
            'ReadLightNovel':self.__Novel_Site_Data(SiteLink='https://www.readlightnovel.org/',fix='-'),
            'NovelFull':self.__Novel_Site_Data(SiteLink='https://novelfull.com/',fix='-',suffix='.html'), #koncowka z .html chyba trzeba przeklikac na ostatnia strone,zeby znalezc numery tytulu
            'ReadNovelFull':self.__Novel_Site_Data(SiteLink='https://readnovelfull.com/',fix='-',suffix='.html#tab-chapters-title'), # '#tab-chapters-title' trzeba dodac do konca nazwy .html                     
                                  }
        self.__Formated_domain_titles={}
        self.title=title
        self.results=[]
    
    @property
    def results(self):
        return self.__results
    @results.setter
    def results(self,results):
        if results==[]:
            self.__results=[] 
        else:
            self.__results.append(results)
    @property
    def title(self):
        return (self.__title)
    @title.setter
    def title(self,title):
        try:
            if len(title)<=1 or title.isdigit()==True:
                raise TypeError
            else:
                self.__title=title
                self.__GenerateDomainTitles()
        except TypeError:
            self.__title=''
            print('There occurred an error with title.')
    def __GenerateDomainTitles(self):
        def __GetTitle(item):
            self.browser=''
            self.browser.get(self.__Domains_to_search[item].SiteLink)
            find_button=self.browser.find_element_by_xpath('/html/body/header/div/div/a[1]')
            find_button.click()
            input_field=self.browser.find_element_by_id('seachModalInput')
            input_field.send_keys(self.title)
            input_field.submit()
            self.WaitForElement('/html/body/div[1]/div[2]/div[2]/div[1]/div/ul/li[1]/h3/a','XPATH','','')
            title_nr1=self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div/ul/li[1]/h3/a')
            title_nr1.click()
            wyn=self.browser.current_url
            self.browser.close()
            return (wyn)
        
        if self.title=='DummyTitle':
            return {}
        Progress_counter=0
        with ProgressBar(max_value=len(self.__Domains_to_search)) as bar:
            print(40*'=','Generating possible links for known sites',40*'=')
            for item in self.__Domains_to_search:
                bar.update(Progress_counter)
                if self.__Domains_to_search[item].AdditionalActionNeeded==False and self.__Domains_to_search[item].AdditionalLinks==[]:
                    self.__Formated_domain_titles[item]=f'{self.__Domains_to_search[item].SiteLink}{self.title}{self.__Domains_to_search[item].suffix}'.replace("'",'').replace("!",'').replace(' ',self.__Domains_to_search[item].fix).lower().replace(',',self.__Domains_to_search[item].fix)
                elif self.__Domains_to_search[item].AdditionalActionNeeded==True:
                    self.__Formated_domain_titles[item]=__GetTitle(item)
                elif self.__Domains_to_search[item].AdditionalLinks!=[]:
                    link_list=[]
                    for addition in self.__Domains_to_search[item].AdditionalLinks:
                        link_list.append(f'{self.__Domains_to_search[item].SiteLink}{self.title} {addition}'.replace("'",'').replace("!",'').replace(' ',self.__Domains_to_search[item].fix).replace(',',self.__Domains_to_search[item].fix).lower())
                    self.__Formated_domain_titles[item]=link_list
                    del addition
                # print(f'\n{self.__Formated_domain_titles[item]}')
                Progress_counter+=1
                sleep(1)
        print('') 
    def FindCurrentChapterCount(self):
        def Generate_for_title(item):
            if item=='Novel Updates':
                    temp=self.WaitForElement('seriestitlenu','CLASS_NAME','page-404','CLASS_NAME')
                    if temp=='E200':
                        novel_updates_status=self.browser.find_element_by_id('editstatus')
                        self.results=[item,novel_updates_status.text]
                    elif temp=='Error':
                        print('There occurred an error with the link/novel name')
            elif item=='Webnovel':
                temp=self.WaitForElement('/html/body/div[1]/div[2]/div/div/div[2]/p[1]/strong[1]/span','XPATH','err-con','CLASS_NAME')
                if temp=='E200':
                    novel_updates_status=self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/p[1]/strong[1]/span').text
                    novel_updates_status+=' '+self.browser.find_element_by_xpath('/html/body/div[1]/div[2]/div/div/div[2]/p[1]/strong[2]/span').text
                    self.results=[item,novel_updates_status]
                elif temp=='Error':
                    print('There occurred an error with the link/novel name')
            elif item=='NovelOnlineFull':
                temp=self.WaitForElement('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[1]/a','XPATH','other_news_wrap','CLASS_NAME')
                if temp=='E200':
                    novel_updates_status=self.browser.find_element_by_xpath('/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/span[1]/a')
                    self.results=[item,novel_updates_status.text]
                elif temp=='Error':
                    print('There occurred an error with the link/novel name')
            elif item=='ReadLightNovel':
                temp=self.WaitForElement('/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div[7]/div[2]','XPATH','error-code','CLASS_NAME')
                if temp=='E200':
                    novel_updates_status=self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[2]/div/div[2]/div/div[7]/div[2]')
                    self.results=[item,novel_updates_status.text]
                elif temp=='Error':
                    print('There occurred an error with the link/novel name')
            elif item=='NovelFull':
                temp=self.WaitForElement('/html/body/div/main/div[2]/div[1]/div/div[1]/div[3]/div[5]/ul/li[1]/a/span','XPATH','alert alert-danger','CLASS_NAME')
                if temp=='E200':
                    novel_updates_status=self.browser.find_element_by_xpath('/html/body/div/main/div[2]/div[1]/div/div[1]/div[3]/div[5]/ul/li[1]/a/span')
                    self.results=[item,novel_updates_status.text]
                elif temp=='Error':
                    print('There occurred an error with the link/novel name')
            elif item=='ReadNovelFull':
                temp=self.WaitForElement('item-value','CLASS_NAME','site-error','CLASS_NAME')
                if temp=='E200':
                    novel_updates_status=self.browser.find_element_by_class_name('item-value')
                    self.results=[item,novel_updates_status.text]
                elif temp=='Error':
                    print('There occurred an error with the link/novel name')
        self.browser=''
        Progress_counter=0
        print(40*'=','Checking Sites for Chapter Count',40*'=')
        with ProgressBar(max_value=len(self.__Formated_domain_titles)) as bar:
            for item in self.__Formated_domain_titles:
                bar.update(Progress_counter)
                if type(self.__Formated_domain_titles[item])==list:
                    for pos in self.__Formated_domain_titles[item]:
                        self.browser.get(pos)
                        Generate_for_title(item)
                else:
                    self.browser.get(self.__Formated_domain_titles[item])
                    Generate_for_title(item)
                Progress_counter+=1
        print('')
        self.browser.close()
        
            
            
            
            
# try:
#     browser.get(site)
#     WebDriverWait(browser,delay).until(EC.presence_of_element_located((By.CLASS_NAME,'seriestitlenu')))
#     novel_updates_status=browser.find_element_by_id('editstatus')
#     print(novel_updates_status.text)
# #CLOSING SESSION
# except KeyboardInterrupt:
#     Destroy()
# except NoSuchElementException:
#     print('Could not find such element')
# except TimeoutException:
#     if browser.find_element_by_class_name('page-404'):
#         print(f'There occurred an error with title of page: [ {site} ]')
#     else:
#         print('Loading took too long')
# finally:
#     Destroy()
#     pass
if __name__ == '__main__':
    a=NovelUpdatesInformation(headless=False)
    a.title="I'm the Evil Lord of an Intergalactic Empire!"
    a.FindCurrentChapterCount()
    print(a.results)
# a.DebugBrowser()
    

"""
NOTATKI:


WEBNOVEL.COM Z TEGO CO WIDZE DLA WSZYSTKIEGO ZWRACA WYNIK,NIE WAZNE CZY MAJA CZY NIE,BO PATRZA CZY PODOBNE COS,
WIEC TRZEBA SPRAWDZAC CZY TYTUL NA KTORYM JESTESMY ZGADZA SIE LUB JEST PODOBNY DO TYTULU NOVELKI


"""