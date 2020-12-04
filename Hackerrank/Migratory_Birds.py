def migratoryBirds(arr):
    birds={
        1:0,
        2:0,
        3:0,
        4:0,
        5:0,
    }
    _max=[birds[1],1]
    for i in arr:
        birds[i]+=1
    for i in range(1,6):
        if birds[i]>_max[0]:
            _max[0]=birds[i]
            _max[1]=i
    return _max[1]
        
        
        
        


arr=[1,2,3,4,5,4,3,2,1,3,4]
result = migratoryBirds(arr)
print(result)

    
    