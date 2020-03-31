import math
import os
class produkty():
    def __init__(self,name,price):
        self.name=name
        self.price=price
waluty=[500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.01]
p1=produkty("Coca-Cola",2.5)
p2=produkty("Czipsy",1.8)
p3=produkty("Ice-tea",2.3)
p4=produkty("kawa",2)
p5=produkty("woda",4.5)
produkty=[p1,p2,p3,p4,p5]
wplacone=0
wplacone_m=[]
temp=0

ten_folder = os.path.dirname(os.path.abspath(__file__))
ten_plik=(os.path.join(ten_folder, 'data.txt'))
#=========================input=====================
"""
hand_input=False
if hand_input:
    end=False
    while end != True:
        t=input("Wsadź pieniądze:")
        if t == 'ok':
        wplacone.append(t)
"""   
try:
    f=open(ten_plik,'w+')
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
        """
        if i>=1:
            print(i ,"zł")
        else:
            print(int(i*100),"gr")
        """
        
        
    while (wplacone <produkty[x].price) :
        temp=float(input((f"Wsadź pieniądze: {round(produkty[x].price-wplacone,2)} zł: ")))
        if temp not in waluty:
            print("Automat nie przyjmuje podanej waluty. Spróbuj podać po monecie")
        else:
            wplacone=temp+wplacone
            wplacone_m.append(temp)
    f.write(f'[{produkty[x].name},{produkty[x].price},{wplacone_m},{abs(round(produkty[x].price-wplacone,2))}]')
    print(f'{produkty[x].name} zostanie zaraz wydany/a\n Pozostały balans:{abs(round(produkty[x].price-wplacone,2))}')
    for i in range()

    

    
    

finally:
    f.close()