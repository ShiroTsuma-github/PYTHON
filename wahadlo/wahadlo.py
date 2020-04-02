import math
hand_input=False

if hand_input:
    _min=input("min: ")
    _max=input("max: ")
    _step=input("step: ")
    _rep=input("repeats: ")
else:
    _min=0
    _max=8
    _step=5
    _rep=2
_prev=_min
x=(_prev+(_max-_prev)*2)%_step
"""
for i in range(0,_rep):
    #r=_max*2-_min
    r=(_min+(_max-_min)*2)
    for j in range(_prev,(_min+(_max-_min)*2),_step):
        if j <=_max:
            print(j,end=" ")
        else:
            print(r-j+_min,end=" ")
        if j == r-x:
           #pass
           _prev=abs((r-j+_min)-_step)
    if i == _rep-1:
        print(_prev)
"""
for i in range(0,_rep):
    #r=_max*2-_min
    r=(_prev+(_max-_prev)*2)
    for j in range(_prev,(_prev+(_max-_prev)*2),_step):
        if j <=_max:
            print(j,end=" ")
        else:
            print(r-j+_prev,end=" ")
        if j == r-x:
           #pass
           _prev=abs((r-j+_prev)-_step)
           x=(_prev+(_max-_prev)*2)%_step
    if i == _rep-1:
        if _prev-_step==_min:
            _prev=_min
        print(_prev)
