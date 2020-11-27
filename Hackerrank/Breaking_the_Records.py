def breakingRecords(scores):
    _max=scores[0]
    _max_times=0
    _min=scores[0]
    _min_times=0
    for match in scores:
        if match>_max:
            _max_times+=1
            _max=match
        elif match<_min:
            _min_times+=1
            _min=match
    return _max_times,_min_times
        
    





text='3 4 21 36 10 28 35 5 24 42'
scores=list(map(int,text.rstrip().split()))
# print(scores)

result = breakingRecords(scores)
print(result)