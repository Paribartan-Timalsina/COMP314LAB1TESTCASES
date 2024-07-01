

def convert_to_binary(number):
    if(number==0):
        return 0
    if(number==1):
        return 1
    else:
        req_number=convert_to_binary(number//2)
        req_num=req_number*10+number%2
        return req_num


def brute_force(p,w,m):
    max_profit=0
    combination=0
    for i in range(pow(2,len(p))):
        profit=0
        rem_capacity=m
        
        binary=convert_to_binary(i)
        binary=str(binary).zfill(3)
        print(i)
        print(binary)
        for j in range(len(binary)):
            if(binary[j]== "1" and rem_capacity >= w[j] ):
                profit=profit+p[j]
                rem_capacity=rem_capacity-w[j]
        if(rem_capacity>0):
             for j in range(len(binary)):
                if(binary[j]== "0" and rem_capacity >= w[j] ):
                    profit=profit+p[j]
                    rem_capacity=rem_capacity-w[j]
                elif(binary[j]== "0" and rem_capacity < w[j]):
                     fraction=(p[j]/w[j])*(rem_capacity)
                     profit=profit+ fraction
                     rem_capacity=0
                     break
        if(profit>max_profit):
            max_profit=profit
            combination=i

    return max_profit,combination
p = [60, 100, 120]
w = [10, 20, 30]
W = 50
print(brute_force(p,w,W))