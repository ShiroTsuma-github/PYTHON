#NEED FOR FILLING EMPTY SPACES OF ARRAY THAT ARE FILLED AS UTF-8 HIGH VALUE CHARACTERS FOR REMOVING
#PROBLEMS WITH PADDING OF TEXT
#TEMP FIX: FILLING WITH MISSING CHARACTER CHAR
 
 
import numpy as np
from math import sqrt,ceil
class CustomEncode():
    def __init__(self,text):
        self.__start_text_len=len(text)
        self.__shape=self.__find_multiplayer()
        self.text=self.__correct_text(text)
        self.__text_array=(np.array(list(self.text))).reshape(self.__shape,self.__shape)
 
    def __correct_text(self,text):
            text+=(self.__shape**2-self.__start_text_len)*'�'
            return text
    def __find_multiplayer(self):
            x_sqr=ceil(sqrt(self.__start_text_len))
            return x_sqr
 
    def __reshufle_text(self):
        lines=[]
        for gen_coord in range(0,self.__shape):
            line=[]
            x_val=gen_coord
            for coord in range(0,self.__shape):
                if x_val==self.__shape:
                    x_val=0
                line.append(self.__text_array[coord][x_val])
                # print(self.__text_array[coord][x_val],end='')
                x_val+=1
 
            # print('')
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
    def Encode(self):
        shuffled_lines=self.__reshufle_text()
        shuffled_position=self.__reshufle_position(shuffled_lines)
        print(shuffled_position)
 
 
 
 
 
 
 
 
# print(ord('�'))
a=CustomEncode('ashuidsahiuysdahudsahiuasdhusdaghuyadgsyhudvgtasgdmas guysdagy jksdafhjkopjadksojio[adspjkoadpsadijslopsdf hjksdf bhjsdf bhjksdfhjk sdfkhj dfshkj dfsk hjubdas hydghuyvasghydghjasghidasghudvghjasghuy d')
a.Encode()