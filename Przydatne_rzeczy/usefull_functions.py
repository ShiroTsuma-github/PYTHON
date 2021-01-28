


print("Mike" in ages)
#True
print(24 in ages)
#False (sprawdza po kluczu )
print(ages.get("Lahn"))
#None (w ages nie ma Lahn,a nie wprowadzono wiadomosci zastepczej)
print(ages.get("Lahn","Not in dictionary"))
#Not in dictionary (w ages nie ma Lahn,wiec wyswietla wiadomosc zastepcza )
try:
	bad_dict = { #Tylko wartosci niezmienne moga byc kluczami
		[1, 2, 3]: "one two three", 
	}
		#TypeError: unhashable type: 'list'
except TypeError:
    pass

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


#TUPLE UNPACKING
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]	#zmienna *przejmuje pozostale argumenty
print(a)
print(b)
print(c)
print(d)
#1
#2
#[3,4,5,6,7,8]
#9

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

#funkcje z *args

def function(named_arg, *args):	#*args/*nasza_nazwa pozwala podac funkcji wiecej argumentow i sa one wtedy przechowywane w tupli
	print(named_arg)
	print(args)

function(1, 2, 3, 4, 5)
#1
#(2, 3, 4, 5)

def my_func(x, y=7, *args, **kwargs):	#**kwargs/**nasza_nazwa pozwala nam obslugiwac niezadeklarowane zmienne z nazwami
   print(kwargs)	#zapisywane w dictionary z nazwa przekazywana i jej wartoscia

my_func(2, 3, 4, 5, 6, a=7, b=8)
#{'a': 7, 'b': 8}
 
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
try:
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
"""
try: #metoda ta zapobiega zapomnieciu o zamknieciu pliku przez nas i zapobiega błędom
	f = open("filename.txt")
	print(f.read())
except FileNotFoundError: #w przypdaku braku pliku lub folderu nie zamyka od razu programu
	print("Welp")
 	try:
	    f = open(__file__, "r") #open itself
     except:
      pass
finally:
	f.close()
with open(__file__) as f:
	print(f.read())
"""
#szybsza metoda,ale nie pozwala w porownaniu z [try:] w korzystaniu z danych w innym bloku danych,oraz po zakonczeniu od razu zamyka plik

import re
from time import ctime, sleep

import _thread


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
"""
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
"""
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
# =====================REGEX============================================
# match dziala tylko dla poczatku stringa i jednoliniowy musi byc. Lepiej uzywac re.search lub re.findall
pattern = r"spam"

if re.match(pattern, "spamspamspam"):
   print("Match")
else:
   print("No match")
# Match
pattern = r"spam"

