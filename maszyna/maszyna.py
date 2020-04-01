import math
import os
import time
from decimal import *
getcontext().prec=2
t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

class produkty():
    def __init__(self,name,price):
        self.name=name
        self.price=price
waluty=[500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
p1=produkty("Coca-Cola",2.5)
p2=produkty("Czipsy",1.8)
p3=produkty("Ice-tea",2.3)
p4=produkty("kawa",2)
p5=produkty("woda",4.5)
p6=produkty('choco',1.87)
produkty=[p1,p2,p3,p4,p5,p6]
wplacone_m=[]
koniec=''

ten_folder = os.path.dirname(os.path.abspath(__file__))
ten_plik=(os.path.join(ten_folder, 'data.txt'))
#=========================input=====================
def info():
    temp=0
    print("Wybierz produkt")
    for i in produkty:
        #print(i)
        print(f'[{temp+1}]',i.name,' : ',i.price)
        temp+=1
    print("=============================")
    x=int(input("Wybierz opcję: "))-1
    temp=0
    print("Obsługiwane waluty")
    for i in waluty:
        print(i,"zł")
    return x
    """
    if i>=1:
        print(i ,"zł")
    else:
        print(int(i*100),"gr")
    """

def check(money):
    x=info()
    wplacone=money
    while (wplacone <produkty[x].price) :
            temp=float(input((f"Wsadź pieniądze: {round(produkty[x].price-wplacone,2)} zł: ")))
            if temp not in waluty:
                print("Automat nie przyjmuje podanej waluty. Spróbuj podać po monecie")
            else:
                wplacone=temp+wplacone
                wplacone_m.append(temp)
    f.write(f'%%%%%\nNazwa: {produkty[x].name}\nCena: {produkty[x].price}\nWplacone lacznie: {wplacone}\nWplacone: {str(wplacone_m)}zl\nReszta: {abs(round(produkty[x].price-wplacone,2))}\nGodzina: {current_time}\n')
    print("==========================================================")
    print(f'{produkty[x].name} zostanie zaraz wydany/a\n Pozostały balans:{abs(round(produkty[x].price-wplacone,2))} zł')
    print('==========================================================')
    return round(wplacone-produkty[x].price,2)
    
try:
    f=open(ten_plik,'a')
    end=False
    balans=check(0)
    while end != True:
        koniec=str(input("Jeżeli chcesz kupić kolejną rzecz wybierz [DALEJ], w innym przypadku wybierz [END]: "))
        if koniec.upper() == 'END':
            print('==========================================')
            reszta=balans
            while reszta>=0:
                f.write('Wydane nominaly:')
                for i in range(0,len(waluty)):
                    if reszta>=waluty[i]:
                        if Decimal(waluty[i])*2<=reszta:
                            temp=2
                        else:
                            temp=1
                        print(f'wydaje {temp}x{waluty[i]} zł')
                        f.write(f' {temp}*{waluty[i]}zl')
                        reszta-=temp*waluty[i]
                        reszta=float("{:.2f}".format(reszta))
                if reszta<=0.009:
                    break
            f.write('\n')
            end=True
            f.write('\n')
            f.write(f'End\n')
            f.write('\n')
        elif koniec.upper() == 'DALEJ':
            f.write('\n')
            f.write('Continue\n')
            f.write('\n')
            balans=check(balans)
            

    

    
    

finally:
    f.close()