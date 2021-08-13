from typing import Union
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome,Firefox,Edge
from selenium.webdriver import ChromeOptions
from selenium.webdriver import FirefoxOptions
from msedge.selenium_tools import EdgeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from glob import glob
import re
from os.path import abspath,isdir
from os import mkdir,listdir
from shutil import rmtree
import os
import sys
from time import sleep
from progressbar import progressbar


class DriverFolderNotFound(Exception):
    """Raised when can't find DRIVERS folder (probably beacuse you renamed `\\MySelenium\\` or `\\MySelenium\\DRIVERS\\`)"""
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
                if self.browser_type=='CHROME':
                    return Chrome(self.path,options=self.options)
                elif self.browser_type=='FIREFOX':
                    return Firefox(self.path,options=self.options)
                elif self.browser_type=='EDGE':
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
        def AddExpOption(self,option):
            self.options.add_experimental_option('prefs',option)
        def AddAddon(self,addon):
            self.options.add_extension(addon)
            
        def Maximize(self):
            self.instance.maximize_window()
            
        def FixSiteAddress(self,link):
            temp=link
            pattern=r'((http|https):[/]{2})'
            if re.match(pattern,temp):
                pass
            else:
                temp=f'http://{temp}'
            return temp
        
        def OpenSite(self,link):
            try:
                self.instance.get(link)
            except:
                sys.exit('There was problem with link.')
            
        def SiteAddress(self)->str:
            return self.instance.current_url
        
        def SiteTitle(self)->str:
            return self.instance.title
        
        def FindElement(self,element:str,parameter:str):
            parameter=parameter.upper()
            try:
                if parameter=='XPATH':
                    return self.instance.find_element_by_xpath(element)
                elif parameter=='CLASS_NAME':
                    return self.instance.find_element_by_class_name(element)
                elif parameter=='ID':
                    return self.instance.find_element_by_id(element)
                elif parameter=='CSS_SELECTOR':
                    return self.instance.find_element_by_css_selector(element)
                elif parameter=='NAME':
                    return self.instance.find_element_by_name(element)
                elif parameter=='LINK-CONTENT':
                    return self.instance.find_element_by_link_text(element)
                elif parameter=='LINK-PARTIAL CONTENT':
                    return self.instance.find_element_by_partial_link_text(element)
            except NoSuchElementException:
                if parameter=='XPATH':
                    print('The XPATH didn\'t work. Maybe try giving full XPATH. And make sure you want XPATH to correct object')
                sys.exit('Could not find element you are looking for. Did you give correct parameter?')
        
        def AddInstance(self,site,current_handle=None):
            self.instance.execute_script(f'window.open("{site}")')
            
        def CloseInstance(self):
            self.instance.close()
            
        def ChangeInstance(self,position):
            self.instance.switch_to.window(self.instance.window_handles[position])
            
        def ListInstances(self):
            print(self.instance.window_handles)
            
   
                
    def __init__(self,browser_type:str):
        """Initialization of class with browser_type

        Args:
            browser_type (str): type of browser to initialize
        """
        self.browser_type=browser_type.upper()
        self.browser=self.__LoadDrivers()
        self.objects=[]
        self.tabs=[]
        self.links=[]
        self.current_tab=0
        self.total_tabs=1
        self.tabs.append('')
        self.links.append('')
        self.PendingDownloads=[]
        self.FinishedDownloads=[]
        self.Downloads_path=''
    def __LoadDrivers(self):
        """Hidden method that checks for `MySelenium` folder in current path and from that goes to `DRIVERS` and tries to open specified driver

        Raises:
            DriverFolderNotFound: If there is no `MySelenium` folder in current file path.
            DriverMissing: There is no driver found with specified name

        Returns:
            __EasyBrowser instance: Returns object address to __EasyBrowser initialized
        """
        pattern=r'(.*\\MySelenium\\)(.*)'
        folder_path=re.search(pattern,abspath(__file__))
        try:
            if folder_path:
                folder_path=str(folder_path.group(1))+'DRIVERS\\'
            else:
                raise DriverFolderNotFound
            if self.browser_type=='CHROME':
                return self.__EasyBrowser(f'{folder_path}chromedriver.exe',ChromeOptions(),self.browser_type)
            elif self.browser_type=='FIREFOX':
                return self.__EasyBrowser(folder_path,FirefoxOptions(),self.browser_type)
            elif self.browser_type=='EDGE':
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
    def AddBrowserAddon(self,addon:str)->None:
        """Given path to `.crx` file will load it to browser.

        Args:
            addon (str): [description]
        """
        self.browser.AddAddon(addon)
        self.ReloadBrowser()
    
    def PrepareDownloads(self,path:str)->None:
        if self.browser_type!='CHROME':
            print('Sorry. That browser wasn\'t implemented yet.')
            return
        if not isdir(path):
            pattern=r'(.*)\\(.*\..*)$'
            folder_path=re.search(pattern,path)
            if folder_path:
                path=folder_path.group(1)
        path=f'{path}\\SessionDownloads'
        opt={'download.default_directory':f'{path}\\CACHE'}
        try:
            mkdir(path)
        except FileExistsError:
            pass
        path+='\\CACHE'
        try:
            mkdir(path)
        except FileExistsError:
            pass
                
        self.browser.AddExpOption(opt)
        self.Downloads_path=path
        self.ReloadBrowser()
        
        
    def ChangeVisibility(self)->None:
        """Changes browser visibility through `headless`.
        """
        self.browser.options.headless=not self.browser.options.headless
        self.ReloadBrowser()
    
    def MaximizeWindow(self)->None:
        self.browser.Maximize()
        
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
        self.CheckDownloads()
        if len(self.Downloads_path)>1:
            rmtree(f'{self.Downloads_path}',ignore_errors=True)
            
            
    
    def BrowserWait(self,seconds:int)->None:
        """Makes browser wait for `seconds`. 

        Args:
            seconds (int): time to wait for.
        """
        for i in progressbar(range(seconds),redirect_stdout=True):
            sleep(1)
    
    def CreateTroubleshootWindow(self,seconds:int,new:bool=True)->None:
        """Opens Browser window for specified amount of `seconds` to allow for doing actions etc.

        Note:
        
            It resets browser options before that.
            
        Args:
            seconds (int): amount of seconds to wait for.
            new (boolean): Specifies if open clear session ( `True` ) or with setting already set (`False`).Defaults to True.
        """
        if new:
            self.ResetBrowser()
        else:
            self.ReloadBrowser()
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

        self.browser.OpenSite(self.browser.FixSiteAddress(link))
        self.tabs[self.current_tab]=self.CurrentURLTitle()
        self.links[self.current_tab]=self.CurrentURLAddress()
            
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
        
    def CheckDownloads(self):
        """[summary]

        Returns:
            [type]: [description]
        """
        if len(self.Downloads_path)<1:
            return
        self.PendingDownloads=glob(f'{self.Downloads_path}\\*.crdownload')
        self.FinishedDownloads+=[f'{self.Downloads_path}\\{f}' for f in listdir(self.Downloads_path) if f'{self.Downloads_path}\\{f}' not in self.PendingDownloads]
        for _file in self.FinishedDownloads:
            os.replace(_file,_file.replace('CACHE\\',''))
        if len(glob(f'{self.Downloads_path}\\*.crdownload'))<1:
            return True
        
        return False
            
    
    
    
    def AddTab(self,URL:str)->None:
        """Adds new Tab to rightmost of another tabs. Adds it's title and URL into `self.links` and `self.tabs`

        Args:
            URL (str): address of site to open
        """
        self.browser.ChangeInstance(self.total_tabs-1)
        temp=self.browser.FixSiteAddress(URL)
        self.browser.AddInstance(temp,self.current_tab)
        self.total_tabs+=1
        self.browser.ChangeInstance(self.total_tabs-1)
        self.tabs.append(self.CurrentURLTitle())
        self.links.append(temp)
        self.browser.ChangeInstance(self.current_tab)
        
        
    def CloseCurrentTab(self)->None:
        """Closes tab that is currently focused.
        """
        self.tabs.pop(self.current_tab)
        self.links.pop(self.current_tab)
        self.total_tabs-=1
        self.browser.CloseInstance()
        if self.current_tab==self.total_tabs:
            self.current_tab-=1
        if self.current_tab<0:
            sys.exit('All tabs closed. Closing program')
        self.browser.ChangeInstance(self.current_tab)
