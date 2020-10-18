#=======================GENERALNIE NIE ODPALAĆ,BO NIE CHCIAŁO MI SIĘ WSZYSTKO KOMENTOWAĆ LUB INDENTOWAĆ====================

try:
#STRING FUNCTIONS

	print(", ".join(["spam", "eggs", "ham"])) #laczy liste stringow z uzyciem innej jako separatora
	#prints "spam, eggs, ham"

	print("Hello ME".replace("ME", "world")) #zamienia wybrany substring na inny
	#prints "Hello world"

	print("This is a sentence.".startswith("This")) #sprawdza czy string zaczyna z wybranym substringiem
	# prints "True"

	print("This is a sentence.".endswith("sentence.")) #Sprawdza czy string konczy z wybranym substringiem
	# prints "True"

	print("This is a sentence.".upper()) #wszystko CAPS LOCK
	# prints "THIS IS A SENTENCE."

	print("AN ALL CAPS SENTENCE".lower()) #wszystko malymi literami	
	#prints "an all caps sentence"

	print("spam, eggs, ham".split(", ")) #oddzielenie wyrazow wybranym stringiem
	#prints "['spam', 'eggs', 'ham']"

	#FORMATING STRING
	nums = [4, 5, 6]
	msg = "Numbers: {0} {1} {2}". format(nums[0], nums[1], nums[2]) 
	#formatuje wartosci z nums[0,1,2] poprzez przechowanie na czas operacji w .format() i potem umieszczeniu w nitce w kolejnosci okreslonej przez {}
	print(msg)
	#Numbers: 4 5 6



#NUMERIC FUNCTIONS

	print(min(1, 2, 3, 4, 0, 2, 1)) #wyciaga najmniejsza liczbe
	#0
	print(max([1, 4, 9, 2, 5, 6, 8])) #wyciaga najwieksza liczbe
	#9
	print(abs(-99)) #odleglosc od zera
	#99
	print(abs(42)) #odleglosc od zera
	#42
	print(sum([1, 2, 3, 4, 5])) #wyswietla sume liczb
	#15
	print(round(4.853444,2)) #zaokragla do liczby miejsc po przecinku podanej
	#4.85


#(MI ZNANE(xD))TYPY STRUKTUR

	nums = [55, 44, 33, 22, 11] #zwyczajna tabela dajaca mozliwosc zapisu,zmiany i odczytu wartosci
	print(nums[2]) 
	#daje 33

	ages = {"Dave": 24, "Mary": 42, "John": 58} #slownik w ktorym przypisujemy wartosci do danych. Mozna dodawac,zmieniac i zapisywac wartosci
	print(ages["Dave"])
	#daje 24
	ages["Dave"]=13 
	#zmienia dane,bo juz wystepuja
	ages["Mike"]=5 
	#dodaje wpis, bo nie bylo
	print("Mike" in ages)
	#True
	print(24 in ages)
	#False (sprawdza po kluczu )
	print(ages.get("Lahn"))
	#None (w ages nie ma Lahn,a nie wprowadzono wiadomosci zastepczej)
	print(ages.get("Lahn","Not in dictionary"))
	#Not in dictionary (w ages nie ma Lahn,wiec wyswietla wiadomosc zastepcza )
	
	bad_dict = { #Tylko wartosci niezmienne moga byc kluczami
  		[1, 2, 3]: "one two three", 
	}
	#TypeError: unhashable type: 'list'

	primary = {
  		"red": [255, 0, 0], 
  		"green": [0, 255, 0], 
  		"blue": [0, 0, 255], 
	}
	print(primary["red"])
	#daje [255,0,0]

	words = ("spam", "eggs", "sausages",) # podobna do listy,ale bez mozliwosci edycji,ani wprowadzania danych
	print(words[0]) 
	#spam (wyswietla tak samo jak lista)

	a = "{x}, {y}".format(x=5, y=12) #pozwala na przypisywanie zmiennych
	print(a)
	#5, 12