if re.match(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")

if re.search(pattern, "eggspamsausagespam"):
   print("Match")
else:
   print("No match")
    
print(re.findall(pattern, "eggspamsausagespam"))
# No match
# Match
# ['spam','spam']

# wyswietlanie poczatku i koncu wyrazu
pattern = r"pam"
match = re.search(pattern, "eggspamsausagepam")
if match:
	print(match.group())	#match.group zwraca nam wartosc zapytania,jezeli prawdziwe. przydatne to przy [A-Z][A-Z][0-9] (zwroci nam wyraz pasujacy)
	print(match.start())
	print(match.end())
	print(match.span())
# pam
# 4
# 7
# (4,7)

# zamiana wyrazu w tekscie na inny
stra = "My name is David. Hi David."
pattern = r"David"
newstr = re.sub(pattern, "Amy", stra)
print(newstr)
# My name is Amy. Hi Amy.

# Specjalne znaki Regex

#		.
# dziala w zapytaniu jak kazdy inny znak(dopasuje wszystko z gr.y)(musi byc ta sama dlugosc)
pattern=r"gr.y"
if re.match(pattern, "grey"):
   print("Match 1")
if re.match(pattern, "blue"):
   print("Match 3")
#  Match 1
# 	* pattern "...." dopasuje wszystkie 4 literowe rzeczy

	# ^-[oznacza ze zaczyna znakiem]		$-[oznacza ze konczy znakiem]		#uzyteczne glownie w re.search
pattern = r"^s(.)+y$"	#oznacza,ze zaczyna od s,w srodku ma znaki i konczy y
if re.search(pattern,'sunless day'):
    print('Dziala')

# Klasy znakow wpisywane sa w "[abcdef...0123...]" jezeli zawiera okreslony symbol,to cos robi
pattern = r"[aeiou]"
if re.search(pattern, "grey"):
   print("Match 1")
if re.search(pattern, "rhythm myths"):
   print("Match 3")
   
# Match 1

#  [abc][def]   okresla,ze w zdaniu po a/b/c musi nastapic ktorys symbol z d/e/f	np.add
#  [a-z] okresla wszystkie male litery
#  [A-Z] okresla wszystkie duze
#  [0-9] okresla wszystkie numery
#  [A-Za-z0-9] okresla wszystkie duze,male litery i liczby
# {3} okresla ilosc wystapien	np.[A-Z]{3} oznacza- 3*duze liczby pod rzad musza byc
# {1-3} okresla,ze moze wystapic od 1 do 3 razy
# {1,} oznacza od 1 do nieskonczonosci
#  [^A-Z] dopasowuje wszystkie litery,ktore nie sa duze (^ w []--[^] odwraca zapytanie)
# spacje nie dopasowuja do a-z lub A-Z
# 		* 		okresla,ze musi sie potworzyc 0 lub wiecej razy
pattern = r"123([0-9])*456"
# dopasowuje rzeczy posiadajace 123- wewnatrz posiadajece 0 lub wiecej [0-9] i potem 456
# 		+ 		okresla,ze musi sie powtorzyc 1 lub wiecej razy
pattern=r"123([0-9])+456"
# 		-		okresla,ze musi sie powtorzyc 0 lub 1 raz
pattern=r"ice(-)?cream"
# 	pasuje ice-cream	icecream

#	dla dopasowania do operatorow wyrazow mozna uzywac () co pozwala nam jako argumenty podawac (wyraz)*+? 
pattern=r'([^aeiou][aeiou][^aeiou])+'	#okresla 1 lub wiecej wystapien (!aeiou,aeiou,!aeiou)...

pattern = r"a(bc)(de)(f(g)h)i"
# podziela to zapytanie na grupy ('bc', 'de', 'fgh', 'g')
# pozwala na:
match = re.match(pattern, "abcdefghijklmnop")
if match:
   print(match.group())		#calosc zapytania
   print(match.group(0))	#to samo co group()-wyswietla cale
   print(match.group(1))	#wyswietla dla (bc)
   print(match.group(2))	#wyswietla dla (de)
   print(match.groups())	#wyswietla wszystkie grupy
# abcdefghi		
# abcdefghi
# bc
# de
# ('bc', 'de', 'fgh', 'g')

#  w przypadku 1(23)(4(56)78)9(0)	numeracja grup wchodzi wewnatrz grupy (nesting),wiec grupa 3,to 56

# 	2 przydatne typy grup to grupy nazywane i nieuwzgledniane-(NAZWA WLASNA)
pattern = r"(?P<first>abc)(?:def)(ghi)"
# typ pierwszy (?P<nazwa>) pozwala wywolac,przez group("nazwa")
# typ drugi (?:cos) powoduje,ze nie sa indeksowane w groups i nie pozwala wywolac jej numerem
match = re.match(pattern, "abcdefghi")
if match:
   print(match.group("first"))
   print(match.groups())
   
# 		|		oznacza 'or' przypasowuje dla 1 lub drugiej opcji
pattern = r"gr(a|e)y" # a lub e

#==============specjalne sekwencje oznaczane są \ i potem znakiem========================
# 	jedna z przydatnych opcji jest \[liczba]	(w przedziale 1-99)
# w tym przypadku powtarza pierwsze zapytanie i porownuje czy pasuje
pattern = r"(.+) \1"	#oznacza wykonanie dla grupy podanego numeru

match = re.match(pattern, "word word")
if match:	#jest prawdziwe, bo wyraz nastepny jest identyczny,co poprzedni
   print ("Match 1")

match = re.match(pattern, "?! ?!")
if match:	#jest prawdziwe, bo wyraz nastepny jest identyczny,co poprzedni
   print ("Match 2")    

match = re.match(pattern, "abc cde")
if match:	#jest nieprawdziwe, bo ciagi sie roznia
   print ("Match 3")
   
pattern = r"(.+) (.+) (.+) \1" #okresla,ze chce 4 wyrazy, z czego 1 i 4 sa identyczne
#  W ZALEZNOSCI OD LICZBY \1|2|3 bedzie oczekiwalo,ze te wyrazy beda identyczne
# \d-oznacza liczby
# \s-oznacza whitespace	*wiecej opcji dla whitespace
	# \t = Matches a tab \u0009.11
	# \n = 	Matches a new line \u000A.
	# \r = Matches a carriage return \u000D.
	# \f = Matches a form feed \u000C.1
	# \v = 	Matches a vertical tab \u000B.
# \w-oznacza znaki
# przeciwienstwami sa duze znaki \D \S \W 
pattern = r"(\D+\d)"
match = re.match(pattern, "Hi 999!")	#pasuje,bo wiecej niz 1 znak po czym liczba
match = re.match(pattern, "1, 23, 456!")	#nie pasuje,poniewaz zaczyna liczbami i konczy liczbami

# Dodatkowe specjalne sekwencje
# \A-wyraz to poczatek stringa,wiec nic nie moze przed nim wystapic 
# \Z-wyraz to koniec stringa,wiec nic nie moze po nim wystapic
# \b-oznacza,ze musi byc oddzielone symbolem np.[ .,/<>*] itd...	(nie moga byc liczby i litery)
pattern = r"\b(cat)\b"	#oznacza,ze musi byc symbol cat symbol

# SPAM! == \AS...\b.\Z

str = "Please contact info@sololearn.com for assistance"	#wyciaganie adresu email z linijki
pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w]+)"


# https://pypi.org/project/progressbar2/
from time import sleep
from progressbar import progressbar,Bar,ProgressBar
"""
progressbar at botom with possibility of printing things
"""
for i in progressbar(range(100), redirect_stdout=True):
    print('Some text', i)
    sleep(0.1)

"""
in place progressbar
"""
with ProgressBar(max_value=10) as bar:
    for i in range(10):
        sleep(0.1)
        bar.update(i)



from os import system,name,path
# FILE AND SITE LINKS
folder_path=path.dirname(__file__)
folder=path.relpath(folder_path)
file_link=f'{folder}\\linki.txt'


a,*b,c=3,2,4,5,2,5
# GET ONLY X OBJECT OF LIST OF LISTS
DATA=[[6.0, 0.5], [6.1, 1.0], [6.2, 1.5], [6.3, 2.0], [6.4, 2.5], [6.5, 3.0], [6.6, 3.5], [6.7, 4.0], [6.8, 4.5]]
WYN1=[item[0] for item in DATA]

l = [[6.0, 0.5], [6.1, 1.0], [6.2, 1.5], [6.3, 2.0], [6.4, 2.5], [6.5, 3.0], [6.6, 3.5], [6.7, 4.0], [6.8, 4.5]]

a,b = map(list,zip(*l))
print(a,b)


