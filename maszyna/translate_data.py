import os
import ast
"""
class translate():
    def __init__(self,nazwa,cena,bilans,wpłacona_gotówka,stan_po_operacji,czas_operacji,wydane_waluty):
        self.nazwa=nazwa
        self.cena=cena
        self.bilans=bilans
        self.wpłacona_gotówka=wpłacona_gotówka
        self.stan_po_operacji=stan_po_operacji
        self.czas_operacji=czas_operacji
        self.wydane_waluty=wydane_waluty
        """
dane=[]
lineList=[]
def get_data():
    count_char=0
    count_char2=0
    temp=0
    o_x=0
    ten_folder = os.path.dirname(os.path.abspath(__file__))
    ten_plik=(os.path.join(ten_folder, 'data.txt'))
    lineList = [line.rstrip('\n') for line in open(ten_plik)]
    
    for j in range(0,len(lineList)):
        if lineList[j] == '%%%%%':
            print(f'Operacja {temp}: ')
            temp+=1
            o_x=0
        else:
            print(lineList[j])
get_data()