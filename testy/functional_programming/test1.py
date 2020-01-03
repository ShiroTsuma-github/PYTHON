def countdown():
    i = 5
    while i > 0:
        yield i  # zwraca wartosc z funkcji generatora
        i -= 1
for i in countdown():
    print(i)
