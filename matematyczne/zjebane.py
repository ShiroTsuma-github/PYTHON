# def silnia(x):
#     if x==1:
#         return 1
#     else:
#         return x*silnia(x-1)

# n=4

# while True:
#     ns=(silnia(n))
#     ks=(silnia(n-3))
#     dif=silnia(n-(n-3))
#     first=ns/(ks*dif)
#     if first<=n-1:
#         print(n,True)
#         break
#     else:
#         print(False)
#     print(f'{first}<={n-1}')
#     if n==1000:
#         break
#     n+=1
l=9
print(l+3-(l%3))