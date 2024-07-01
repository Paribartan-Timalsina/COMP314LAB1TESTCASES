# def dynamic(p,w,m,n):
#    array=[[0 for i in range(W+1)] for j in range(len(p)+1)]
#    for i in range(len(p)+1):
#       for j in range(W+1):
#          if(i==0 or j==0):
#             array[i][j]=0
#          elif(w[i-1] <= j):
#             array[i][j]=max(array[i-1][j],p[i-1]+array[i-1][j-w[i-1]])
#          else:
#             array[i][j]=array[i-1][j]






















def dynamic_tabu(p,w,capacity):
    array=[[0 for i in range(W+1)] for j in range(len(p)+1)]
    for i in range(len(p)+1):
        for j in range(W+1):
            if(i==0 or j==0):
                array[i][j]=0
            elif(w[i-1]<=j):
                array[i][j]=max(array[i-1][j],p[i-1]+array[i-1][j-w[i-1]])
            else:
                array[i][j]=array[i-1][j]
    i,j=len(p),W
    combination_matrix=[ 0 for i in range(len(p))]
    while(i>=0 and j>=0):
        for k in range(W+1):
            if(array[i-1][k]==array[i][j]):
                combination_matrix[i-1]=1
                j=W-array[i][j]
        i-=1
    print(combination_matrix)
    

    return array[i][j]



p = [1, 4, 5,7]
w = [1, 3,4,5]
W = 7

print(dynamic_tabu(p,w,W))