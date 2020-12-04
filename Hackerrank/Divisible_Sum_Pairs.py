def divisibleSumPairs(n, k, ar):
    _sum=0
    for j in range(0,n-1):
        for i in range(j+1,n):
            temp=ar[i]+ar[j]
            if temp%k==0:
                _sum+=1
    return _sum
n=6
k=3
ar=[1,3,2,6,1,2]
result = divisibleSumPairs(n, k, ar)
print(result)