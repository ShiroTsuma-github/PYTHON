import os
def sciezka():
    script_dir = os.path.dirname(__file__)
    rel_path = "analiza_tekstu/Lorem_Ipsum.txt"
    abs_file_path = os.path.join(script_dir, rel_path)
    return abs_file_path

file=open(abs_file_path,"r")
print(file.read())
file.close()
