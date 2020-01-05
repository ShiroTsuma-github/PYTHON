try:
    def is_prime(num):
        count=0
        if num%2==0 and num>2:
            pass
        else:
            #tab2=[x for x in range(1,num+1)]
            #tab=list(filter(lambda x: x%2,tab2))
            for i in range(1,num+1):
                if num%i==0:
                    count+=1
                if count>2:
                    break
            if count<=2:
                return num
            else:
                pass
                
    
    def get_primes():
        try:
            num = 1
            while True:
                if is_prime(num):      
                    yield (num)
                    num += 1
                else:
                    num+=1
        except  GeneratorExit:
            print("welp")

    for i in get_primes():
        print(i)
except:
    pass