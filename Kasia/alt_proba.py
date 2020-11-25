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

def rysuj_plansze(komorki,baseL,baseP):         
    normal_cells=6
    board_height=12
    for y in range(0,board_height):
        if y>=2 and y<=board_height-3:
            rysuj_pole(szer=12,wys=8,akt_poz=y-2,DATA=baseL)
            Nprint(' ')
        else:
            Nprint(13*' ')
        for i in range(0,normal_cells):
            if y>6:
                rysuj_pole(szer=11,wys=6,akt_poz=y,DATA=komorki[normal_cells+i])
            else:
                rysuj_pole(szer=11,wys=6,akt_poz=y,DATA=komorki[normal_cells-i-1])
            Nprint(' ')
        if y>=2 and y<=board_height-3:
            rysuj_pole(szer=12,wys=8,akt_poz=y-2,DATA=baseP)
        print('')
    
def poprawny_input(table,player):
    if (player=='P' and sum(table[6:])==0) or(player=='L' and sum(table[:6])==0):
        return -1
    while True:
        if player=='P':
            color(red=True,word=f'Podaj Pole graczu {player} [1-6]: ',end2='\n')
        else:
            color(blue=True,word=f'Podaj Pole graczu {player} [1-6]: ',end2='\n')
        try:
            _input=int(input(''))-1
        except:
            continue
        if _input in [0,1,2,3,4,5]:
            if player=='P':
                _input+=6
            else:
                _input=5-_input
            if table[_input]>0:
                return _input
            else:
                print('Error: [EMPTY FIELD]')
        else:
            print('Error: [VALUE OUT OF RANGE]')

def czy_koniec(komorki,baseL,baseP,player):
    Lewy=komorki[:6]
    Prawy=komorki[6:]
    if sum(Lewy)==0 or sum(Prawy)==0:
        if baseL+sum(Lewy)>baseP+sum(Prawy) and player=='L':
            print('Gratulacje Wygranej dla Gracza L')
            return True
        elif baseP+sum(Prawy)>baseL+sum(Lewy) and player=='P':
            print('Gratulacje Wygranej dla Gracza P')
            return True
        else:
            print('Gratulacje remisu')
            return True

def tura(komorki,baseL,baseP,Turn,pole,player):
    ilosc=komorki[pole]
    komorki[pole]=0
    flag=0
    for pos in range(0,ilosc):
        if flag==1:
            flag=0
            komorki[pole+1]+=1
            """
            if player=='P' and pole+1>5:
                    baseP+=komorki[11-(pole+1)]
                    komorki[11-(pole+1)]=0
            """
        elif pole<=12:
            if pole==11:
                if pos==ilosc-1 and player=='P':
                    Turn+=1
                baseP+=1
                pole+=1
                continue
            elif pole==5:
                if pos==ilosc-1 and player=='L':
                    Turn+=1
                baseL+=1
                flag=1
                continue
            elif pole==12:
                pole=0  
                komorki[pole]+=1
                continue
            
            komorki[pole+1]+=1
            
        if pos==ilosc-1:
            if player=='L' and pole+1<6:
                baseL+=komorki[11-(pole+1)]
                komorki[11-(pole+1)]=0
            
            elif player=='P' and pole+1>5:
                baseP+=komorki[11-(pole+1)]
                komorki[11-(pole+1)]=0
                
                # od ilosci pozycji [0-11] odejmujemy pole+1
        pole+=1
    return baseL,baseP,Turn
            
def main():
    komorki=[3,0,1,0,0,10,14,0,0,0,0,1]
    baseP=0
    baseL=0
    Turn=0
    First_player=str(input('Podaj Zaczynającego gracza: [L/P]: ').upper())
    Second_player=str('LP'.replace(First_player.upper(),''))
    while Turn>=0 and (First_player=='L' or First_player=='P'):
        rysuj_plansze(komorki,baseL,baseP)
        if Turn%2==0:
            player=First_player
        else:
            player=Second_player
        pole=poprawny_input(komorki,player)
        if pole==-1:
            if czy_koniec(komorki,baseL,baseP,player):
                break
        
        baseL,baseP,Turn=tura(komorki,baseL,baseP,Turn,pole,player)
        Turn+=1
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
main()