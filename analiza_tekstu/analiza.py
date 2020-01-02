import os
alphabet=('q','w','e','r','t','y','u','i','o','p','[',']','a','s','d','f','g','h','j',
'k','l',';',':','{','}','"',"'",'|','z','x','c','v','b','n','m',',','<','.','>','?','/',
'1','!','2','@','3','#','4','$','5','%','6','^','7','&','8','*','9','(',')','-','_','=','+',' ','~','0'
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


try:
    nazwa=input("Podaj nazwe pliku: ")
    file=open(sciezka(nazwa),"r")
    text=file.read()
    for i in range(0,len(alphabet)):
        char=alphabet[i]
        temp=liczenie_char(text,char)
        lacznie=lacznie+temp
        print("Dla znaku "+str(alphabet[i])+" ",temp)
    print("Laczna ilosc: "+ str(lacznie))
    #print(laczna_ilosc_char(text))
except:
    raise 

finally:
    file.close()

