from os import  system,name,
from  time import  sleep

def clear():
	if name == 'nt':
		__=system('cls')
	else:
		print("welp")

#clear()

ilosc=int(input("Podaj ilosc liczb ciągu Fibonacciego: \n"))
ciag=[]
for x in range(0,ilosc):
	ciag.append(x)
	if x>=1:
		ciag[x]=ciag[x-1]+ciag[x-2]

for x in range(0,len(ciag)):
	print("F"+str(x)+"     "+ str(ciag[x])+"\n")

sleep(5)
clear()