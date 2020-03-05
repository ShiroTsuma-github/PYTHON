import urllib.request

def get_html(url):
    f=open('htmlcode.txt','w')
    page=urllib.request.urlopen(url)
    pagetext=page.read() ## Save the html and later save in the file
    f.write(pagetext)
    f.close()

import urllib.request    
urllib.request.urlretrieve("https://mega.nz/#!RPATBKzT!QddA0bTmdE_oepdMDCjPgfXW2KYsZ_WT4R5yeYcZHpU%E2%9C%85", "test.txt")