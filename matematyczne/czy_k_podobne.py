A=[4,7,1,4,5]
B=[1,4,5,4,7]
n=5
k=2
def czy_k_podobne(n,A,B,k):
    for k_pos in range(0,k):
        if A[k_pos]==B[n-k+k_pos] and A[k+k_pos]==B[k_pos-k]:
            return 'prawda'
        
# print(czy_k_podobne(n,A,B,k))
tab=[]
def sym(a,b):
    if a!=0:
        sym(a-1,b+1)
        print(a*b)
        tab.append(a*b)
        sym(a-1,b+1)
        
sym(10,2020)
print('')
print(len(tab))