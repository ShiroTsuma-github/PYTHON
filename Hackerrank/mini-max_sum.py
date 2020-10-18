def miniMaxSum(arr):
    return (sum(arr)-min(arr)),(sum(arr)-max(arr))

arr = list(map(int, input().rstrip().split()))
a, b=miniMaxSum(arr)
print(b, a)
