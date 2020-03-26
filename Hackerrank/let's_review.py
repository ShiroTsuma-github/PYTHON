# Enter your code here. Read input from STDIN. Print output to STDOUT
word=input()
if type(word)==int:
    times=word
for t in range(0,word):
    for i in range(0,len(word)-1):
        if i ==0:
            pass
        else:
            if i%2==0