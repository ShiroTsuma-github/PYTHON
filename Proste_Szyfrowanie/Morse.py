LetterDict={
    'a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.',
    'f':'..-.','g':'--.','h':'....','i':'..','j':'.---',
    'k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.',
    'q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-',
    'w':'.--','x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---',
    '3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..',
    '9':'----.','0':'-----',',':'--..--','.':'.-.-.-','?':'..--..','"':'.-..-.',
    ':':'---...',"'":'.----.','-':'-....-','/':'-..-.','(':'-.--.',')':'-.--.-',
    ' ':'/','!':'-.-.--','+':'.-.-.','_':'-....-','$':'...-..-','=':'-...-','/':'-..-.',
    'ą':'.-.-',"ć":'-.-..','ę':'..-..','ł':'.-..-','ń':'--.--','ó':'---.','ś':'...-...','ż':'--..-.','ź':'--..-',
}
FROM_file='Proste_Szyfrowanie\Plik_do_odczytu.txt'
TO_file='Proste_Szyfrowanie\Zaszyfrowane.txt'
def EnkrypcjaMorsem(FROM_file,TO_file):
    to_encrypt=open(FROM_file,'r',encoding='utf-8')
    text=to_encrypt.read().lower()
    to_encrypt.close()
    encrypted=open(TO_file,'w+',encoding='utf-8')
    for i in range(0,len(text)):
        if i+1<=len(text)-1:
            print(LetterDict[text[i]],end=' ')
            encrypted.write(f'{LetterDict[text[i]]} ')
        else:
            print(LetterDict[text[i]],end='')
            encrypted.write(f'{LetterDict[text[i]]}')
    encrypted.close()
    print('')

def DekryptujMorsa(TO_file):
    to_decrypt=open(TO_file,'r',encoding='utf-8')
    text=to_decrypt.read()
    to_decrypt.close()
    to_decrypt=open(TO_file,'w',encoding='utf-8')
    word=''
    for i in range(0,len(text)):
        if text[i] == '/': 
            print(' ',end='')
            to_decrypt.write(' ')
        elif text[i]==' ' and len(word)!=0:
            temp=(list(LetterDict.keys())[list(LetterDict.values()).index(word)])
            print(temp,end='')
            to_decrypt.write(temp)
            word=''
        elif text[i] !=' ':
            word+=str(text[i])
        if i==len(text)-1:
            temp=(list(LetterDict.keys())[list(LetterDict.values()).index(word)])
            to_decrypt.write(temp)
            print(temp,end='')
      
EnkrypcjaMorsem(FROM_file,TO_file)          
# DekryptujMorsa(TO_file)

                
                
        
        
