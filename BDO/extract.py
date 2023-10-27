import re

f=open('I:\\Pobrane\\temporary.txt')
content=f.read()
f.close()
pattern=r'<tr>.*?(href="\?t=(.*?)").*?(<br>(.*?)<a.*?\?t=(.*?)").*?(<br>(.*?)<a.*?\?t=(.*?)").*?(<br>(.*?)<a.*?\?t=(.*?)").*?(<br>(.*?)<a.*?\?t=(.*?)").*?(<br>(.*?)<a.*?\?t=(.*?)")?.*?<\/tr>'
wyn=re.findall(pattern,content)
if wyn:
    for line in wyn:
        # res="".join([pos for pos in line])
        # pattern=r'href=".*?"'
        # print(res,'\n\n')
        try:
            print(line[3], end=' ')
            print(line[4], end='\n')
            print(line[6], end='  ')
            print(line[7], end='\n')
            print(line[9], end='  ')
            print(line[10], end=' ')
            print(line[12], end='\n')
            print(line[13], end=' ')
            print(line[14], end='\n')
            print(line[15], end='  ')
            print(line[16], end='\n')
            print(line[17], end=' ')
            print(line[18], end='\n')
        except :
            print('\n')
        # w=re.search(pattern,res)
        # if w:

    
    
