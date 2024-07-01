# def dynamic(p,w,m,n):
#     if(m==0 or n==0):
#         return 0
#     if(array[m][n]!=-1):
#         return array[m][n]
#     if(w[n-1]>m):
#         array[m][n]= dynamic(p,w,m,n-1)
#     else:
#         value=max(dynamic(p,w,m,n-1),p[n-1]+dynamic(p,w,m-w[n-1],n-1))
#         array[m][n]=value
#     return array[m][n]
















def dynamic(p,w,capacity,n):
    if(capacity==0 or n==0):
        array[capacity][n]=0
    if(array[capacity][n]!=-1):
        return array[capacity][n]
    if (w[n-1] > capacity):
        array[capacity][n]=dynamic(p,w,capacity,n-1)
    else:
        array[capacity][n]=max(dynamic(p,w,capacity,n-1),p[n-1]+dynamic(p,w,capacity-w[n-1],n-1))
    return array[capacity][n]





p = [1, 4, 5,7]
w = [1, 3,4,5]
W = 7
array=[[-1 for i in range(len(p)+1)] for j in range(W+1)]
print(dynamic(p,w,W,len(p)))