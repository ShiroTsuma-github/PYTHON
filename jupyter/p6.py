import numpy as np
import matplotlib.pyplot as plt
import math
A=np.zeros((4,4))
A[0,0]=1; A[0,1]=0; A[0,2]=0; A[0,3]=0
A[1,0]=1; A[1,1]=0; A[1,2]=1; A[1,3]=1
A[2,0]=1; A[2,1]=1; A[2,2]=0; A[2,3]=1
A[3,0]=1; A[3,1]=1; A[3,2]=1; A[3,3]=0
#---- wykreslenie obszaru klasyfikacji
Licz=0
IleKrokow=50000
blad = []
plt.figure(0)
for i in range(0,4):
    if A[i,3]==1:
        plt.plot(A[i,1],A[i,2],'ko:')
    else:
        plt.plot(A[i,1],A[i,2],'r+:')
plt.axis([-0.5,1.5,-0.5,1.5])
#---- utworzenie odpowiednich tablic na dane
W=np.zeros((9));S=np.zeros((3));U=np.zeros((3));F=np.zeros((3));d=np.zeros((3))
#---- losowa inicjalizacja wag poczatkowych
for i in range(0,9):
    W[i]=np.random.rand()-0.5
ro=0.2
iteracja=0
while (iteracja<IleKrokow):
    iteracja=iteracja+1
    #---- losowe wybieranie wektora trenujacego
    i=np.random.randint(4)
    #---- faza propagacji w przod - warstwa posrednia
    S[0]=W[0]*A[i,0]+W[1]*A[i,1]+W[2]*A[i,2]
    S[1]=W[3]*A[i,0]+W[4]*A[i,1]+W[5]*A[i,2]
    U[0]=1/(1+math.exp(-S[0]))
    U[1]=1/(1+math.exp(-S[1]))
    #---- faza propagacji w przod - warstwa wyjsciowa
    S[2]=W[6]*A[i,0]+W[7]*U[0]+W[8]*U[1]
    U[2]=1/(1+math.exp(-S[2]))
    #---- faza propagacji wstecz - warstwa wyjsciowa
    F[2]=U[2]*(1-U[2])
    d[2]=(A[i,3]-U[2])*F[2]
    #---- faza propagacji wstecz - warstwa posrednia
    F[0]=U[0]*(1-U[0])
    d[0]=W[7]*d[2]*F[0]
    F[1]=U[1]*(1-U[1])
    d[1]=W[8]*d[2]*F[1]
    #---- uaktualnienie wag - warstwa wyjsciowa
    W[6]=W[6]+ro*d[2]*A[i,0]
    W[7]=W[7]+ro*d[2]*U[0]
    W[8]=W[8]+ro*d[2]*U[1]
    
    #---- uaktualnienie wag - warstwa posrednia
    W[0]=W[0]+ro*d[0]*A[i,0]
    W[1]=W[1]+ro*d[0]*A[i,1]
    W[2]=W[2]+ro*d[0]*A[i,2]
    W[3]=W[3]+ro*d[1]*A[i,0]
    W[4]=W[4]+ro*d[1]*A[i,1]
    W[5]=W[5]+ro*d[1]*A[i,2]
    if iteracja % 100 == 0:
        blad.append(A[i, 3] - U[2])
#---- wykreslenie otrzymanej linii podzialu (neuron 1)
XX=np.zeros((401))
YY=np.zeros((401))
k=0
for i in np.arange(-2,2.01,0.01):
    XX[k]=i
    YY[k]=-((W[1]/W[2])*i)-(W[0]*1)/W[2]
    k=k+1
plt.plot(XX,YY)
#---- wykreslenie otrzymanej linii podzialu (neuron 2)
k=0
for i in np.arange(-2,2.01,0.01):
    XX[k]=i
    YY[k]=-((W[4]/W[5])*i)-(W[3]*1)/W[5]
    k=k+1
plt.plot(XX,YY)
plt.axis([-0.5,1.5,-0.5,1.5])


poz = 4
while True:
    A = np.vstack([A, [1, 0, 0, 0]])
    liczba = input("Podaj wartosc U1, U2 np. [2 0]: ")
    liczba = liczba.split()
    if liczba[0] == 'x' or liczba[0] == 'X' or len(liczba) != 2:
        break
    liczba = [float(l) for l in liczba]
    print(liczba)
    A[poz, 1] = liczba[0]
    A[poz, 2] = liczba[1]
    
    S[0]=W[0]*A[poz,0]+W[1]*A[poz,1]+W[2]*A[poz,2]
    S[1]=W[3]*A[poz,0]+W[4]*A[poz,1]+W[5]*A[poz,2]
    U[0]=1/(1+math.exp(-S[0]))
    U[1]=1/(1+math.exp(-S[1]))
    #---- faza propagacji w przod - warstwa wyjsciowa
    S[2]=W[6]*A[poz,0]+W[7]*U[0]+W[8]*U[1]
    U[2]=1/(1+math.exp(-S[2]))
    print(U[2])
    
    # plt.scatter(A[poz,1],A[poz,2],'ko:' if round(U[2]) == 1 else 'r+:')
    A[poz, 3] = U[2]
    plt.pause(0.001)
    poz += 1
    

plt.figure(3)
plt.plot(range(len(blad)), blad)
    # plt.plot(A[i,1],A[i,2],'r+:')