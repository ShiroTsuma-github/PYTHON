from lxml import html
import requests
from bs4 import BeautifulSoup
import os

page = requests.get('https://mega.nz/#!RPATBKzT!QddA0bTmdE_oepdMDCjPgfXW2KYsZ_WT4R5yeYcZHpU%E2%9C%85')
tree = html.fromstring(page.content)
title= tree.xpath('//span[1]/text()')
print()
'''
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'zapis.txt')
text_zapis=open(my_file,"w")


content=page.content
#print(content)
soup= BeautifulSoup(content,'html.parser')
text_zapis.write(str(soup))
print(str(soup.prettify()))
print(soup.findAll('span.filename'))
text_zapis.close()
'''