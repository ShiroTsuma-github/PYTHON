from os import  system,name
from  time import  sleep

def clear():
	if name == 'nt':
		__=system('cls')
	else:
		print("welp")

#clear()

# ilosc=int(input("Podaj ilosc liczb ciągu Fibonacciego: \n"))
# ciag=[]
# for x in range(0,ilosc):
# 	ciag.append(x)
# 	if x>=1:
# 		ciag[x]=ciag[x-1]+ciag[x-2]

# for x in range(0,len(ciag)):
# 	print("F"+str(x)+"     "+ str(ciag[x])+"\n")

# sleep(5)
# clear()
suma=0
tablica=[0,1,0]
ilosc=100
for i in range(0,ilosc):
    if i==0:
        pass
    else:
    	tablica[1]=tablica[0]
    tablica[0]=tablica[2]
    tablica[2]=tablica[0]+tablica[1]
    suma+=tablica[2]
    print(f'Poz:[{i}]:    {tablica[2]}')

print('\n\n',suma/1000)