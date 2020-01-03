import os
alphabet=('q','w','e','r','t','y','u','i','o','p','[',']','a','s','d','f','g','h','j',
'k','l',';',':','{','}','"',"'",'|','z','x','c','v','b','n','m',',','<','.','>','?','/',
'1','!','2','@','3','#','4','$','5','%','6','^','7','&','8','*','9','(',')','-','_','=','+',' ','~','0',
)
lacznie=0
def sciezka(nazwa):
    sciezka_do_folderu = os.path.dirname(__file__)
    sciezka_z_folderu_do_pliku =nazwa
    pelna_sciezka = os.path.join(sciezka_do_folderu, sciezka_z_folderu_do_pliku)
    return pelna_sciezka

def liczenie_char(text,char):
    count=0
    for i in text:
        if i==char:
            count+=1
    return count

def wyrazy(text):
    wyrazy={}
    temp=[]
    count=0
    for i in text:
        if i != " ":          
            temp.append(str(i))
        else:
            """
            f=open("test.txt","a+")
            f.write(str(temp))
            f.close
            """
            wyraz=("".join(temp))
            wyrazy[count]=wyraz #wystepuje problem,ze nie chce wpisywac,wiec robie droga na okolo
            count+=1
            temp.clear()
    return wyrazy
    
    


try:
    nazwa=input("Podaj nazwe pliku: ")
    file=open(sciezka(nazwa),"r")
    text_sub=file.read()
    text=text_sub.lower()
    
    for i in range(0,len(alphabet)):
        char=alphabet[i]
        temp=liczenie_char(text,char)
        lacznie=lacznie+temp
        print("Dla znaku "+str(alphabet[i])+" ",temp)
    
    print("Laczna ilosc: "+ str(lacznie))
    
    print(wyrazy(text))
except:
    raise 

finally:
    file.close()

