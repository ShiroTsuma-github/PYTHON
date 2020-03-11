def f(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return f(n-1) + f(n-2)
for x in range(2,8):
    print(f(x))