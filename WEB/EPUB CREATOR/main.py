from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions

import re
from os.path import abspath
class DriverFolderNotFound(Exception):
    """Raised when can't find DRIVERS folder (probably beacuse you renamed `\\WEB\\` or `\\WEB\\DRIVERS\\`)"""
    pass
class DriverMissing(Exception):
    """Raised when can't find specific driver"""
    pass
class EasySelenium():
    
    def __init__(self,BrowserType:str,headless:bool=True):
        self.browser=self.__LoadDrivers(BrowserType)
        
    def __LoadDrivers(self,BrowserType:str):
        pattern=r'(.*\\WEB\\)(.*)'
        folder_path=re.search(pattern,abspath(__file__))
        try:
            if folder_path:
                folder_path=str(folder_path.group(1))+'DRIVERS\\'
            else:
                raise DriverFolderNotFound
            
        
        except (DriverFolderNotFound,DriverMissing) as error:
            print(error.__doc__)
    def AddBrowserOption(self,option:str):
        pass
        
    def CurrentURL(self)->str:    
        return self.browser.current_url
    
a=EasySelenium('CHROME')
