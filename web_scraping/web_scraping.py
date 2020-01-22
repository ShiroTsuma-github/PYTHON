from lxml import html
import requests
page = requests.get('https://www.rapidtables.com/web/color/RGB_Color.html')
tree = html.fromstring(page.content)
testowe_wyniki=tree.xpath('//p[@class=code]/code()')
print(testowe_wyniki)

#//tbody//tr//td/text()