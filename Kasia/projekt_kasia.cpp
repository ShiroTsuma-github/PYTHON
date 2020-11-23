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
    wyswietl_plansze(gorne_komorki,dolne_komorki,baza_lewa,baza_prawa,wys_planszy,komorki_w_rzedzie,wys_komorki,szer_komorki,wys_bazy,szer_bazy);
}
