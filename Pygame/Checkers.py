from time import sleep
def Nprint(text,end='',flush=True):
    print(text,end=end,flush=flush)
def clear(): 
    from os import system, name 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

class Checkers():
    def __init__(self,positions):
        pass
    class __Checker():
        def __init__(self,type,color,position=None):
            self.type=self.__check_valid(type)
            self.moveset=self.__get_moveset()
            self.color=color
        def __get_moveset(self):
            pass
        def __check_valid(self,inp):
            if inp.upper() == 'Q' or inp.upper() == 'C':
                return inp.upper()
            else:
                raise 'NotValidCheckerType'
    def Checker(self,type,color):
        return self.__Checker()
        
    
        

table=Checkers()
table.Checker()