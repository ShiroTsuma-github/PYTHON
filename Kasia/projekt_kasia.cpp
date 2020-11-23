#include <iostream>

using namespace std;

int dlugosc_liczby(int k)
{
    int ilosc_cyfr = 0;
    do {
         ++ilosc_cyfr; 
         k /= 10;
    } while (k);
    return ilosc_cyfr;
}
int suma_rzedu(const int tablica[],const int komorki_w_rzedzie)
{
    unsigned int suma_pozycji=0;
    for(int i=0;i<komorki_w_rzedzie;i++)
    {
        suma_pozycji+=tablica[i];
    }
    return suma_pozycji;
}
int poprawna_pozycja(int aktualna_strona[],const int komorki_w_rzedzie)
{
    char pole;
    unsigned int pozycja;
    while(true)
    {
        if(suma_rzedu(aktualna_strona,komorki_w_rzedzie)==0)      {return -1;}   
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
                cout<<"Błąd: [Wartość poza zakresem]";
                pozycja=10;        
        }
        if(pozycja>=0 and pozycja<6)    
        {   
            if(aktualna_strona[pozycja]>0)  {return pozycja;}    
            
            else{cout<<"Błąd: [Podane pole jest puste]";}
        }
    }
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
int czy_skonczyc(
    const int gorne_komorki[],
    const int dolne_komorki[],
    int baza_lewa,
    int baza_prawa,
    const char aktualny_gracz,
    const int komorki_w_rzedzie)
{
    unsigned int suma_gora=suma_rzedu(gorne_komorki,komorki_w_rzedzie);
    unsigned int suma_dol=suma_rzedu(dolne_komorki,komorki_w_rzedzie);

    if(suma_gora==0 or suma_dol==0)
    {
        if((baza_lewa+suma_gora>baza_prawa+suma_dol)and aktualny_gracz=='L')
        {
            cout<<"Gratulacje wygranej dla Gracza grającego do Lewej Bazy";
            return 1;
        }
        else if((baza_prawa+suma_dol>baza_lewa+suma_gora)and aktualny_gracz=='P')
        {
            cout<<"Gratulacje wygranej dla Gracza grającego do Prawej Bazy";
            return 1;
        }
        else 
        {
            cout<<"Gratulacje remisu";
            return 1;
        }
    }
}
void wyswietl_plansze(
    int gorne_komorki[],
    int dolne_komorki[],
    int baza_lewa,
    int baza_prawa,
    const int wys_planszy,
    const int komorki_w_rzedzie,
    const int wys_komorki,
    const int szer_komorki,
    const int wys_bazy,
    const int szer_bazy)
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
            if(wys_komorki>y)       {rysuj_fragment(wys_komorki,szer_komorki,y,gorne_komorki[i]);}
            // jezeli poza wysokoscia gornych komorek,to liczba brana z listy dolnych komorek
            else{rysuj_fragment(wys_komorki,szer_komorki,y,dolne_komorki[i]);}
            // po kazdej komorce robi ' '
            cout<<' ';
        }
        // rysowanie bazy po prawej stronie
        if(y>=(wys_planszy-wys_bazy)/2 and y<=wys_planszy-1-(wys_planszy-wys_bazy)/2)
        {
            // rysuje linie bazy,jezeli w odpowiednich polach,a podaje funkcji Y mniejszy o tyle, od ktorej zaczyna linijki(jezeli wyswietla od 2,to podaje Y=0) 
            rysuj_fragment(wys_bazy,szer_bazy,y-(wys_planszy-wys_bazy)/2,baza_lewa);
            cout<<' ';
        }
        cout<<endl;
    }
        cout<<"                  A           B           C           D           E           F"<<endl;
}


int main()
{
    const int wys_planszy=12;
    const int wys_komorki=6;
    const int szer_komorki=11;
    const int wys_bazy=8;
    const int szer_bazy=12;
    const int komorki_w_rzedzie=6;
    int gorne_komorki[komorki_w_rzedzie]={6,6,6,6,6,6};
    int dolne_komorki[komorki_w_rzedzie]={6,6,6,6,6,6};
    int baza_lewa=0;
    int baza_prawa=0;
    unsigned int Tura=0;
    const char Gracz_pierwszy='P';    //tu trzeba ze pierwszy gracz to dol i gra do prawej bazy
    const char Gracz_drugi='L';
    char Aktualny_gracz;
    while(Tura>=0)
    {
    wyswietl_plansze(gorne_komorki,dolne_komorki,baza_lewa,baza_prawa,wys_planszy,komorki_w_rzedzie,wys_komorki,szer_komorki,wys_bazy,szer_bazy);
    // na poczatku podzielne,przez 2,wiec pierwszy zaczyna,potem w zaleznosci czy liczba podzielna,ten gracz
    if(Tura%2==0)   {Aktualny_gracz=Gracz_pierwszy;}
    // jezeli Tura jest nieparzysta 
    else    {Aktualny_gracz=Gracz_drugi;}

    if(Aktualny_gracz=='L')
    {
        int pole=poprawna_pozycja(gorne_komorki,komorki_w_rzedzie);
        if(pole==-1)
        {
            
        }
    }
    else
    {
        int pole=poprawna_pozycja(gorne_komorki,komorki_w_rzedzie);
        cout<<pole;  
    }
    
    
    cin>>baza_prawa;
    }
}

