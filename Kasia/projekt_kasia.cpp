#include <iostream>

using namespace std;

const int wys_planszy=12;
const int wys_komorki=6;
const int szer_komorki=11;
const int wys_bazy=8;
const int szer_bazy=12;
const int komorki_w_rzedzie=6;
const int ilosc_rzedow=2;

int dlugosc_liczby(int k)
{
    int ilosc_cyfr = 0;
    do {
         ++ilosc_cyfr; 
         k /= 10;
    } while (k);
    return ilosc_cyfr;
}

void rysuj_fragment(const int wys_komorki,const int szer_kom,int pozycja_y,const int liczba)
{
    int ile_pominac=0;
    int szer_liczby=dlugosc_liczby(liczba);
    if(pozycja_y>=wys_komorki)  {pozycja_y-=wys_komorki;}

	for(int pozycja_x=0;pozycja_x<szer_kom;pozycja_x++)
    {
        // jezeli dlugosc liczby jest wieksza nic 1,to okresla ile razy ma nic nie wyswietlic
        if(ile_pominac>0)   {ile_pominac--;continue;}
        // dla 4 rogow jezeli pasuje X i Y,to rysuje '+'
        if((pozycja_x==0 or pozycja_x==szer_kom-1) and (pozycja_y==0 or pozycja_y==wys_komorki-1))    {cout<<'+';}
        // dla gory i dolu wyswietla '-'
        else if(pozycja_y==0 or pozycja_y==wys_komorki-1)   {cout<<'-';}
        // dla lewej i prawej strony komorki wyswietla '|' 
        else if(pozycja_x==0 or pozycja_x==szer_kom-1)      {cout<<'|';}
        // gdy liczba ma szerokosc 1 nic nie zmieniamy,wiec [-1+1]
        else if(pozycja_x==(szer_kom-szer_liczby+1)/2 and pozycja_y==wys_komorki/2)
        {
            cout<<liczba;
            ile_pominac=szer_liczby-1;
        }
        // jezeli jest pustym miejscem w srodku komorki,to wyswietla ' '
        else    {cout<<' ';}
    }
}

int suma_rzedu(const int tablica[])
{
    unsigned int suma_pozycji=0;
    for(int i=0;i<komorki_w_rzedzie;i++)
    {
        suma_pozycji+=tablica[i];
    }
    return suma_pozycji;
}
int podziel_tablice(const int tablica_glowna[],int tablica[],const int od_liczby,const int do_liczby)
{

    for(int i=od_liczby;i<do_liczby;i++)
    {
        tablica[i-od_liczby]=tablica_glowna[i];
    }
}
int poprawna_pozycja(int tablica[],const char Gracz,const int suma_gorna,const int suma_dolna)
{
    char pole;
    unsigned int pozycja;
    if((Gracz=='P' and suma_dolna==0) or (Gracz=='L' and suma_gorna==0))      {return -1;}
    
    while(true)
    {   
        cout<<"Podaj pole do wykonania ruchu [A-F]"<<endl;
        cin>>pole;
        cout<<endl;
        switch(pole)
        {
            case 'A': case 'a':
                pozycja=0;
                break;
            case 'B': case 'b':
                pozycja=1;
                break;
            case 'C': case 'c':
                pozycja=2;
                break;
            case 'D': case 'd':
                pozycja=3;
                break;
            case 'E': case 'e':
                pozycja=4;
                break;
            case 'F': case 'f':
                pozycja=5;
                break;      
            default:
                cout<<"Błąd: [Wartość poza zakresem]"<<endl;
                pozycja=10;        
        }
        if(pozycja>=0 and pozycja<6)    
        {   
            if(Gracz=='P')  {pozycja=pozycja+komorki_w_rzedzie;}
            else {pozycja=komorki_w_rzedzie-1-pozycja;}
            if(tablica[pozycja]>0)  {return pozycja;}    
            
            else{cout<<"Błąd: [Podane pole jest puste]"<<endl;}
        }
    }
}
int przenies_do_bazy(int tablica[],int *baza_lewa,int *baza_prawa)
{
    for(int i=0;i<komorki_w_rzedzie*ilosc_rzedow;i++)
    {
        if(i<komorki_w_rzedzie) {*baza_lewa=tablica[i]}
    }
}
int czy_skonczyc(int baza_lewa,int baza_prawa,const char aktualny_gracz)
{
    if((baza_lewa>baza_prawa)and aktualny_gracz=='L')
    {   cout<<"Gratulacje wygranej dla Gracza grającego do Lewej Bazy";}
    else if((baza_prawa>baza_lewa)and aktualny_gracz=='P')
    {   cout<<"Gratulacje wygranej dla Gracza grającego do Prawej Bazy";}
    else    {   cout<<"Gratulacje remisu";}
    return 1;
}
void wyswietl_plansze(const int komorki[],const int baza_lewa,const int baza_prawa)
{
    for(int y=0;y<wys_planszy;y++)
    {
        // rysowanie lewej bazy
        // od (12-8)/2=2 do 12-1-(12-8)/2=9     <[2-9]>
        if(y>=(wys_planszy-wys_bazy)/2 and y<=wys_planszy-1-(wys_planszy-wys_bazy)/2)
        {
            // rysuje linie bazy,jezeli w odpowiednich polach,a podaje funkcji Y mniejszy o tyle, od ktorej zaczyna linijki(jezeli wyswietla od 2,to podaje Y=0) 
            rysuj_fragment(wys_bazy,szer_bazy,y-(wys_planszy-wys_bazy)/2,baza_lewa);
            cout<<' ';
        }
        else{   for(int i=0;i<szer_bazy+1;i++)      {cout<<' ';}}
        // tyle razy ile jest komorek w rzedzie pisze odpowiednia linijke
        for(int i=0;i<komorki_w_rzedzie;i++)
        {
            // jezeli dalej jestemy w obrebie wysokosci pierwszego rzedu komorek,to liczba brana z listy gornych komorek
            if(wys_komorki>y)       {rysuj_fragment(wys_komorki,szer_komorki,y,komorki[komorki_w_rzedzie-i-1]);}
            // jezeli poza wysokoscia gornych komorek,to liczba brana z listy dolnych komorek
            else{rysuj_fragment(wys_komorki,szer_komorki,y,komorki[komorki_w_rzedzie+i]);}
            // po kazdej komorce robi ' '
            cout<<' ';
        }
        // rysowanie bazy po prawej stronie
        if(y>=(wys_planszy-wys_bazy)/2 and y<=wys_planszy-1-(wys_planszy-wys_bazy)/2)
        {
            // rysuje linie bazy,jezeli w odpowiednich polach,a podaje funkcji Y mniejszy o tyle, od ktorej zaczyna linijki(jezeli wyswietla od 2,to podaje Y=0) 
            rysuj_fragment(wys_bazy,szer_bazy,y-(wys_planszy-wys_bazy)/2,baza_prawa);
            cout<<' ';
        }
        cout<<endl;
    }
        cout<<"                  A           B           C           D           E           F"<<endl;
}

