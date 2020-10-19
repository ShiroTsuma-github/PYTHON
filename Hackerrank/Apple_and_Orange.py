
def countApplesAndOranges(s, t, a, b, apples, oranges):
    count_ap=0
    count_or=0
    for i in apples:
        if i+a >=s and i+a <=t:
            count_ap+=1
    for i in oranges:
        if b+i >=s and i+b <=t:
            count_or+=1
    return count_ap,count_or

print("Print Sam's House [x1] [x2]")

st = input().split()

s = int(st[0])

t = int(st[1])
print("Position of Apple Tree and Orange Tree")
ab = input().split()

a = int(ab[0])

b = int(ab[1])
print("Amount of Apples and Oranges")
mn = input().split()

m = int(mn[0])

n = int(mn[1])
print("Apples falling [x]")
apples = list(map(int, input().rstrip().split()))
print("Oranges falling [x]")
oranges = list(map(int, input().rstrip().split()))

a,b=countApplesAndOranges(s, t, a, b, apples, oranges)
print(a)
print(b)
