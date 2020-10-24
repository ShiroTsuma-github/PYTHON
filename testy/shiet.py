from random import randint
x=randint(0,9999)
y=randint(0,9999)
while x!=y:
    x=randint(0,999999)
    y=randint(0,999999)
    print(x, y)
print("Found same ",x, y)

    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<head>\n")
    f.write(' <meta charset="utf-8">\n')
    f.write("</head>\n")
    f.write("<body>\n")
    f.close()