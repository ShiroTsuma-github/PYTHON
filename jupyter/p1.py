import numpy as np
import matplotlib.pyplot as plt
from math import exp

def triangle(x, a, x0, b):
    try:
        if x > a and x <= x0:
            return (x - a) / (x0 - a)
        elif x >= x0 and x <= b:
            return (b - x) / (b - x0)
        return 0
    except ZeroDivisionError:
        return 0

def trap(x, a, x1, x2, b):
    try:
        if x >= a and x <= x1:
            return (x - a) / (x1 - a)
        elif x >= x1 and x <= x2:
            return 1
        elif x >= x2 and x <= b:
            return (b - x) / (b - x2)
        return 0
    except ZeroDivisionError:
        return 1

def singleton(x, x0):
    return 1 if x == x0 else 0

def gauss(x, x0, sigma):
    return exp(-(1/2) * ( (x - x0) / sigma)**2 )

dyskretyzacja = 1
wartosci = 181
l = np.zeros((int(wartosci/dyskretyzacja),5))
for i in range(0,int(wartosci/dyskretyzacja)):
    l[i,0] = i * dyskretyzacja
    l[i,1] = trap(i * dyskretyzacja, 20, 40, 60, 90)
    l[i,2] = trap(i * dyskretyzacja, 110, 140, 180, 180)
    l[i,3] = triangle(i * dyskretyzacja, 70, 100, 130)
    l[i,4] = triangle(i * dyskretyzacja, 0, 0, 40)
    print(i * dyskretyzacja)


plt.plot(l[:,0],l[:,1],'r')
plt.plot(l[:,0],l[:,2],'b')
plt.plot(l[:,0],l[:,3],'g')
plt.plot(l[:,0],l[:,4],'c')
plt.axis([0,wartosci,0,1.2])







"""
wzrost=np.zeros((2,71))
for i in range(0,71):
    x=150+i
    wzrost[0,i]=x
    if x>=155 and x<=165:
        sredni=(x-155)/(165-155)
    elif x>165 and x<175:
        sredni=1
    elif x>=175 and x<=185:
        sredni=(185-x)/(185-175)
    else:
        sredni=0
    wzrost[1,i] = sredni
#---- graficzna prezentacja termu "sredni"
plt.plot(wzrost[0,:],wzrost[1,:],'r')
plt.axis([150,220,0,1.2])
plt.xlabel('wzrost [cm]')
plt.ylabel('u(wzrost)')
"""