#FUNKCJE OGOLNE DLA LIST

	if all([i > 5 for i in nums]):  #jezeli wszystkie wyrazy listy spelniaja warunek oddaje "TRUE"/"FALSE"
	   print("All larger than 5")

	if any([i % 2 == 0 for i in nums]): #jezeli jakikolwiek wyraz listy spenia warunek oddaje "TRUE"/"FALSE"
	   print("At least one is even")

	for v in enumerate(nums): #przechodzi przez wszystkie obiekty w liscie i rownoczesnie przechowuje ich pozycje
	   print(v)

	from itertools import product, permutations

	letters = ('A','B')
	print(list(permutations(letters)))	#wyswietla wszystkie kombinacje obiektów
	print(list(product(letters, range(2)))) #powtarza obiekty do range() i przypisuje w liscie
	

	None == None #None okresla brak wartosci. W przemianie na bool variable daje False. Funkcja ktora nie zwraca nic po odwolaniu daje None
	#True
	None
	print(None)
	#None
 
	a = ('John', 'Charles', 'Mike')
	b = ('Jenny', 'Christy', 'Monica')
	x = zip(a, b)  #funkcja zip() tworzy tuple w ktorej obiekt i jest rowny obiektom i z kazdego z argumentow
	#use the tuple() function to display a readable version of the result:
	print(tuple(x))

	#LIST SLICES pozwalaja dokladniej wprowadzac jaki zakres danych chcemy pozyskac
	squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
	print(squares[2:6]) #Podany zakres wyrazow to 2-5
	#[4, 9, 16, 25]
	print(squares[3:8]) #Podany zakres wyrazow to 3-7
	#[9, 16, 25, 36, 49]
	print(squares[0:1]) #Podany zakres wyrazow to wyraz 0
	#[0]
	print(squares[:7]) #Podany zakres wyrazow to 0-6
	#[0, 1, 4, 9, 16, 25, 36]
	print(squares[7:]) #Podany zakres wyrazow to 7-(koniec listy)
	#[49, 64, 81]
	print(squares[::2]) #Przeskakuje o 2 od 0-(koniec listy)
	#[0, 4, 16, 36, 64]
	print(squares[2:8:3]) # przeskakuje o 3 od 2-7
	#[4, 25]
	print(squares[1:-1]) # zakres to od 1 do (koniec listy -1) * przy podaniu [-] porusza od konca tabeli

	#LIST COMPREHENSIONS pozwalaja tworzyc szybko listy ktorych zawartosc obeys(na polski znaczenie nie pasuje) prostą regule
	cubes = [i**3 for i in range(5)] #liczby w przedziale 0-4 do potegi 3
	print(cubes)
	#[0, 1, 8, 27, 64]
	evens=[i**2 for i in range(10) if i**2 % 2 == 0] #liczby w przedziale 0-9 do kwadratu,ktore sa parzyste 
	print(evens) 
	#[0, 4, 16, 36, 64]

	#LAMBDA ETC
	def my_func(f, arg):
  		return f(arg)

	my_func(lambda x: 2*x*x, 5) #uzywa sie do operacji na jednej linijce,gdy nie chcemy wczesniej okreslac zmiennej

	nums = [11, 22, 33, 44, 55]

	result = list(map(lambda x: x+5, nums)) #funkcja map bierze obiekty z listy i dla kazdego z nich uzywa funkcje
	print(result)
	#[16, 27, 38, 49, 60]
	def add_five(x):
    	 return x+5

	nums = [11, 22, 33, 44, 55] #to samo
	result = list(map(add_five, nums))
	print(result)
 	#[16, 27, 38, 49, 60]
  
  
	nums=[11,22,33,44]
	res = list(filter(lambda x: x%2==0, nums)) #usuwa wszystkie obiekty nie spelniajace warunku
	print(res)
	#[22, 44]
 
	#YIELD I GENERATORY
	def countdown():
  		i=5
  		while i > 0:
    		 yield i #zwraca wartosc z funkcji generatora
    		 i -= 1
    
	for i in countdown():
  		print(i)

	"""

	Tak sie komentuje wieksza ilosc linijek
	
	"""
 # funkcje rekursywne
	def silnia(x):
		if x==1:
			return 1
		else:
			return x*silnia(x-1)
	print(silnia(5))
