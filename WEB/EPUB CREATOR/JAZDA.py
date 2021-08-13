from MySelenium.EasierSelenium import EasySelenium
import pyautogui

def CreateEpubs(link,last_chapter_link,next_chapter_identifier,method,browser_type):
    
        
    sele=EasySelenium(browser_type)
    sele.AddBrowserAddon('H:\Dokumenty\GitHub\PYTHON\WEB\EPUB CREATOR\okpfiebkkmjcnodegbbbiellepfhoglm.crx')
    sele.MaximizeWindow()
    #PIN ADDON
    addons_button=pyautogui.locateOnScreen('WEB\EPUB CREATOR\images\\addons_list_button.png',confidence=0.9)
    print(addons_button)
    if addons_button:
        pyautogui.moveTo(addons_button.left+addons_button.width//2,addons_button.top+addons_button.height//2)
        pyautogui.click()
        pyautogui.sleep(0.2)
        pin_button=pyautogui.locateOnScreen('WEB\EPUB CREATOR\images\\addons_pin_button.png',confidence=0.9)
        if pin_button:
            pyautogui.moveTo(pin_button.left+pin_button.width//2,pin_button.top+pin_button.height//2)
            pyautogui.click()
    sele.OpenURL(link)
    epub_button=pyautogui.locateOnScreen('WEB\EPUB CREATOR\images\\addons_epub_button.png',confidence=0.9)
    if epub_button:
        pyautogui.moveTo(epub_button.left+epub_button.width//2,epub_button.top+epub_button.height//2)
        pyautogui.click()
    while sele.CurrentURLAddress!=last_chapter_link:
        print('xD')
        sele.BrowserWait(5)


CreateEpubs(
            'https://www.readlightnovel.org/custom-made-demon-king/chapter-350',
            'http://www.readlightnovel.org/custom-made-demon-king/chapter-464',
            'next next-link',
            'class_name',
            'chrome'
            )