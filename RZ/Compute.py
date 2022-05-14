text='elo co tam u was ( adssd ( elo ) )'
operators={
    'v':'',
    '^':'',
    '!':'',
    '>':'',
    '<>':''
}
def alt(op1,op2):
    return True if (op1 or op2) else False

def kon(op1,op2):
    return True if (op1 and op2) else False

def neg(op):
    return not op

def imp(op1,op2):
    return False if (op1 and op2!=op1) else True

def row(op1,op2):
    return True if op1==op2 else False

# text=input("Podaj rachunek: \n").split()
text=text.split()
depth=0
words=[]
depths={0:[0,len(text)-1]}
for pos,word in enumerate(text):
    if word=='(':
        depth+=1
        depths[depth]=[pos+1,pos+1]
    elif word==')':
        depths[depth]=[depths[depth][0],pos]
        depth-=1
# print(words)
# 

for i in reversed(depths):
    temp=text[depths[i][0]:depths[i][1]]
    del(text[depths[i][0]-1:depths[i][1]+1])
    # print(text)
    # print(temp)
    # print(depths[i])
    # print(text[depths[i][0]])
    # print(depths[i][0]-1,end='\n==================')
    
    text[depths[i][0]-1]=[text[depths[i][0]-1],temp]
    print(text)
# print(depths)
