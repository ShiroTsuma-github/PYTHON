import math
def diagonalDifference(arr):
    #=============================zmienne==============================#
    tabela=arr
    wskaznik=len(tabela)
    odrzuc=[]
    diag_l=0
    diag_r=0
    temp=0
    #===========================znajdywanie nieodpowiednich pól=========#
    for i in range(0,len(tabela)-1):
        if len(tabela[i]) == wskaznik and wskaznik %2==1 or len(tabela[i])== wskaznik and wskaznik==2:
            pass
        else:
            if  wskaznik%2==0:
                pass
            else:
                odrzuc.append(tabela[i])
                wskaznik-=1
                       
    #=========================odrzucanie nieodpowiednich pól==============#
    for i in odrzuc:
        if i == tabela[temp]:
            tabela.remove(tabela[temp])
            temp+=1

    #========================diagonal sums============================#
    for i in range(0,len(tabela)):
        diag_l=diag_l+tabela[i][i]
        diag_r=diag_r+tabela[i][(len(tabela[i])-1)-i ]
        
    #==============================return=============================#
    return abs((diag_l-diag_r))
    
print(diagonalDifference([[4],[-1,1,-7,-8],[-10,-8,-5,-2],[0,9,7,-1],[4,4,-2,1]]))