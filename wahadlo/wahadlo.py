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
    _step=3
    _rep=3
_prev=_min
x=(_prev+(_max-_prev)*2)%_step

for i in range(0,_rep):
    #r=_max*2-_min
    r=(_prev+(_max-_prev)*2)
    for j in range(_prev,(_prev+(_max-_prev)*2),_step):
        if j <=_max:
            print(j,end=" ")
        else:
            print(r-j+_prev,end=" ")
        if j == r-x:
           
           _prev=abs((r-j+_prev)-_step)
           x=(_prev+(_max-_prev)*2)%_step
        elif j == r-_step:
            _prev=abs((r-j+_prev)-_step)
    if i == _rep-1:
        if _prev-_step==_min:
            _prev=_min
        print(_prev)
