import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if j < (n+1-i):
                print(" ",end="")
            else:
                print("#",end="")
        print("")


n = int(input())
staircase(n)