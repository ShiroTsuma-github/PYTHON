tab=[5,3,2,14,1,4,3,5,6,7,12,-2]
temp=tab[0]
for i in range(0,len(tab)-1):
    for j in range(i,len(tab)):
        if tab[i]>tab[j]:
            temp=tab[j]
            tab[j]=tab[i]
            tab[i]=temp
            
print(tab)