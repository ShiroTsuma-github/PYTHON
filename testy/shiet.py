def dec(n):
    tab=[]
    while n!=0:
        tab.append(n%2)
        n//=2
    return (tab[::-1])

print(dec(123))