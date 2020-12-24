#CHWILOWO ZAPRZESTANE


import numpy as np
from math import sqrt,ceil
text='ashuidsahiuysdahudsahiuasdhusdaghuyadgsyhudvgtasgdmas guysdagy jksdafhjkopjadksojio[adspjkoadpsadijslopsdf hjksdf bhjsdf bhjksdfhjk sdfkhj dfshkj dfsk hjubdas hydghuyvasghydghjasghidasghudvghjasghuy d'
start_length=len(text)
def correct_text(text=''):
    def find_multiplayer():
        x_sqr=ceil(sqrt(start_length))
        return x_sqr
    
    if text=='':
        return None
    else:
        shape=find_multiplayer()
        if shape**2-start_length>=shape:
            print(shape**2-start_length)
        text+=(shape**2-start_length)*' '
        return text,shape
    
def gen_pos_key(sqroot):
    if len(text)>=start_length+sqroot:
        for i in sqroot:
            pass
            # text_arr[sqroot]
text,shape=correct_text(text)
text_arr=np.array(list(text))
text_arr=text_arr.reshape(shape,shape)
print(text_arr)
print(text_arr.shape)
gen_pos_key(shape)
