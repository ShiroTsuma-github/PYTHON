from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException,NoSuchElementException

class SitesInformation():
    def __init__(self,Site_Load_Delay=5,headless=True):
        self.__init_selenium_options=Options()
        self.__init_selenium_options.headless=headless
        self.browser=''
        self.site_load_delay=Site_Load_Delay
        self.browser.close()
    
    @property
    def site_load_delay(self):
        return self.__site_load_delay
    @property
    def browser(self):
        return self.__browser
    @browser.setter
    def browser(self,browser):
        self.__browser=Firefox(options=self.__init_selenium_options)
    @site_load_delay.setter
    def site_load_delay(self,site_load_delay):
        try:
            if site_load_delay>0 and site_load_delay<20:
                self.__site_load_delay=site_load_delay
        except:
            self.__site_load_delay=5
            
    def WaitForElement(self,object,param,object2,param2,debug=False):
        if param=='XPATH':
            by_what=By.XPATH
        elif param=='CLASS_NAME':
            by_what=By.CLASS_NAME
        elif param=='ID':
            by_what=By.ID
        elif param=='CSS_SELECTOR':
            by_what=By.CSS_SELECTOR
        else:
            by_what=By.ID
        if param2=='XPATH':
            by_what2=By.XPATH
        elif param2=='CLASS_NAME':
            by_what2=By.CLASS_NAME
        elif param2=='ID':
            by_what2=By.ID
        elif param2=='CSS_SELECTOR':
            by_what2=By.CSS_SELECTOR
        else:
            by_what2=By.ID
        try:
            WebDriverWait(self.browser,self.site_load_delay).until(EC.presence_of_element_located((by_what,object)))
            return 'E200'
        except TimeoutException:
            if debug:
                print(f'There occurred an error when trying to access [ {object} ]')
            try:
                WebDriverWait(self.browser,self.site_load_delay).until(EC.presence_of_element_located((by_what2,object2)))
                return 'E404'
            except TimeoutException:
                return 'Error'
            # /html/body/main/div/div/h1
        