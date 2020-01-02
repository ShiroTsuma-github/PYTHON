import os

def sciezka(nazwa):
    script_dir = os.path.dirname(__file__)
    rel_path =nazwa
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path

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
    print(liczenie_char(text,"a"))
except FileNotFoundError:
    pass

finally:
    file.close()

