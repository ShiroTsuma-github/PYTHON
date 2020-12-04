def birthday(s, d, m):
    methods=0
    for square in range(0,len(s)):
        temp=0
        if square+m<=len(s):
            for amount in range(0,m):
                temp+=s[square+amount]
            if temp==d:
                methods+=1
    return methods
            

s=[1,2,1,3,2]
d=3
m=2
result = birthday(s, d, m)
print(result)