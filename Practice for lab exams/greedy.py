def greedy(p,w,W,combination):
    rem_capacity=W
    profit=0
    for i in range(len(combination)):
        if(rem_capacity >= w[i] and rem_capacity>0):
            profit=profit+p[i]
            rem_capacity=rem_capacity-w[i]
        elif(rem_capacity < w[i] and rem_capacity>0):
            profit=profit+combination[i][2]*rem_capacity
            rem_capacity=0
    return profit

p = [60, 100, 120]
w = [10, 20, 30]
div=[]
for i in range(len(p)):
    div.append(p[i]/w[i])
W = 50
combination=list(zip(p,w,div))
combination.sort(key=lambda x:x[2],reverse=True)
print(combination)
print(greedy(p,w,W,combination))
