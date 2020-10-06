import os
ten_folder = os.path.dirname(os.path.abspath(__file__))
ten_plik=(os.path.join(ten_folder, 'data.txt'))
dane=open(ten_plik,'r')

to_change=dane.read()
word=''
words=[]
try:
    for counter,i in enumerate(to_change):
        if i == ' ':
            words.append(word)
            word=''
        elif i == '(':
            words.append(i)
        elif i ==',':
            pass
        else:
            if to_change[counter+1] ==')':
                words.append(word)
                word=''
            else:
                word+=str(i)
except IndexError:
    pass
finally:
    actual1=[]
    actual2=[]
    do=0
    #print(words)
    for counter,word in enumerate(words):
        if word == '(':
            do+=1
        if word == ')':
            do+=1
        if do==1 and word != '(' and word != ')' :
            actual1.append(word)
        if do ==3 and word != '(' and word != ')' :
            actual2.append(word)
    print(f'db.faktury.insert({{"_{actual1[0]}":"{actual2[0]}","{actual1[1]}":"{actual2[1]}","{actual1[2]}":"{actual2[2]}","{actual1[3]}":"{actual2[3]}","{actual1[4]}":"{actual2[4]}","{actual1[5]}":"{actual2[5]}"}})')
            
        
        