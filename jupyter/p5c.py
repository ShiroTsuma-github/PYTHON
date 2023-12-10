# -*- coding: utf-8 -*-
"""
Created on Mon May 15 10:41:36 2023

@author: Studia
"""

import numpy as np
import matplotlib.pyplot as plt


def getPerceptronAns(values: list) -> int:
    S = sum([values[j] * W[j] for j in range(3)])
    Sig = 0
    if S > 0:
        Sig = 1
    else:
        Sig = -1
    return (Sig, S)



A = [
     [1, -1, -1, -1, -1],
     [1, -1, -1, 1, -1],
     [1, -1, 1, -1, -1],
     [1, -1, 1, 1, -1],
     [1, 1, -1, -1, -1],
     [1, 1, -1, 1, 1],
     [1, 1, 1, -1, -1],
     [1, 1, 1, 1, -1]]

lenX = len(A[0])
lenY = len(A)
"""
for i in range(lenX):
    if A[i][lenX - 1] == 1:
        plt.plot(A[i][1], A[i][2], 'ko:')
    else:
        plt.plot(A[i][1], A[i][2], 'r+:')
plt.axis([-2, 2, -2, 2])
"""
#---- ustalenie poczatkowych wartosci wag
W=[0 for _ in range(lenX - 1)]
#---- proces trenowania
print(W)


Zmiana = 1
while (Zmiana == 1):
    Zmiana = 0
    for i in range(lenY):
        Sig, S = getPerceptronAns(A[i])
        if (Sig > 0 and A[i][lenX - 1] == 1) or (Sig < 0 and A[i][lenX - 1] == -1):
            W = W
        else:
            Zmiana = 1
            if S != 0:
                for j in range(len(W)):
                    W[j] = W[j] + 0.5 * (A[i][lenX - 1] - Sig) * A[i][j]
        if S == 0:
            Zmiana = 1
            for j in range(len(W)):
                W[j] = W[j] + A[i][lenX - 1] * A[i][j]
        print(W)
    break
#---- wykreslenie otrzymanej linii podzialu
"""
k = -2;
XX = np.zeros((401))
YY = np.zeros((401))
for i in range(0, 401):
    XX[i] = k
    YY[i] = -( (W[1] / W[2]) * k) - (W[0] * 1) / W[2];
    k += 0.01;
plt.plot(XX, YY)
"""

test = input("Podaj wartosci wejsciowe [Example: -1 1]: ")
test = test.split()
test.insert(0, 1)
test = [int(i) for i in test]
print(getPerceptronAns(test)[0])