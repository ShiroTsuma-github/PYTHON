import matplotlib.pyplot as plt
import numpy as np

dyskTemp = 0.5
dyskWilg = 1
dyskWyj = 1

liczTemp = 35
liczWilg = 100
liczWyj = 100

resTemp = int(liczTemp/dyskTemp) + 1
resWilg = int(liczWilg/dyskWilg) + 1
resWyj = int(liczWyj/dyskWyj) + 1

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



outTemp = np.zeros((resTemp,5))
for i in range(0,resTemp):
    outTemp[i,0] = i * dyskTemp
    outTemp[i,1] = trap(i * dyskTemp, 0, 0, 5, 15)
    outTemp[i,2] = triangle(i * dyskTemp, 5, 15, 25)
    outTemp[i,3] = triangle(i * dyskTemp, 15, 25, 35)
    outTemp[i,4] = triangle(i * dyskTemp, 25, 35, 40)

outWilg = np.zeros((resWilg,4))
for i in range(0,resWilg):
    outWilg[i,0] = i * dyskWilg
    outWilg[i,1] = trap(i * dyskWilg, 0, 0, 25, 50)
    outWilg[i,2] = triangle(i * dyskWilg, 25, 50, 100)
    outWilg[i,3] = triangle(i * dyskWilg, 50, 100, 101)

outWyj = np.zeros((resWyj,6))
for i in range(0,resWyj):
    outWyj[i,0] = i * dyskWyj
    outWyj[i,1] = singleton(i * dyskWyj, 0)
    outWyj[i,2] = singleton(i * dyskWyj, 25)
    outWyj[i,3] = singleton(i * dyskWyj, 50)
    outWyj[i,3] = singleton(i * dyskWyj, 75)
    outWyj[i,4] = singleton(i * dyskWyj, 100)

"""
plt.plot(outTemp[:,0],outTemp[:,1],'r')
plt.plot(outTemp[:,0],outTemp[:,2],'b')
plt.plot(outTemp[:,0],outTemp[:,3],'g')
plt.plot(outTemp[:,0],outTemp[:,4],'c')
plt.axis([0,liczTemp,0,1.2])
plt.xticks([i * 5 for i in range(8)])
"""
"""
plt.plot(outWilg[:,0],outWilg[:,1],'r')
plt.plot(outWilg[:,0],outWilg[:,2],'b')
plt.plot(outWilg[:,0],outWilg[:,3],'g')
plt.axis([0,liczWilg,0,1.2])
plt.xticks([i * 10 for i in range(11)])
"""

"""
plt.axvline(x=0)
plt.axvline(x=25)
plt.axvline(x=50)
plt.axvline(x=100)
plt.axis([-1,liczWyj + 1,0,1])
plt.xticks([i * 10 for i in range(11)])
"""

def BlurData(data, point):
    for i in data:
        if i[0] == point:
            return [y for y in i[1:]]
        
blur1 = (BlurData(outTemp, 17.5))
blur2 = (BlurData(outWilg, 60))
#print(blur1)
#print(blur2)

def setMin(*args):
    return min([i for i in args])

def outMatrix(blurred1, blurred2):
    ans = []
    for y in range(len(blurred1)):
        ans.append([])
        for x in range(len(blurred2)):
            ans[y].append(min(blurred1[y], blurred2[x]))
    return ans

ansMat = outMatrix(blur1, blur2)
print(ansMat)

def retRules(Mat):
    rules = [
        [2, 1, 3],
        [3, 1, 0],
        [3, 2, 1],
        [4, 3, 2]]
    
    tempMat = [0, 0, 0, 0, 0]
    for y, line in enumerate(Mat):
        for x, pos in enumerate(line):
            tempMat[rules[y][x]] = max(pos, tempMat[rules[y][x]])
    return tempMat
    
singletons = [0, 25, 50, 75, 100]
rulesAns = retRules(ansMat)
#print(rulesAns)
y = round(sum( rulesAns[y] * singletons[y] for y in range(len(rulesAns))) / sum(rulesAns),4)
print(y)

charTemp = np.zeros((resTemp,2))
for x in range(resTemp):
    blur1 = (BlurData(outTemp, outTemp[x][0]))
    blur2 = (BlurData(outWilg, 60))
    ansMat = outMatrix(blur1, blur2)
    rulesAns = retRules(ansMat)
    y = round(sum( rulesAns[y] * singletons[y] for y in range(len(rulesAns))) / sum(rulesAns),4)
    charTemp[x, 0] = x * dyskTemp
    charTemp[x, 1] = y

    
plt.plot(charTemp[:,0],charTemp[:,1],'b') 
    