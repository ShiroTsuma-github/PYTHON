class Zadania():
    def ad1():
        print( "Jestem Super")
    def ad2():
        wyr=str(input("Podaj wyraz: "))
        print( "Hello "+wyr)
    def ad3():
        goscie=int(input("Podaj liczbę gości: "))
        cukierki=int(input("Podaj liczbę cukierków: "))
        print( f"Dla Justyny zostaną {cukierki%goscie} cukierki")
    def ad4():
        print( 20*'*')
    def ad5():
        liczba=str(input("Podaj liczbę: "))
        print( len(liczba))
    def ad6():
        liczba=input("Podaj liczbę: ")
        if liczba.isdigit():
            print( int(liczba)*10)
        else:
            print( "To nie jest poprawna liczba")
    def ad7():
        wyraz=str(input("Podaj wyraz: "))
        print( wyraz[0])
    def ad8():
        from random import randint
        print( randint(1,6))
    def ad9():
        wiek=int(input("Podaj wiek: "))
        if 13<=wiek<=17:
            print( "Jest nastolatkiem" )
    def ad10():
        from datetime import datetime
        now=datetime.now()
        now_hour=now.strftime("%H")
        if now_hour=='9' or now_hour=='12':
            print("Wypij kawę")   
    def ad11():
        for i in range(6):
            print(i*'*')
    def ad12():
        wyraz=str(input("Podaj wyraz: "))
        if 'kot' in wyraz:
            print(True)
        else:
            print(False)
    def ad13():
        wyraz=str(input("Podaj wyraz: "))
        print(wyraz.lower())
    def ad14():
        wyraz=str(input("Podaj wyraz: "))
        if wyraz=='Akademia':
            print(True)
        else:
            print(False)
    def ad15():
        print("1 3 5 ? 9\n2 4 6 ? 10")
        liczby=input("Podaj liczby: ").split()

        if liczby[0] =="7" and liczby[1] =="8":
            print("Zgadłeś")
        else:
            print("Spróbuj ponownie")
    def ad16():
        liczby=input("Podaj liczby: ").split()
        print(max(liczby))
    def ad17():
        from random import randint
        znajomi = [] 
        while True:
            znajomy=input("Podaj znajomego: ")
            if znajomy=='':
                break
            else:
                znajomi.append(znajomy)
        print(znajomi[randint(0,len(znajomi)-1)])  
    def ad18():
        liczby=input("Podaj liczby: ").split()
        print((int(liczby[0])+int(liczby[1]))/2)
    def ad19():
        import turtle
        screen=turtle.getscreen()
        render=turtle.Turtle()
        render.speed(5)
        render.pensize(10)
        for i in range(4):
            render.forward(100)
            render.left(90)
    def ad20():
        import turtle
        screen=turtle.getscreen()
        render=turtle.Turtle()
        render.pensize(20)
        render.penup()
        render.right(50)
        render.forward(150)
        render.pendown()
        render.color('blue')
        render.circle(50)
        render.penup()
        render.right(130)
        render.forward(120)
        render.left(130)
        render.pendown()
        render.color('purple')
        render.circle(50)
        render.penup()
        render.left(130)
        render.forward(90)
        render.pendown()
        render.color('green')
        render.circle(50)
        render.penup()
        render.right(110)
        render.forward(80)
        render.pendown()
        render.color('yellow')
        render.circle(50)
        render.penup()
        render.left(25)
        render.forward(150)
        render.pendown()
        render.color('red')
        render.circle(50)
    def ad21():
        import pyautogui
        from time import sleep
        from random import randint
        a_m=10
        name='Kasia'
        print("Zaraz zacznie. Kliknij pole do wprowadzania tekstu")
        sleep(2)
        while a_m>0:
            pyautogui.typewrite(f'{name} ta wiadomość jest zautomatyzowana nr.{a_m}')
            sleep(0.2)
            pyautogui.typewrite('\n')
            sleep(0.2)
            a_m-=1
    def ad22():
        from random import randint
        print(randint(1,100))
    def ad23():
        import time
        from selenium import webdriver
        Timer=3
        link='https://www.youtube.com/watch?v=QMUHZYUZ3y4'
        views=20
        driver=webdriver.Firefox()
        driver.get(link)
        for i in range(views):
            print(f'Progress {(i/views)*100}%')
            time.sleep(Timer)
            driver.refresh()
    def ad24():
        wyraz=str(input("Podaj wyraz: "))
        if wyraz[0]=='A':
            print(True)
        else:
            print(False)
    def ad25():
        wyraz1=str(input("Podaj wyraz 1: "))
        wyraz2=str(input("Podaj wyraz 2: "))
        if wyraz1 == wyraz2:
            print(True)
        else:
            print(False)
    def ad26():
        wyraz=str(input("Podaj wyraz: "))
        if wyraz== wyraz[::-1]:
            print('Tak')
        else:
            print('Nie')        
    def ad27():
        liczby=input("Podaj liczby: ").split()
        print(int(liczby[0])**int(liczby[1]))
    def ad28():
        wyraz=str(input("Podaj wyraz: "))
        print(wyraz[1])
    def ad29():
        wyraz=str(input("Podaj wyraz: "))
        print(wyraz.replace('*',""))
    def ad30():
        wyraz=str(input("Podaj wyraz: "))
        if wyraz.endswith('tka'):
            print(True)
        else:
            print(False)
Zadania.ad20()