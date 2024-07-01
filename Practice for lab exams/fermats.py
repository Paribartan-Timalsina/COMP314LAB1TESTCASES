import math
import random
def fermat_test(number):
    for _ in range(5):
        random_number=random.randint(2,number-2)
        value=(random_number**(number-1))%number
        if(value==1):
            continue
        else:
            return False

logic=fermat_test(561)
if(logic):
    print("The number may be probably prime")
else:
    print("The number is composite")