void wyczysc(int komorki[])
{
    for(int pos=0;pos<komorki_w_rzedzie*ilosc_rzedow;pos++)
    {
        komorki[pos]=0;
    }
}
void Wykonaj_Ture(int komorki[],int *baza_lewa,int *baza_prawa,int *Tura,int pole,const char Aktualny_gracz)
{
    int ilosc=komorki[pole];
    komorki[pole]=0;
    bool Flaga_zaczekania_tury=false;
    for(int pos=0;pos<ilosc;pos++)
    {
        if(Flaga_zaczekania_tury==1)    {Flaga_zaczekania_tury=false;komorki[pole+1]+=1;}   
        //mniejsze lub rowne 12
        else if(pole<=komorki_w_rzedzie*ilosc_rzedow)
        {           //rowne 11
            if(pole==komorki_w_rzedzie*ilosc_rzedow-1)
            {   //jezeli ostatni kamien i gracz prawy do prawej bazy, to tura++,wiec znowu bedzie on
                if(pos==ilosc-1 and Aktualny_gracz=='P')    {*Tura++;}
                *baza_prawa++;pole++;continue;
            }   //rowne 12
            else if(pole==komorki_w_rzedzie*ilosc_rzedow)   {pole=0;komorki[pole]+=1;continue;}
            //rowne 5 pole
            else if(pole==komorki_w_rzedzie-1)
            {   //jezeli ostatni kamien to kolejny ruch tego gracza
                if(pos==ilosc-1  and Aktualny_gracz=='L')   {*Tura++;}
                baza_lewa++;Flaga_zaczekania_tury=true;continue;
            }
            komorki[pole+1]+=1;
        }
        if(pos==ilosc-1)
        {
            if(Aktualny_gracz=='P' and pole+1>5)
            {
                *baza_prawa+=komorki[(komorki_w_rzedzie*ilosc_rzedow-1)-(pole+1)];
                komorki[(komorki_w_rzedzie*ilosc_rzedow-1)-(pole+1)]=0;
            }
            else if(Aktualny_gracz=='L' and pole+1<6)
            {
                *baza_lewa=komorki[(komorki_w_rzedzie*ilosc_rzedow-1)-(pole+1)]
                komorki[(komorki_w_rzedzie*ilosc_rzedow-1)-(pole+1)]=0;
            } 
        }
        pole++;
    }
}


int main()
{
    int komorki[komorki_w_rzedzie*ilosc_rzedow]={1,2,3,4,5,6,7,8,9,10,11,12};
    int czesc_1_tablicy[komorki_w_rzedzie];
    int czesc_2_tablicy[komorki_w_rzedzie];
    unsigned int suma_gorna,suma_dolna;
    int baza_prawa=0,baza_lewa=0;
    unsigned int Tura=0;
    const char Gracz_pierwszy='P';    //tu trzeba ze pierwszy gracz to dol i gra do prawej bazy
    const char Gracz_drugi='L';
    char Aktualny_gracz;
    while(Tura>=0)
    {
    wyswietl_plansze(komorki,baza_lewa,baza_prawa);

    podziel_tablice(komorki,czesc_1_tablicy,(komorki_w_rzedzie-komorki_w_rzedzie),komorki_w_rzedzie);
    podziel_tablice(komorki,czesc_2_tablicy,komorki_w_rzedzie,komorki_w_rzedzie*ilosc_rzedow);
    suma_gorna=suma_rzedu(czesc_1_tablicy);
    suma_dolna=suma_rzedu(czesc_2_tablicy);
    if(Tura%2==0)   {Aktualny_gracz=Gracz_pierwszy;}
    else    {Aktualny_gracz=Gracz_drugi;}

    int pole=poprawna_pozycja(komorki,Aktualny_gracz,suma_gorna,suma_dolna);
    if(pole==-1){
        przenies_do_bazy(komorki,&baza_lewa,&baza_prawa);
        if(czy_skonczyc(baza_lewa,baza_prawa,Aktualny_gracz)){
            // wyczysc(komorki);
            wyswietl_plansze(komorki,baza_lewa,baza_prawa);
            break;
        }
    }
    Wykonaj_Ture(komorki,&baza_lewa,&baza_prawa,&Tura,pole,Aktualny_gracz);
    Tura++;
    }
}