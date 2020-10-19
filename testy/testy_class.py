import math
import os
import random
import re
import sys

def plusMinus(arr):
    pos=0
    neg=0
    zer=0
    for i in arr:
        if i>0:
            pos+=1
        elif i<0:
            neg+=1
        else:
            zer+=1
    return format(pos/n, '.6f'), format(neg/n, '.6f'), format(zer/n, '.6f')

n = int(input())

arr = list(map(int, input().rstrip().split()))

a,b,c=plusMinus(arr)
print(a)
print(b)
print(c)