#operacje na plikach

	myfile=open("myfile.txt","r") 
	#metody: r-odczyt w-zapis od zera a-dodawanie do koncowki pliku b-binarnie [+]-jezeli pliku nie ma utworzyc rw+- odczyt,zapis,a jezeli brak utwórz

	content=myfile.read() 
	#przy print(file.read(16)) podaje 16 bajt,czyli 16 litere
	
	content2=myfile.readlines() 
	# przy podaniu print(file.readlines(3)) wydrukuje 3 linijke
	
	for line in myfile: #przechodzi po wszystkich linijkach
    	 print(line)
	myfile.write("This has been written to a file")
	#This has been written to a file

	msg = "Hello world!"
	amount_written = myfile.write(msg)
	print(amount_written) 
	#Wyswietli ilosc bajtow zapisanych do pliku

	myfile.close() 
	#na koniec trzeba zawsze zamknac plik
except:
	pass

try: #metoda ta zapobiega zapomnieciu o zamknieciu pliku przez nas i zapobiega błędom
    f = open("filename.txt")
    print(f.read())
except FileNotFoundError: #w przypdaku braku pliku lub folderu nie zamyka od razu programu
    print("Welp")
    f = open(__file__, "r") #open itself
finally:
    f.close()
with open(__file__) as f:
   	print(f.read())
#szybsza metoda,ale nie pozwala w porownaniu z [try:] w korzystaniu z danych w innym bloku danych,oraz po zakonczeniu od razu zamyka plik

import _thread
from time import sleep,ctime
# Define a function for the thread
def print_time(thread,delay):
   count = 0
   while count < 5:
      sleep(delay)
      count += 1
      print (count)
								#multithreading funkcja odwolywac podajac nazwe threadu i opoznienie. Model napisany
# Create two threads as follows
try:
    """
   _thread.start_new_thread(print_time,("Thread-1",1))
   _thread.start_new_thread(print_time,("Thread-2",1))
   _thread.start_new_thread(print_time,("Thread-3",1))
   """
except:
   raise

while 1:
   pass

# klasy i wszystko (atm mi wiadome ) o nich
class Wolf: #superklasa,z ktorej bedą przejmować
    legs=4 #zmienna dzielona dla całej klasy
  def __init__(self, name, color): 		#metoda deklarująca zmienne dla instancji klasy
      self.name = name 
      self.color = color

  def bark(self): #metoda dla klasy 
    print("Grr...")

class Dog(Wolf): #subklasa dziedzicząca od klasy Wolf
  def bark(self): #override metody z superklasy
    print("Woof")
        
husky = Dog("Max", "grey") #zapisywanie instancji dla zmiennej
husky.bark() #odwołanie do metody klasy

class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y) #"magiczna metoda", specjalna metoda zastępująca 
# podstawową funkcjonalność i pozwalająca na wcześniej niemożliwe operacje (jak w tym przypadku [+]dla takiego obiektu)

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
#odp: 8 16
try: #specjalne metody zastępujące operacje
	__sub__ for -
	__mul__ for *
	__truediv__ for /
	__floordiv__ for //
	__mod__ for %
	__pow__ for **
	__and__ for &
	__xor__ for ^
	__or__ for |
except:
    pass

class SpecialString:
  def __init__(self, cont):
    self.cont = cont

  def __truediv__(self, other): #other odnosi się do innej instancji klasy
    line = "=" * len(other.cont) #w tym przypadku bierze 2 obiekt jako długość [=],wiec nie jest uniwersalne
    return "\n".join([self.cont, line, other.cont])

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

""" wynik
spam
============
Hello world!
"""






