import os, sys

# sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
# from MyModules.QuickSort import QuickSortNestedList as qsn
import numpy as np
from math import sqrt,ceil


"""
coded with hex values of lines multiplied by amount of most common letter

TO DO:
    think about solving slightly differently encoded hex header with values of lines,because it is of shape of sqrt,so it tells shape of array too easily
"""

class CustomEncode():
    """My function to encode text based on creating array of size `sqrt` of length and ``rounding it up``. Later reading letters diagonally into the lists and  then sorting lines by sum of value of all letters.
    

    """
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
    def __Generate_key(self,text,numbers): 
        def get_key(val,_dict):
            l=[]
            for key, value in _dict.items():
                if val == value:
                    l.append(key)
            return l
        values=set(list(text))
        values.discard('�')
        values.discard(' ')
        values.discard('\n')
        values_keys=values
        values={item:0 for item in values}
        for letter in values_keys:
            values[letter]=text.count(letter)
        del text
        if len(values)==0:
            return '|None|'
        max_value_letters=''
        letters_to_encode_with=''
        
        
        while True and len(values)!=1:
            max_value_letters=(get_key(max(values.values()),values))
            if len(max_value_letters)>1:
                if len(values)-len(max_value_letters)>1:
                    [values.pop(x,None) for x in max_value_letters]
                else:
                    letters_to_encode_with=max_value_letters
                    break
            else:
                letters_to_encode_with=max_value_letters
                break
        else:
            letters_to_encode_with=values.values()
        del max_value_letters
        del values_keys
        
        key=sum(list(map(lambda x:values[x],letters_to_encode_with)))
        result='|'
        for number in numbers:
            result+=f'{(hex(number*key))}|'
        return result

    #*******************************************************************************************************************
    def Encode(self):
        shuffled_lines=self.__reshufle_text()
        shuffled_position=[item[0] for item in (self.__reshufle_position(shuffled_lines))]
        a=list(map(lambda x:shuffled_lines[x],shuffled_position))
        del shuffled_lines
        a=(list(map(lambda x:''.join(a[x]),range(0,len(a)))))

        a=''.join(a)
        a=list(a)
        a.insert(0,self.__Generate_key(a,shuffled_position))
        a=''.join(a)
        self.__Computer_change=True
        self.result=a
        

f=open('Proste_Szyfrowanie\\text.txt')
content=f.read()
f.close()
 
a=CustomEncode(content)
a.Encode()
f=open('Proste_Szyfrowanie\\w.txt','w+',encoding='utf-8',errors='ignore')
f.write(a.result)
f.close()