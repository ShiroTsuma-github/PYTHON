hand_input=False
if hand_input:
    _min=input("min: ")
    _max=input("max: ")
    _step=input("step: ")
    _rep=input("repeats: ")
else:
    _min=1
    _max=3
    _step=1
    _rep=3
    
for i in range(0,_rep):
    #r=_max*2-_min
    r=((_max)-_min)*2+1
    for j in range(_min,r,_step):
        if float(j) <=round(r/2):
            print(j)
        else:
            print(r-j)
    if i == _rep-1:
        print(_min)
        
