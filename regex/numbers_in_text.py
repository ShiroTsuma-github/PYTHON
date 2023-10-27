import re


text='a1dfsD243543dfdsf'

liczby=re.findall('[0-9]', text)
print(len(liczby))
print(liczby)
duza_litera=re.findall('[A-Z]', text)
print(duza_litera)