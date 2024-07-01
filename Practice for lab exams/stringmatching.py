def string_matching(A,B):
    len1=len(A)
    len2=len(B)
    diff=len1-len2
    for i in range(diff+1):
        j=0
        while(j < len2 and B[j]==A[j+i] ):
            j=j+1
        if(j==(len2)):
            print("The string is matched")
            return
    print("The string isn't matched")
    




        
    




A="prereo"
B="pre"
string_matching(A,B)