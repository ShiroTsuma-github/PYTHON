from random import randrange
from math import floor,ceil
def test(tekst,dlugosc,ilosc_wywolan,x=0):
    print('wywolane',x)
    x+=1
    if len(str(tekst))==dlugosc:
        print(tekst)
    else:
        for i in range(0,ilosc_wywolan):
            x+=1
            test(f'{str(tekst)}{i}',dlugosc,ilosc_wywolan,x)
            
import os, sys
try: 
    sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
    from MyModules import CustomPrint as cp
except:
    print('Nie działa')      
def gen_list(n):
    l=[]
    t1=randrange(0,100)
    t2=randrange(0,100)
    for i in range(0,t1):
        x=randrange(1, 99,2)
        l.append(x)
    for i in range(0,t2):
        x=randrange(0,100,2)
        l.append(x)
            
    return l

lista=(gen_list(25))
# cp.printTable(lista)
def find(l,p=[0,0]):
    dl=len(l)
    if p[1]==0:
        p[1]=dl
    polowa=int(dl/2)
    if l[polowa]%2==0:
        pos2=polowa+1
        pos1=0

    elif l[polowa]%2==1:
        pos1=polowa
        pos2=dl
        p[0]+=polowa
    if dl<=2:
        if l[0]%2==0:
            return [l[0],p[0]]
        else:
            return([l[1],p[0]+1])
    
    x=find(l[pos1:pos2],p)
    if x:
        return x
cp.printTable(lista)
print(lista) 
x,y=(find(lista))
print(x,y,lista[y])
print('\n\n')
print(lista[y:])
print('\n\n')
print(lista[:y])
# cp.printTable(lista)