class test():
    def __init__(self,f):
        self.f=f
    def __gt__(self,other):
        return self.f>other.f
        
        
a=test([5,2])
b=test([3,4])
c=test([2,2])
tab=[a,b,c]
print(min(tab).f)
for i in tab:
    if (2,2) == i.f:
        print('jest')
    else:
        print('nope')