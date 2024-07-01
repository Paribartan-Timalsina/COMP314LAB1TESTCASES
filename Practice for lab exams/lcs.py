combination=[]
def lcs_memo(A,B,x,y):
    if (array[x][y]!=-1):
        return array[x][y]
    if(x==len(A) or y==len(B)):
        array[x][y] = 0
        lcs_table[x][y] = ""
        return array[x][y]
    if(A[x]==B[y]):
        array[x][y]= 1+lcs_memo(A,B,x+1,y+1)
        lcs_table[x][y] = A[x] + lcs_table[x + 1][y + 1]
    else:
        if lcs_memo(A, B, x + 1, y) > lcs_memo(A, B, x, y + 1):
            array[x][y] = lcs_memo(A, B, x + 1, y)
            lcs_table[x][y] = lcs_table[x + 1][y]
        else:
            array[x][y] = lcs_memo(A, B, x, y + 1)
            lcs_table[x][y] = lcs_table[x][y + 1]
    return array[x][y]

def lcs_tabu(A,B):
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if(i==0 or j==0):
                array[i][j]=0
            elif(A[i-1]==B[j-1]):
                array[i][j]=1+array[i-1][j-1]
            else:
                array[i][j]=max(array[i-1][j],array[i][j-1])
    i=len(A)
    j=len(B)
    print(i,j)
    req_string=[]
    while(i>0 or j>0):
        if(array[i-1][j-1] < array[i][j]):
            req_string.append(A[j+1])
            i-=1
            j-=1
            continue
        if(array[i][j-1]==array[i][j]):
            j-=1
            continue
        if(array[i-1][j]==array[i][j]):
            i-=1
    
    new_string=str("".join(req_string))[::-1]
    print(new_string)
    





    return array[i][j]


A="stratosphere"
B="atmosphere"
array=[[-1 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
# Initialize the LCS table to store the LCS strings
lcs_table = [["" for _ in range(len(B) + 1)] for _ in range(len(A) + 1)]
print(lcs_memo(A,B,0,0))
print(lcs_tabu(A,B))
print(array)
lcs_string = lcs_table[0][0]
print(f"LCS: {lcs_string}")

