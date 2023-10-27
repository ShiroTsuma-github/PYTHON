import numpy as np
import matplotlib.pyplot as plt

A=np.ones((4,4))
A[0,1]=-1; A[0,2]=-1; A[0,3]=-1;
A[1,1]=-1; A[1,3]=-1;
A[2,2]=-1; A[2,3]=-1;

#---- wykreslenie obszaru klasyfikacji
for i in range(0,4):
    if A[i,3]==1:
        plt.plot(A[i,1],A[i,2],'ko:')
    else:
        plt.plot(A[i,1],A[i,2],'r+:')
plt.axis([-2,2,-2,2])
#---- ustalenie poczatkowych wartosci wag
W=[0,0,0]
#---- proces trenowania
print(W)
Zmiana=1
while (Zmiana==1):
    Zmiana=0
    for i in range(0,4):
        S=A[i,0]*W[0]+A[i,1]*W[1]+A[i,2]*W[2]
        Sig=0
        if S>0:
            Sig=1
        else:
            Sig=-1
        if (Sig>0 and A[i,3]==1) or (Sig<0 and A[i,3]==-1):
            W=W
        else:
            Zmiana=1
            if S!=0:
                for j in range(0,3):
                    W[j]=W[j]+0.5*(A[i,3]-Sig)*A[i,j]
        if S==0:
            Zmiana=1
            for j in range(0,3):
                W[j]=W[j]+A[i,3]*A[i,j]
        print(W)
#---- wykreslenie otrzymanej linii podzialu
k=-2;
XX=np.zeros((401))
YY=np.zeros((401))
for i in range(0,401):
    XX[i]=k
    YY[i]=-((W[1]/W[2])*k)-(W[0]*1)/W[2];
    k=k+0.01;
plt.plot(XX,YY)