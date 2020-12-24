tab=[]
n=-100
while True:
    tab.append([(n**2-(3*n)-10 ),n]) 
    n+=1
    if n==1000:
        break
    
for i,obj in enumerate(tab):
    if obj[0]==0:
        print(obj[0],f" : ({obj[1]}**2-(3*{obj[1]})-10 )    {obj[1]}")
        