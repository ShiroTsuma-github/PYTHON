def birthdayCakeCandles(candles):
    #return len(list(filter(lambda x: x== max(candles),candles)))
    m=max(candles)
    amount=0
    for i in candles:
        if i ==m:
            amount+=1
    return amount
        



candles_count = int(input().strip())
candles = list(map(int, input().rstrip().split()))
result = birthdayCakeCandles(candles)

print(result)