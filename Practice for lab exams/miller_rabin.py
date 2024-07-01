import math 
import random
def get_required_number(number):
    value=number-1
    count=0
    while(value%2!=1):
        value=value/2
        count+=1
    print(value,count)
    return value,count
def miller_rabin(number):
    value,count=get_required_number(number)
    random_number=random.randint(2,number-2)
    b0=(2**value) % number
    if(b0 == number-1):
        b0=-1
    if(b0==1 or b0==-1):
        return True
    else:
        iterative_value=b0
        for i in range(1,count+1):
            iterative_value=(iterative_value**2)%number
            if(iterative_value==number-1):
                iterative_value=-1
            if(iterative_value==1):
                return False
            if(iterative_value==-1):
                return True
        return False

    
decision=miller_rabin(113)
if(decision):
     print("The number may be probably prime")
else:
     print("The number is composite")