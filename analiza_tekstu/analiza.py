try:
    f=open("Lorem_Ipsum.txt","r")

except FileNotFoundError():
    x=__file__
    f=open(x,"r")
    print("welp")
finally:
    f.close()
    