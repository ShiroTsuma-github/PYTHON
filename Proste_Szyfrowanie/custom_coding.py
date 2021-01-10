import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from MyModules.QuickSort import QuickSortNestedList as qsn
import numpy as np
from math import sqrt,ceil

class CustomEncode():
    def __init__(self,text):
        self.__start_text_len=len(text)
        self.__shape=self.__find_multiplayer()
        self.text=self.__correct_text(text)
        self.__text_array=(np.array(list(self.text))).reshape(self.__shape,self.__shape)
        self.__Computer_change=True
        self.result=None
    @property
    def result(self):
        return self.__result
    @result.setter
    def result(self,result):
        if self.__Computer_change==True:
            self.__result=result
            self.__Computer_change=False
        else:
            print('This variable is only accessible to Program and doesn\'t allow user input')
    #======================================== basic starting text correction methods ===================================
    def __correct_text(self,text):
            text+=(self.__shape**2-self.__start_text_len)*'�'
            return text
    def __find_multiplayer(self):
            x_sqr=ceil(sqrt(self.__start_text_len))
            return x_sqr
        
    #*******************************************************************************************************************    
    #=============================================== self.Encode methods =============================================== 
    def __reshufle_text(self):
        lines=[]
        for gen_coord in range(0,self.__shape):
            line=[]
            x_val=gen_coord
            for coord in range(0,self.__shape):
                if x_val==self.__shape:
                    x_val=0
                line.append(self.__text_array[coord][x_val])
                x_val+=1
            lines.append(line)
        return lines
    
    def __reshufle_position(self,arrays):
        line_total={}
        for i,line in enumerate(arrays):
            line_total[i]=0
            for character in line:
                line_total[i]+=ord(character)
        return (sorted(line_total.items(), key = 
             lambda kv:(kv[1], kv[0])))  
    def __reshufle_values(self,arrays):
        output=[]
        for level in arrays:
            output.append(list(reversed(qsn(level))))
        return output
    #*******************************************************************************************************************
    def Encode(self):
        shuffled_lines=self.__reshufle_text()
        shuffled_position=[item[0] for item in (self.__reshufle_position(shuffled_lines))]
        a=list(map(lambda x:shuffled_lines[x],shuffled_position))
        a=(list(map(lambda x:''.join(a[x]),range(0,len(a)))))
        a=[[[ord(wyn),wyn]  for wyn in item] for item in a]
        a=self.__reshufle_values(a)
        a=[[wyn[1] for wyn in item]for item in a]
        a=(list(map(lambda x:''.join(a[x]),range(0,len(a)))))
        a=''.join(a)
        self.__Computer_change=True
        self.result=a
        
 
 
f=open('Proste_Szyfrowanie\\text.txt')
content=f.read()
f.close()
 
# print(ord('�'))
a=CustomEncode(content)
# a.result='beka'
a.Encode()
print(a.result)