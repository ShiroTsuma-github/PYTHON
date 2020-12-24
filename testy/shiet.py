from mpmath import mp
a=mp.dps=101
a=mp.fdiv(5.0,7.0)
counter=0
a=str(a).replace('0.','')
for pos in a:
    counter+=1
    print(counter,pos)