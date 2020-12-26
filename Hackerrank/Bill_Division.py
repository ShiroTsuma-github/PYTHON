def bonAppetit(bill, k, b):
    del bill[k]
    Anns_part=sum(bill)/2
    if Anns_part==b:
        print('Bon Appetit')
    else:
        print(int(b-Anns_part))






text='4 1'
nk = text.rstrip().split()
n = int(nk[0])
k = int(nk[1])
text='3 10 2 9'
bill = list(map(int, text.rstrip().split()))
del text
del nk
b = 12
bonAppetit(bill, k, b)