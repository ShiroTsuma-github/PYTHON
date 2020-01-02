import os
script_dir = os.path.dirname(__file__)
rel_path ="Lorem_Ipsum.txt"
abs_file_path = os.path.join(script_dir, rel_path)

file=open(str(abs_file_path),"r")
print(file.read())
file.close()
