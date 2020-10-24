
def getTotalX(a, b):
    a=sorted(a)
    b=sorted(b)
    for a_i in range(a[0],b[0]+1):
        ok=lambda x:len(x)==len(a),(list(filter(lambda x : x%a_i==0,a)))
        print(ok)


#first_multiple_input = input().rstrip().split()
#size of first arr
#n = int(first_multiple_input[0])
#size of sec arr
#m = int(first_multiple_input[1])
#arr1
#arr = list(map(int, input().rstrip().split()))
#arr2
#brr = list(map(int, input().rstrip().split()))

arr=[2,4]
brr=[16,32,96]
total = getTotalX(arr, brr)
print(total)