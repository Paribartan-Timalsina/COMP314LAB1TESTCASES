import sys
def matrix_multiplication(p0,j,k):
    if(array[j][k]!=-1):
        return array[j][k]
    if(j==k):
        return 0
    array[j][k]=sys.maxsize
    for i in range(j,k):
        value=min(array[j][k],matrix_multiplication(p0,j,i)+matrix_multiplication(p0,i+1,k)+p0[i]*p0[k]*p0[j-1])
        array[j][k]=value
    return array[j][k]


A1=(5,4)
A1=(4,6)
A1=(6,2)
A1=(2,7)
p0=[5,4,6,2,7]
array=[[-1 for i in range(len(p0))] for j in range(len(p0))]
print(matrix_multiplication(p0,1,len(p0)-1))