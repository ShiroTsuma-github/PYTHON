# SITE REQUESTING
import urllib3
import certifi
#SITE SCANNING AND SCRAPPING
from bs4 import BeautifulSoup
#SYSTEM CONTROL
from time import sleep


class SearchInternet():
    def __init__(self,title,_type='',options=''):
        self.title=title
        self.__query=f'{self.title}'.replace(' ','-').lower()
    def GiveXResults(self):  
        http = urllib3.PoolManager()    
        prefix='https://wuxiaworld.online/'
        title = self.__query
        url=prefix+title
# https://wuxiaworld.online/the-empresss-gigolo
        user_agent='Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'
        headers={'User-Agent':user_agent}
        resp = http.request('GET', url,headers=headers)
        print('')
        if resp.status==200:
            print('')
            soup=BeautifulSoup(resp.data.decode('utf-8'),'html.parser')
            # print(soup.prettify())
            for i in (list(soup.children)):
                print(i)
                print(100*'=')
                sleep(1)
            
            # print(resp.data.decode('utf-8'))
        else:
            raise ValueError(f'URLLIB3 VALUE: [ {resp.status} ]')
        
if __name__ == "__main__":
    a=SearchInternet(title='The empresss gigolo')
    a.GiveXResults()
