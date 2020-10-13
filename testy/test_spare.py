def pa():
    from time import sleep
    def podzielne():
        x=0
        while 1 != 0:
            x=x+11
            sleep(0.5)
            print(x)



    x=1
    y=1
    fin=False
    wyn=60
    odp=[]
    while fin != True:
        if x>wyn and y>wyn:
            fin =True
        if x*y==wyn:
            odp.append([x,y])
        if x>wyn:
            y+=1
            x=1
        x+=1
    print(odp)
        
        
        
        
a=3
b=1
c=4


if a>c:
    _max=a
    _min=c
else:
    _max=c
    _min=a
if c<b:
    _max=b
    _min=c
else:
    _max=c
    _min=b
if a>b:
    _max=a
else:
    _max=b
print(_max," ",_min)