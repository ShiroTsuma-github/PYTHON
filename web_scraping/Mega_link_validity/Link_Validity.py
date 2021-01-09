# IMPORTING SELENIUM COMPONENTS
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
#IMPORTING SYSTEM CONTROL
from os import system,name,path
from time import sleep
from progressbar import ProgressBar,Bar

# FILE AND SITE LINKS
folder_path=path.dirname(__file__)
folder=path.relpath(folder_path)
file_link=f'{folder}\\linki.txt'
file_write_good=f'{folder}\\zapis_dobre.txt'
file_write_bad=f'{folder}\\zapis_zle.txt'
validity_link_site='http://dailyleech.com/check_mega/'

#OPENING AND READING FROM FILE
with open(file_link,'r') as f:
    content=f.read()

#CREATING LIST FROM LINKS
lista=content.split('\n')

# CONFIGURING BROWSER
opts=Options()
opts.headless=True
assert opts.headless
browser=Firefox(options=opts)
browser.get(validity_link_site)



# CYCLING THROUGH OBJECTS IN LIST
with ProgressBar(max_value=len(lista)) as bar:
    for i,item in enumerate(lista):
        search_form=browser.find_element_by_id('links')
        search_form.send_keys(item)
        button=browser.find_element_by_id('submit')
        button.click()
        results=browser.find_element_by_xpath('/html/body/center/center[2]/textarea')
        if results.text=='Link Dead.':
            f1=open(file_write_bad,'a+')
            f1.write(f'{item}\n')
            f1.close()
        else:
            f2=open(file_write_good,'a+')
            f2.write(f'{item}\n')
            f2.close()
        bar.update(i)
        
#CLOSING SESSION
browser.close()
quit()
    
    