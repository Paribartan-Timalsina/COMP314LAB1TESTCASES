def matrix_multiplication(p0,i,j):
    if(array[i][j]!=-1):
        return array[i][j]
    if(i==j):
        return 0
    array[i][j]=float('inf')
    for k in range(i,j):
        value=matrix_multiplication(p0,i,k)+matrix_multiplication(p0,k+1,j)+p0[k]*p0[i-1]*p0[j]
        if(value<array[i][j]):
            array[i][j]=value
    return array[i][j]

p0 = [5, 4, 6, 2, 7]
length=len(p0)-1
array = [[-1 for _ in range(length+1)] for _ in range(length+1)]

print(matrix_multiplication(p0,1,length))
print(array)