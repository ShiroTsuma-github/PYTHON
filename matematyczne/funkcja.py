from math import sqrt
    
class Zadania_z_infy:
    def zad_l2_f3_z3():
        a=float(input("Podaj a:"))
        b=float(input("Podaj b:"))
        c=float(input("Podaj c:"))
        if a==0:
            if b!=0:
                odp=c/(-b)
                return(f'x = {round(odp,5)}')
            elif b==0 and c==0:
                return("Rozwiazanie ma nieskonczona liczbe rozwiazan")
            else:
                return("Równanie jest sprzeczne. Nie ma rozwiązania")
        else:
            delta=b**2-4*a*c
            if delta==0:
                odp=(-b)/(2*a)
                return(f'x = {round(odp,5)}')
            elif delta<0:
                return("Równanie nie ma rozwiązań w zbiorze liczb rzeczywistych")
                odp1=None
            else:
                odp1=((-b)-sqrt(delta))/2*a
                odp2=((-b)+sqrt(delta))/2*a
            if odp1 != None:
                return(f'x1 = {round(odp1,5)} , x2 = {round(odp2,5)}')
    def zad_l2_f3_z2():
        x=float(input("Podaj x: "))
        y=float(input("Podaj y: "))
        odleglosc=abs(x)**2+abs(y)**2
        odleglosc=sqrt(odleglosc)
        if odleglosc >2:
            return "Punkt nie należy do koła"
        else:
            wynik="Punkt należy do koła. "
            if x>0 and y>0:
                wynik+="Znajduje się w 1 ćwiartce"
            elif x<0:
                wynik+="Znajduje się w 2 ćwiartce"
            return wynik
print(getattr(Zadania_z_infy,f'zad_{input("Zadanie: ").lower()}')())

