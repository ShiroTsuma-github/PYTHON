import math as ma

if input("Zadanie: ").upper() == "L2_F3_Z3":
    a=float(input("Podaj a:"))
    b=float(input("Podaj b:"))
    c=float(input("Podaj c:"))
    if a==0:
        if b!=0:
            odp=c/(-b)
            print(f'x = {round(odp,5)}')
        elif b==0 and c==0:
            print("Rozwiazanie ma nieskonczona liczbe rozwiazan")
        else:
            print("Równanie jest sprzeczne. Nie ma rozwiązania")
    else:
        delta=b**2-4*a*c
        if delta==0:
            odp1=odp2=(-b)/(2*a)
        elif delta<0:
            print("Równanie nie ma rozwiązań w zbiorze liczb rzeczywistych")
            odp1=None
        else:
            odp1=((-b)-ma.sqrt(delta))/2*a
            odp2=((-b)+ma.sqrt(delta))/2*a
        if odp1 != None:
            print(f'x1 = {round(odp1,5)} , x2 = {round(odp2,5)}')
            