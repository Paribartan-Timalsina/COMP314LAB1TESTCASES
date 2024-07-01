def merge(arr,left,middle,right):
    n1=middle-left+1
    n2=right-middle
    left_array=[0]*(n1+1)
    right_array=[0]*(n2+1)
    for i in range(0,n1):
        left_array[i]=arr[left+i]
    for j in range(0,n2):
        right_array[j]=arr[middle+j+1]
    left_array[n1]=float('inf')
    right_array[n2]=float('inf')
    i=0
    j=0
    for k in range(left,right+1):
        if left_array[i] <= right_array[j]:
            arr[k]=left_array[i]
            i=i+1
        else:
            arr[k]=right_array[j]
            j=j+1
    return arr
