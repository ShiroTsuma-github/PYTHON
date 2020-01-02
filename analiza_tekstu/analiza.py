try:
    f=open("Lorem_Ipsum.txt","r")

except FileNotFoundError():
    f=open(__file__,"r")
    print("welp")
finally:
    f.close()
    