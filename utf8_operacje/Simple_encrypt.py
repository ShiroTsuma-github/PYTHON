def string_to_utf(string):
    import re
    pattern=r'\d*x'
    re.search(pattern,string)
    for i in string:
        value=str(hex(ord(i)))
        prefix=re.search(pattern,value)
        value=value.replace(prefix.group(),'')
        value=list(value)
        for pos in range(len(value),4):
            value.insert(0,'0')
        value="".join(map(str, value))
        print(f'Charakter [ {i} ] : U+{value}                                       Link: [ https://www.compart.com/en/unicode/U+{value} ]')
        
def encrypt(FROM_file,TO_file,COUNTER_RESET=3016):
    to_encrypt=open(FROM_file,'r',encoding='utf-8')
    encrypted=open(TO_file,'w+',encoding='utf-8')
    content=to_encrypt.read()
    to_encrypt.close()
    error=0
    counter=0
    for i,letter in enumerate(content):
        if counter==COUNTER_RESET:
            counter=0
        encrypted.write(  chr(ord(letter)+13+counter)  )
        counter+=1
    encrypted.close()
    
def decrypt(FROM_TO_file,COUNTER_RESET=3016):
    encrypted=open(FROM_TO_file,'r',encoding='utf-8')
    enc_content=encrypted.read()
    encrypted.close()
    encrypted=open(FROM_TO_file,'w',encoding='utf-8')
    encrypted.close()
    error=0
    encrypted=open(FROM_TO_file,'a+',encoding='utf-8')
    try:
        counter=0
        for i,letter in enumerate(enc_content):
            if counter==COUNTER_RESET:
                counter=0
            encrypted.write(chr(ord(letter)-13-counter))
            counter+=1
    except ValueError:
        pass
    finally:
        encrypted.close()
        
# encrypt('utf8 operacje\Pozdrowienia.txt','utf8 operacje\encrypted.txt')
# decrypt('utf8 operacje\encrypted.txt')
string_to_utf('|羈|枈|芈|庈|檈|守|墈|粈|憈|ᚈ|撈|ᲈ|消|劈|皈|薈|炈|禈|躈|讈|喈|ᾈ|ᦈ|袈|玈|䦈|醈|针|䂈|㪈|⺈|䚈|㒈|㶈|⮈|㞈|䎈|ㆈ|█|⊈|侈|䲈|⢈|𖦈|𖚈|𖲈|𒞈|𖎈|𖾈|𑢈|ᎈ|𔢈|𕞈|𖂈|𔮈|𕒈|𕶈|늈|𒪈|횈|𕆈|𑖈|𓎈|𑺈||𔺈|ꎈ|𓾈|쪈|ﶈ|𕪈|𔖈||𑮈||솈|𓦈|𒒈|Ꚉ|쒈|있||춈|𐂈||愈|𒆈|𐦈|𓂈|𓚈|𔊈|𒶈|𑊈|뢈|鶈||鞈||뮈|𐚈|𐎈||떈|뺈|骈|ꂈ|𓲈||ꦈ|겈|𐲈||펈|킈||𐾈|꾈|'.replace('|',''))



#𒆈