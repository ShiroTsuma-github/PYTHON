from namedlist import namedlist
from dataclasses import dataclass
from colored import fg,bg,attr

# funkcje customowe do wyswietlania i formatowania tekstu
def Nprint(text,end='',flush=True):
    print(text,end=end,flush=flush)
def Cprint(text,end='\n',flush=False):
    if text.side.upper()=='RED':
        color(text.ilosc,red=True,end=end,flush=flush)
    elif text.side.upper()=='BLUE':
        color(text.ilosc,blue=True,end=end,flush=flush)
    else:
        color(text.ilosc,end='',flush=flush)
def color(word,end2='\r',flush2=False,red=False,blue=False):
    res = attr('reset')
    if red == True:
        C_color='#FF0000'
    elif blue == True:
        C_color='#0000FF'
    else:
        C_color='#00FF00'
    _color=bg(C_color)+fg("#FFFFFF")
    print(_color+f" {word}  ",res,end=end2,flush=flush2)

def rysuj_pole(wys,szer,akt_poz,DATA=0):
    passing=0
    if akt_poz>=wys:
        akt_poz-=wys
    for i in range(0,szer):
        if passing>0:
            passing-=1
            continue
        if (i==0 or i==szer-1) and (akt_poz==0 or akt_poz==wys-1):
            Nprint('+')
        elif akt_poz==0 or akt_poz==wys-1:
            Nprint('-')
        elif i==0 or i==szer-1:
            Nprint('|')
        elif i==(szer-len(str(DATA))+1)//2 and akt_poz==wys//2:
            Nprint(DATA)
            passing=len(str(DATA))-1
        else:
            Nprint(' ')

def rysuj_plansze(red,blue,baseR,baseB):         
    normal_cells=6
    board_height=12
    for y in range(0,board_height):
        if y>=2 and y<=board_height-3:
            rysuj_pole(szer=12,wys=8,akt_poz=y-2,DATA=baseR)
            Nprint(' ')
        else:
            Nprint(13*' ')
        for i in range(0,normal_cells):
            if y>6:
                rysuj_pole(szer=11,wys=6,akt_poz=y,DATA=blue[i])
            else:
                rysuj_pole(szer=11,wys=6,akt_poz=y,DATA=red[i])
            print(' ',end='')
        if y>=2 and y<=board_height-3:
            rysuj_pole(szer=12,wys=8,akt_poz=y-2,DATA=baseB)
        print('')
    
def poprawny_input(table,player):
    while True:
        if sum(table)==0:
            return -1
        if player=='P':
            color(red=True,word=f'Podaj Pole graczu {player} [1-6]: ',end2='\n')
        else:
            color(blue=True,word=f'Podaj Pole graczu {player} [1-6]: ',end2='\n')
        try:
            _input=int(input(''))-1
        except:
            continue
        if _input in [0,1,2,3,4,5]:
            if table[_input]>0:
                return _input
            else:
                print('Error: [EMPTY FIELD]')
        else:
            print('Error: [VALUE OUT OF RANGE]')
# do zrobienia
def czy_koniec(Lewy,Prawy,baseL,baseP,player):
    if sum(Lewy)==0 or sum(Prawy)==0:
        if baseL+sum(Lewy)>baseP+sum(Prawy) and player=='L':
            print('Gratulacje Wygranej dla Gracza L')
            return True
        elif baseP+sum(Prawy)>baseL+sum(Lewy) and player=='P':
            print('Gratulacje Wygranej dla Gracza P')
        else:
            print('Gratulacje remisu')
            return True

def tura_lewy(Lewy,Prawy,baseL,baseP,Turn,pole):
    positional_counter=1
    ilosc=Lewy[pole]
    Lewy[pole]=0
    for pos in range(0,ilosc):
        if pole-positional_counter>=0:
            if pos==ilosc-1:
                if Prawy[pole-positional_counter]>0 and Lewy[pole-positional_counter]==0:
                    baseL+=Prawy[pole-positional_counter]
                    Prawy[pole-positional_counter]=0
            Lewy[pole-positional_counter]+=1
        elif pole-positional_counter==-1:
            baseL+=1
            if pos==ilosc-1:
                Turn+=1
            reversed_positional_counter=0
        elif pole-positional_counter<-1:
            if reversed_positional_counter!=6:
                Prawy[reversed_positional_counter]+=1
            if reversed_positional_counter==6:
                positional_counter=0
                baseP+=1
                continue
            reversed_positional_counter+=1
        positional_counter+=1 
    return Lewy,Prawy,baseL,baseP,Turn  

def tura_prawy(Lewy,Prawy,baseL,baseP,Turn,pole):
    positional_counter=1
    ilosc=Prawy[pole]
    Prawy[pole]=0
    for pos in range(0,ilosc):
        if pole+positional_counter<=5:
            if pos==ilosc-1:
                if Lewy[pole+positional_counter]>0 and Prawy[pole+positional_counter]==0:
                    baseP+=Lewy[pole+positional_counter]
                    Lewy[pole+positional_counter]=0
            Prawy[pole+positional_counter]+=1
        elif pole+positional_counter==6:
            baseP+=1
            if pos==ilosc-1:
                Turn+=1
            reversed_positional_counter=5
        elif pole+positional_counter>6:
            if reversed_positional_counter>=0:
                Lewy[reversed_positional_counter]+=1
            if reversed_positional_counter<0:
                positional_counter=0-pole
                baseL+=1
                continue
            reversed_positional_counter-=1
        positional_counter+=1  
    return Lewy,Prawy,baseL,baseP,Turn
        

def main():
    Lewy=[1,0,0,0,0,0]
    Prawy=[0,0,0,0,0,1]
    baseP=0
    baseL=0
    Turn=0
    First_player=str(input('Podaj Zaczynającego gracza: [L/P]: ').upper())
    Second_player=str('LP'.replace(First_player.upper(),''))
    while Turn>=0 and (First_player=='L' or First_player=='P'):
        rysuj_plansze(Lewy,Prawy,baseL,baseP)
        if Turn%2==0:
            player=First_player
        else:
            player=Second_player
        if player=='L':
            pole=poprawny_input(Lewy,player)
            if pole==-1:
                if czy_koniec(Lewy,Prawy,baseL,baseP,player):
                    break  
            Lewy,Prawy,baseL,baseP,Turn=tura_lewy(Lewy,Prawy,baseL,baseP,Turn,pole)
        else:
            pole=poprawny_input(Prawy,player)
            if pole==-1:
                if czy_koniec(Lewy,Prawy,baseL,baseP,player):
                    break  
            Lewy,Prawy,baseL,baseP,Turn=tura_prawy(Lewy,Prawy,baseL,baseP,Turn,pole)
        Turn+=1
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
main()