#                                           Pretty much identical. Change to single one ? less code or easier to use?
    def CloseTitleTab(self,name:str)->None:
        """Closes tab based on title that is displayed on top (`<title>` tag in HTML)

        Args:
            name (str): title of tab.
        """
        for pos in range(0,len(self.tabs)):
            if self.tabs[pos].upper()==str(name).upper():
                break
        else:
            print('No tab with such Title. Did you type it correctly?')
            return
        self.tabs.pop(pos)
        self.links.pop(pos)
        self.total_tabs-=1
        self.browser.ChangeInstance(pos)
        self.current_tab=pos
        self.browser.CloseInstance()
        if self.current_tab==self.total_tabs:
            self.current_tab-=1
        if self.current_tab<0:
            sys.exit('All tabs closed. Closing program')
        self.browser.ChangeInstance(self.current_tab)
        
    def CloseURLTab(self,name:str)->None:
        """Closes tab based on URL of it.

        Args:
            name (str): URL of site.
        """
        for pos in range(0,len(self.links)):
            if self.links[pos].upper()==str(name).upper():
                break
        else:
            print('No tab with such URL. Did you type it correctly?')
            return
        self.links.pop(pos)
        self.tabs.pop(pos)
        self.total_tabs-=1
        self.browser.ChangeInstance(pos)
        self.current_tab=pos
        self.browser.CloseInstance()
        if self.current_tab==self.total_tabs:
            self.current_tab-=1
        if self.current_tab<0:
            sys.exit('All tabs closed. Closing program')
        self.browser.ChangeInstance(self.current_tab)                                              
        
    def ListTabsInfo(self):
        """Displays information about tabs.
        

        Returns [list] with:
            [0]: List of instances,
            [1]: List of tab titles,
            [2]: List of URL addresses
        """
        return [self.browser.ListInstances(),self.tabs,self.links]
    
    
    def GoRightTab(self):
        """Changes tab to one further right.
        """
        if self.current_tab<self.total_tabs-1:
            self.browser.ChangeInstance(self.current_tab+1)
            self.current_tab+=1
        else:
            print('There is no next tab.')
    
    def GoLeftTab(self):
        """Changes tab to one further left.
        """
        if self.current_tab-1>=0:
            self.browser.ChangeInstance(self.current_tab-1)
            self.current_tab-=1
        else:
            print('There is no previous tab.')
    
    def GoRightmostTab(self):
        """Changes tab to one on rightmost side.
        """
        self.browser.ChangeInstance(self.total_tabs-1)
        self.current_tab=self.total_tabs-1
    
    def GoLeftmostTab(self):
        """Changes tab to one on leftmost side.
        """
        self.browser.ChangeInstance(0)
        self.current_tab=0
        
        
    
    
            
        
if __name__ == '__main__': 
    a=EasySelenium('chrome')
    # a.OpenURL('https://www.python.org')
    a.PrepareDownloads(__file__)
    a.CheckDownloads()
    a.CloseBrowser()
    # a.BrowserWait(30)
    # a.CreateTroubleshootWindow(500,False)
    # print(a.CurrentURLAddress())
    # print(a.CurrentURLTitle())
    # a.AddTab('www.facebook.com')
    # a.AddTab('www.google.com')
    # a.GoRightTab()
    # a.OpenURL('https://www.wp.pl')
    # a.CloseURLTab(a.links[2])
    # a.OpenURL('www.google.com')
    # a.AddTab('www.minecraft.com')
    # a.GoLeftmostTab()
    # a.CloseCurrentTab()
    # a.GoRightmostTab()

    