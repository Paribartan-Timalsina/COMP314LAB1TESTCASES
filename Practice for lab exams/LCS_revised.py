def lcs(A,B,X,Y):
    if(array[X][Y]!=-1):
        return array[X][Y]
    if(X==len(A) or Y==len(B)):
        array[X][Y]=0
        return 0
    if(A[X]==B[Y]):
        array[X][Y]= 1+lcs(A,B,X+1,Y+1)
    else:
        array[X][Y]= max(lcs(A,B,X+1,Y),lcs(A,B,X,Y+1))

    return array[X][Y]

        

A="atmosphere"
B="stratosphere"
array=[[-1 for i in range(len(B)+1)] for j in range(len(A)+1)]
print(lcs(A,B,0,0))
