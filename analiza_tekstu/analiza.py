import os

nazwa=input("Podaj nazwe pliku: ")

script_dir = os.path.dirname(__file__)
rel_path =nazwa
abs_file_path = os.path.join(script_dir, rel_path)


file=open(abs_file_path,"r")
print(file.read())
file.close()

