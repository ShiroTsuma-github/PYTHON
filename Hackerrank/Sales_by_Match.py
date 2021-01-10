def sockMerchant(n, ar):
    wyn=0
    for item in set(ar):
        wyn+=int((ar.count(item))/2)
    return wyn

n=9
ar=[10,20,20,10,10,30,50,10,20]

result=sockMerchant(n,ar)
print(result)