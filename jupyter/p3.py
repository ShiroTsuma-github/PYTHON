import numpy as np
import matplotlib.pyplot as plt


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

def triangle(x, a, x0, b):
    try:
        if x > a and x <= x0:
            return (x - a) / (x0 - a)
        elif x >= x0 and x <= b:
            return (b - x) / (b - x0)
        return 0
    except ZeroDivisionError:
        return 0

def BlurData(data, point):
    for i in data:
        if i[0][0] == point:
            return [i[y][1] for y in range(data.shape[1])]

def BlurResult(dataIn,dataOut, point, dysk1, dysk2):
    ans = np.zeros((int(101/dysk2),3,2))
    res = BlurData(dataIn, point)
    for y, i in enumerate(dataOut):
        for x, j in enumerate(i):
            ans[y][x][0] = dataOut[y][x][0]
            ans[y][x][1] = min(res[x], dataOut[y][x][1])
    return ans
    
def setMax(*args):
    return max([i for i in args])

def Focus(dataIn):
    top = sum([dataIn[y][0][1] * dataIn[y][0][0] for y in range(len(dataIn))])
    bot = sum([dataIn[y][0][1] for y in range(len(dataIn))])
    return top / bot

dyskretyzacja = 0.5
dysk1= dyskretyzacja
wartosci = 51
l = np.zeros((int(wartosci/dyskretyzacja),3,2))
for i in range(0,int(wartosci/dyskretyzacja)):
    l[i,0] = (i * dyskretyzacja, trap(i * dyskretyzacja, 0, 0, 20, 30))
    l[i,1] = (i * dyskretyzacja, triangle(i * dyskretyzacja, 20, 30, 40))
    l[i,2] = (i * dyskretyzacja, trap(i * dyskretyzacja, 30, 40, wartosci, wartosci))

fig2, (ax1, ax2, ax3) = plt.subplots(nrows=3, ncols=1)
#fig1, ax1 = plt.subplots()
ax1.plot(l[:,0][:,0],l[:,0][:,1],'r')
ax1.plot(l[:,1][:,0],l[:,1][:,1],'b')
ax1.plot(l[:,2][:,0],l[:,2][:,1],'g')
ax1.axis([0,wartosci,0,1.2])
ax1.set_title("Zbior wejsciowy")
#ax1.xticks([i * 5 for i in range(11)])


dyskretyzacja = 1
dysk2 = dyskretyzacja
wartosci = 101
l2 = np.zeros((int(wartosci/dyskretyzacja),3,2))
for i in range(0,int(wartosci/dyskretyzacja)):
    l2[i,0] = (i * dyskretyzacja, triangle(i * dyskretyzacja, 0, 0, 50))
    l2[i,1] =  (i * dyskretyzacja, triangle(i * dyskretyzacja, 20, 60, 80))
    l2[i,2] = (i * dyskretyzacja, triangle(i * dyskretyzacja, 60, 100, 110))


ax2.plot(l2[:,0][:,0],l2[:,0][:,1],'r')
ax2.plot(l2[:,1][:,0],l2[:,1][:,1],'b')
ax2.plot(l2[:,2][:,0],l2[:,2][:,1],'g')
ax2.axis([0,wartosci,0,1.2])
ax2.set_xlabel("Zbior wyjsciowy")


t = float(input( 'Podaj x: '))
temp = BlurResult(l, l2, t, 0.5, 1)
ax3.plot(temp[:,0][:,0],temp[:,0][:,1],'r')
ax3.plot(temp[:,1][:,0],temp[:,1][:,1],'b')
ax3.plot(temp[:,2][:,0],temp[:,2][:,1],'g')
ax3.axis([0,wartosci,0,1.2])
#c

plt.figure()
sumtemp = np.zeros((int(wartosci/dysk2),1,2))
for y, line in enumerate(temp):
    sumtemp[y][0][0] = temp[y][0][0]
    sumtemp[y][0][1] = setMax(temp[y][0][1],temp[y][1][1],temp[y][2][1])
#print(temp[:,0][:,1])
plt.plot(sumtemp[:,0][:,0],sumtemp[:,0][:,1],'r')
plt.axis([0,wartosci,0,1.2])
plt.xticks([i * 10 for i in range(11)])
print(Focus(sumtemp))
