from MySelenium.EasierSelenium import EasySelenium
import pyautogui

def CreateEpubs(link,last_chapter_link,next_chapter_identifier,method,browser_type):
    
        
    sele=EasySelenium(browser_type,True,__file__)
    sele.AddBrowserAddon('H:\Dokumenty\GitHub\PYTHON\WEB\EPUB CREATOR\okpfiebkkmjcnodegbbbiellepfhoglm.crx')
    sele.AddBrowserAddon('H:\Dokumenty\GitHub\PYTHON\WEB\EPUB CREATOR\extension_4_34_0_0.crx')
    sele.MaximizeWindow()
    #PIN ADDON
    addons_button=pyautogui.locateOnScreen('WEB\EPUB CREATOR\images\\addons_list_button.png',confidence=0.9)
    # print(addons_button)
    if addons_button:
        pyautogui.moveTo(addons_button.left+addons_button.width//2,addons_button.top+addons_button.height//2)
        pyautogui.click()
        pyautogui.sleep(0.2)
        pin_button=pyautogui.locateOnScreen('WEB\EPUB CREATOR\images\\addons_epub_list_button.png',confidence=0.9)
        if pin_button:
            pyautogui.moveTo(pin_button.left+pin_button.width-8,pin_button.top+pin_button.height//2)
            pyautogui.click()
    sele.OpenURL(link)
    sele.GoRightmostTab()
    sele.CloseCurrentTab()
    epub_button=pyautogui.locateOnScreen('WEB\EPUB CREATOR\images\\addons_epub_button.png',confidence=0.9)
    while sele.CurrentURLAddress()!=last_chapter_link:
        if epub_button:
            pyautogui.moveTo(epub_button.left+epub_button.width//2,epub_button.top+epub_button.height//2)
            pyautogui.click()
        while not sele.CheckDownloads(5):
            pass
        next_chapter=sele.SaveObjectInList(next_chapter_identifier,method)
        sele.PressObject(next_chapter)
        print('dziala dalej')


CreateEpubs(
            'https://www.readlightnovel.org/custom-made-demon-king/chapter-350',
            'http://www.readlightnovel.org/custom-made-demon-king/chapter-464',
            '/html/body/div[2]/div/div/div[1]/div/div[3]/ul/li[3]/a',
            'xpath',
            'chrome'
            )