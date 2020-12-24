from pathlib import Path

PlikDoAnalizy=Path('analiza_tekstu//Lorem_Ipsum.txt')



class AnalizeText():
    def __init__(self,text=None,FilePath=None):
        self.text = text
        self.FilePath=FilePath
        self.total_letters=0
        self.alphabet={
        'q':0,'w':0,'e':0,'r':0,'t':0,'y':0,'u':0,'i':0,'o':0,'p':0,'[':0,']':0,'a':0,'s':0,'d':0,'f':0,'g':0,'h':0,'j':0,
        'k':0,'l':0,';':0,':':0,'{':0,'}':0,'"':0,"'":0,'|':0,'z':0,'x':0,'c':0,'v':0,'b':0,'n':0,'m':0,'o':0,'<':0,'.':0,
        '>':0,'?':0,'/':0,'1':0,'!':0,'2':0,'@':0,'3':0,'#':0,'4':0,'$':0,'5':0,'%':0,'6':0,'^':0,'7':0,'&':0,'8':0,'*':0,'9':0,
        '(':0,')':0,'-':0,'_':0,'=':0,'+':0,' ':0,'~':0,'0':0,'ą':0,'ć':0,'ę':0,'ł':0,'ź':0,'ż':0,'ń':0,',':0,
        }
    def CountLetters(self):
        if self.FilePath !=None:
            with(open(self.FilePath)) as File:
                for line in File.readlines():
                    for letter in line:
                        if letter=='\n':
                            continue
                        self.alphabet[letter.lower()]+=1
                        self.total_letters+=1
        if self.text !=None:
            for letter in self.text:
                if letter=='\n':
                    continue
                self.alphabet[letter.lower()]+=1
                self.total_letters+=1
    def Analize(self,sort='default'):
        percentages=[]
        for position in self.alphabet:
            try:
                percentage=(self.alphabet[position]/self.total_letters)*100
            except ZeroDivisionError:
                percentage=0
            finally:
                if sort=='default':
                    print(f'For letter [ {position} ]: {self.alphabet[position]}    accounting for: {round(percentage,3)}%')
        print(f'\nFor total of: {self.total_letters}')
                
#TO DO: COMPARE BETWEEN TWO TEXTS      
                
a=AnalizeText()
a.text="""SWRlYWx5IHNhIGphayBnd2lhemR5IC0gbmllIG1vem5hIGljaCBvc2lhZ25hYywgYWxlIG1vem5hIHNpZSBuaW1pIGtpZXJvd2FjLg0K
"""
b=AnalizeText()
b.text="""Idealy sa jak gwiazdy - nie mozna ich osiagnac, ale mozna sie nimi kierowac."""
a.CountLetters()
b.CountLetters()
a.Analize()
b.Analize()
