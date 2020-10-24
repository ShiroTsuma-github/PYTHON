for co_i in range(2,10**4):
    counter=0
    while co_i>=1:
        if int(co_i)==1:
            print(True)
            counter=0
            break       
        elif co_i%2==0:
            co_i/=2
        elif co_i%2==1:
            co_i=3*co_i+1
        counter+=1
        if counter>=1000:
            raise Exception
    
