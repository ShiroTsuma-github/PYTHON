from typing import Union
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome,Firefox,Edge
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from msedge.selenium_tools import EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import re
from os.path import abspath
import sys
from time import sleep
from progressbar import progressbar


class DriverFolderNotFound(Exception):
    """Raised when can't find DRIVERS folder (probably beacuse you renamed `\\WEB\\` or `\\WEB\\DRIVERS\\`)"""
    pass
class DriverMissing(Exception):
    """Raised when can't find specific driver or `browser_type` doesn't match"""
    pass
class IncorrectOption(Exception):
    """Raised when option passed is incorrect. Make sure you are using option that works with browser that you use"""
    
    
    
class EasySelenium():
    class __EasyBrowser():
        def __init__(self,driver_path,options,browser_type):
            self.path=driver_path
            self.browser_type=browser_type
            self.options=options
            self.__initial_options=options
            self.instance=self.InitializeSession()
            
        def InitializeSession(self):
            try:
                if self.browser_type.upper()=='CHROME':
                    return Chrome(self.path,options=self.options)
                elif self.browser_type.upper()=='FIREFOX':
                    return Firefox(self.path,options=self.options)
                elif self.browser_type.upper()=='EDGE':
                    return Edge(self.path,options=self.options)
            except:
                sys.exit('Could not find driver for what you specified or there occurred unidentified error.')
        
        def ResetSession(self):
            try:
                self.instance.quit()
                self.options=self.__initial_options
            except:
                raise
            finally:
                self.instance=self.InitializeSession()
                
        def ReloadSession(self):
            try:
                self.instance.quit()
            except:
                raise 
            finally:
                self.instance=self.InitializeSession()
                
        def TerminateSession(self):
            self.instance.quit()
            
        def AddOption(self,option):
            self.options.add_argument(option)
            
        def OpenSite(self,link):
            try:
                self.instance.get(link)
                # print(f'opening site. current handle: {self.instance.current_window_handle}')
            except:
                sys.exit('There was problem with link.')
            
        def SiteAddress(self)->str:
            return self.instance.current_url
        
        def SiteTitle(self)->str:
            return self.instance.title
        
        def FindElement(self,element:str,parameter:str):
            try:
                if parameter.upper()=='XPATH':
                    return self.instance.find_element_by_xpath(element)
                elif parameter.upper()=='CLASS_NAME':
                    return self.instance.find_element_by_class_name(element)
                elif parameter.upper()=='ID':
                    return self.instance.find_element_by_id(element)
                elif parameter.upper()=='CSS_SELECTOR':
                    return self.instance.find_element_by_css_selector(element)
                elif parameter.upper()=='NAME':
                    return self.instance.find_element_by_name(element)
                elif parameter.upper()=='LINK-CONTENT':
                    return self.instance.find_element_by_link_text(element)
                elif parameter.upper()=='LINK-PARTIAL CONTENT':
                    return self.instance.find_element_by_partial_link_text(element)
            except NoSuchElementException:
                if parameter.upper()=='XPATH':
                    print('The XPATH didn\'t work. Maybe try giving full XPATH. And make sure you want XPATH to correct object')
                sys.exit('Could not find element you are looking for. Did you give correct parameter?')
        
        def AddInstance(self):
            self.instance.execute_script('window.open()')
        def CloseInstance(self):
            self.instance.close()
        def ChangeInstance(self,position):
            self.instance.switch_to.window(self.instance.window_handles[position])
            # print(self.instance.current_window_handle)
        def ListInstances(self):
            print(self.instance.window_handles)
            
   
                
    def __init__(self,browser_type:str):
        """Initialization of class with browser_type

        Args:
            browser_type (str): type of browser to initialize
        """
        self.browser_type=browser_type
        self.browser=self.__LoadDrivers()
        self.objects=[]
        self.tabs=[]
        self.current_tab=0
        self.total_tabs=1
        self.tabs.append(self.CurrentURLTitle())
    def __LoadDrivers(self):
        """Hidden method that checks for `WEB` folder in current path and from that goes to `DRIVERS` and tries to open specified driver

        Raises:
            DriverFolderNotFound: If there is no `WEB` folder in current file path.
            DriverMissing: There is no driver found with specified name

        Returns:
            __EasyBrowser instance: Returns object address to __EasyBrowser initialized
        """
        pattern=r'(.*\\WEB\\)(.*)'
        folder_path=re.search(pattern,abspath(__file__))
        try:
            if folder_path:
                folder_path=str(folder_path.group(1))+'DRIVERS\\'
            else:
                raise DriverFolderNotFound
            if self.browser_type.upper()=='CHROME':
                return self.__EasyBrowser(f'{folder_path}chromedriver.exe',ChromeOptions(),self.browser_type)
            elif self.browser_type.upper()=='FIREFOX':
                return self.__EasyBrowser(folder_path,FirefoxOptions(),self.browser_type)
            elif self.browser_type.upper()=='EDGE':
                return self.__EasyBrowser(f'{folder_path}msedgedriver.exe',EdgeOptions(),self.browser_type)
            else:
                raise DriverMissing
        except (DriverFolderNotFound,DriverMissing) as error:
            sys.exit(error.__doc__)
            
    def AddBrowserOption(self,option:str)->None:
        """Adds setting like language,size,mode,etc.

        ``Important``:
            Make sure option you add is correct for `browser_type` you choose.
        
        Note:
            Still requires to `ReloadBrowser`. 
        
        Args:
            option (str): option to add.
        """
        self.browser.AddOption(option)
        
    def ChangeVisibility(self)->None:
        """Changes browser visibility through `headless`.
        """
        self.browser.options.headless=not self.browser.options.headless
        self.ReloadBrowser()
        
    def ResetBrowser(self)->None:
        """Reloads Browser with cleared setttings.
        """
        self.browser.ResetSession()
        
    def ReloadBrowser(self)->None:
        """Reloads browser without clearing settings.
        """
        self.browser.ReloadSession()
        
    def CloseBrowser(self)->None:
        """Closes Browser.
        """
        self.browser.TerminateSession()
    
    def BrowserWait(self,seconds:int)->None:
        """Makes browser wait for `seconds`. 

        Args:
            seconds (int): time to wait for.
        """
        for i in progressbar(range(seconds),redirect_stdout=True):
            sleep(1)
    
    def CreateTroubleshootWindow(self,seconds:int)->None:
        """Opens Browser window for specified amount of `seconds` to allow for doing actions etc.

        Note:
        
            It resets browser options before that.
            
        Args:
            seconds (int): amount of seconds to wait for.
        """
        self.ResetBrowser()
        for i in progressbar(range(int(seconds/(seconds/10))),redirect_stdout=True):
            sleep(int(seconds/10))
        self.CloseBrowser()
        
    def CurrentURLAddress(self)->str:    
        """Returns Current URL.

        Returns:
            str: address of site.
        """
        return self.browser.SiteAddress()
    
    def CurrentURLTitle(self)->str:
        """Returns URL title.


        Returns:
            str: text inside <title> of site.
        """
        return self.browser.SiteTitle()
    
    def OpenURL(self,link:str)->None:
        """Opens link provided in browser window. If link lacks http | https it adds http://

        Args:
            link (str): link to site
        """
        temp=link
        pattern=r'((http|https):[/]{2})'
        if re.match(pattern,temp):
            self.browser.OpenSite(str(temp))
        else:
            self.browser.OpenSite(f'http://{temp}')
        self.tabs[self.current_tab]=self.CurrentURLTitle()
            
    def ObjectContent(self,element:str,parameter:str)->str:
        """Returns content of object provided.

        Args:
            
                element (str): path | name | selector or anything specified in `FindElement` method that specifies what to look for.
            
                parameter (str): specifies what `element` represents.

        Returns:
            str: Text that is inside our object.
        """
        obj=self.browser.FindElement(element,parameter)
        return obj.get_attribute('innerHTML')
    
    def SaveObjectInList(self,element:str,parameter:str)->int:
        """Saves object into `self.objects`. You can access it later using `index` of list. 

        Args:
        
                element: (str): path | name | selector or anything specified in `FindElement` method that specifies what to look for.
                
                
                parameter (str): 

        Returns:
            int: position in self.objects that object is in.
        """
        obj=self.browser.FindElement(element,parameter)
        self.objects.append(obj)
        return len(self.objects)-1
    
    def RemoveObject(self,_id:int):
        """Removes object from `self.objects`.

        Args:
            _id (int): id of object to remove
        """
        self.objects.pop(_id)
    
    def URLContent(self)->str:
        """Returns whole content of address.

        Returns:
            str: Content of site.
        """
        obj=self.browser.FindElement('/html','XPATH')
        return obj.get_attribute('innerHTML')
    
    def InputIntoField(self,text:str,element:Union[int,str],parameter:str=None,end:bool=False)->None:
        """Inputs text into specified text field.

        Args:
            text (str): Text to input into field
            element (Union[int,str]): if `parameter` is empty expects int corresponding to id inside self.objects else expects path | name | selector.
            parameter (str, optional): specifies what `element` represents. Defaults to None. If None then `element` is expected to be int.
            end (bool, optional): if set to true sends input. Defaults to False.
        """
        if parameter:
            obj=self.browser.FindElement(element,parameter)
        else:
            try:
                obj=self.objects[element]
            except:
                sys.exit('parameter is empty and element is not int or does not exist under specified element(id)')
        obj.clear()
        obj.send_keys(text)
        if end:
            obj.send_keys(Keys.RETURN)
    
    def AddTab(self):
        self.browser.AddInstance()
        self.tabs.append('')
        self.total_tabs+=1
        sleep(1)
        
    def CloseCurrentTab(self):
        self.tabs.pop(self.current_tab)
        self.total_tabs-=1
        self.browser.CloseInstance()
        if self.current_tab==self.total_tabs:
            self.current_tab-=1
        if self.current_tab<0:
            sys.exit('All tabs closed. Closing program')
        self.browser.ChangeInstance(self.current_tab)
    def CloseTitleTab(self,name):
        for pos in range(0,len(self.tabs)):
            if self.tabs[pos].upper()==str(name).upper():
                break
        self.tabs.pop(pos)
        self.total_tabs-=1
        self.browser.ChangeInstance(pos)
        self.current_tab=pos
        self.browser.CloseInstance()
        if self.current_tab==self.total_tabs:
            self.current_tab-=1
        if self.current_tab<0:
            sys.exit('All tabs closed. Closing program')
            
        
    def ListTabs(self):
        self.browser.ListInstances() 
        print(self.tabs)
        
    def GoToNextTab(self):
        if self.current_tab<self.total_tabs-1:
            self.browser.ChangeInstance(self.current_tab+1)
            self.current_tab+=1
        else:
            print('There is no next tab.')
    
    def GoToPreviousTab(self):
        if self.current_tab-1>=0:
            self.browser.ChangeInstance(self.current_tab-1)
            self.current_tab-=1
        else:
            print('There is no previous tab.')
        
        
    
    
            
        
if __name__ == '__main__': 
    a=EasySelenium('chrome')
    # a.CreateTroubleshootWindow(60)
    # a.OpenURL('https://www.python.org')
    # print(a.CurrentURLAddress())
    # print(a.CurrentURLTitle())
    # print(a.ObjectContent('q','name'))
    # a.InputIntoField('Testujemy','q','name')
    # poz=a.SaveObjectInList('q','name')
    # a.InputIntoField('Testujemy2',poz)
    a.OpenURL('www.python.org')
    a.BrowserWait(1)
    a.AddTab()
    a.GoToNextTab()
    a.CloseCurrentTab()
    a.AddTab()
    a.AddTab()
    # a.GoToNextTab()
    a.OpenURL('www.google.com')
    a.GoToNextTab()
    a.OpenURL('www.minecraft.com')
    a.GoToNextTab()
    # a.OpenURL('www.amazon.com')
    a.ListTabs()
    a.CloseTitleTab('google')
    a.BrowserWait(30)
