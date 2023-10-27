import numpy as np
import matplotlib.pyplot as plt

def triangle(x, a, x0, b):
    try:
        if x >= a and x <= x0:
            return (x - a) / (x0 - a)
        elif x >= x0 and x <= b:
            return (b - x) / (b - x0)
        return 0
    except ZeroDivisionError:
        return 0

def setMax(*args):
    return max([i for i in args])

def setMin(*args):
    return min([i for i in args])

def setMax2Alg(arg1, arg2):
    return arg1 + arg2 - arg1 * arg2

def setMin2Alg(arg1, arg2):
    return arg1 * arg2

def setFill(var):
    return 1 - var

dyskretyzacja = 0.25
wartosci = 101
l = np.zeros((int(wartosci/dyskretyzacja),8))
for i in range(0,int(wartosci/dyskretyzacja)):
    l[i,0] = i * dyskretyzacja
    l[i,1] = triangle(i * dyskretyzacja, 30, 40, 50)
    l[i,2] = triangle(i * dyskretyzacja, 40, 60, 70)
    l[i,3] = setMax(l[i,1],l[i,2])
    l[i,4] = setMin(l[i,1],l[i,2])
    l[i,5] = setFill(l[i,2])
    l[i,6] = setMax2Alg(l[i,1],l[i,2])
    l[i,7] = setMin2Alg(l[i,1],l[i,2])
    
    
    
# plt.plot(l[:,0],l[:,1],'r')
# plt.plot(l[:,0],l[:,2],'b')
#plt.plot(l[:,0],l[:,3],'g')
# plt.plot(l[:,0],l[:,4],'c')
# plt.plot(l[:,0],l[:,5],'m')
# plt.plot(l[:,0],l[:,6],'g')
# plt.plot(l[:,0],l[:,7],'g')
plt.axis([0,wartosci,0,1.2])