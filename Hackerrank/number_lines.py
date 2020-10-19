def kangaroo(x1, v1, x2, v2):
    jumps=0
    diff=abs(x1-x2)
    while True:
        if x1+jumps*v1==x2+jumps*v2:
            return 'YES'
        jumps+=1
        if diff <= abs((x1+jumps*v1)-(x2+jumps*v2)):
            return 'NO'



x1V1X2V2 = input().split()

x1 = int(x1V1X2V2[0])

v1 = int(x1V1X2V2[1])

x2 = int(x1V1X2V2[2])

v2 = int(x1V1X2V2[3])

result = kangaroo(x1, v1, x2, v2)
print(result)
