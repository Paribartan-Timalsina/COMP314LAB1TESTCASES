def dynamic(p,w,m,n):
    if(m==0 or n==0):
        return 0
    if(array[m][n]!=-1):
        return array[m][n]
    if(p[m-1]>n):
        array[m][n]=dynamic(p,w,m-1,n)
    else:
        array[m][n]=max(dynamic(p,w,m-1,n),p[m-1]+dynamic(p,w,m-1,n-w[m-1]))
    return array[m][n]


p = [1, 4, 5,7]
w = [1, 3,4,5]
W = 7
array=[[-1 for i in range(W+1)] for j in range(len(p)+1)]
print(dynamic(p,w,len(p),W))