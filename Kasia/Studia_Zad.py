def Nprint(text,end='',flush=True):
    print(text,end=end,flush=flush)
def DrawCell():
    for i in range(0,6):
        for j in range(0,12):
            if (j == 0 or j == 11) and (i ==0 or i==5):
                Nprint('+')
            elif i==0 or i==5:
                Nprint('-')
            elif i==3 and j==5:
                Nprint(6)
            elif j==0 or j==11:
                Nprint('|')
            else:
                Nprint(' ')
        Nprint('',end='\n')

DrawCell()
Nprint('test',end='\r')