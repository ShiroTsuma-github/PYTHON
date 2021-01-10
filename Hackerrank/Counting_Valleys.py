def countingValleys(steps, path):
    sea_level=0
    level=0
    mountain=0
    valley=0
    path=list(path)
    for letter in path:
        if letter=='U':
            
            if level+1==sea_level:
                valley+=1
            level+=1
        else:
            
            if level-1==sea_level:
                mountain+=1
            level-=1
    return(valley)

steps=8
path='UDDDUDUU'
result=countingValleys(steps,path)
print(result)