import os
from colored import fg,bg,attr
ten_folder = os.path.dirname(os.path.abspath(__file__))
ten_plik=(os.path.join(ten_folder, 'data.txt'))
uczniowie_data=open(ten_plik,'r')
uczniowie=[]
for i in uczniowie_data:
    uczniowie.append(list(i.splitlines()))
    #use = list(map(lambda x: x-min(i), uczen_4))

def correct(l1):
    temp=[]
    hold=0
    for i in uczniowie[l1][0]:
        try:
            if int(i) in range(0,10):
                hold=str(hold)+str(i)
        except ValueError:
            if i == "," or i==";":
                temp.append(int(hold))
                hold=0
    return temp

for i in range(0,len(uczniowie)):
    data=correct(i)
    use=list(map(lambda x: x-min(data), data))
    print(f"Znormalizowane liczby dla ucznia nr:{i+1} to: ")
    for j in use:
        print(round(j*(1/max(use)),4),end=' ')
    print(f"\nPrzy kroku {round(1/max(use),4)}, z danymi wejsciowymi:\n{uczniowie[i][0]}")
    print('===========================================')
"""
uczen_4  =  [12, 23, 12, 5, 16, 4, 6, 22] 
use = list(map(lambda x: x-min(uczen_4), uczen_4))
for i in use:
    print(round(i*(1/max(use)),4))
"""