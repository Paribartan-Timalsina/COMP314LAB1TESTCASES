def partition(arr,left,right):
    pivot=arr[right]
    i=left-1
    for j in range(left,right):
        if arr[j]<=pivot:
            i=i+1
            temp1=arr[j]
            arr[j]=arr[i]
            arr[i]=temp1
    temp=arr[right]
    arr[right]=arr[i+1]
    arr[i+1]=temp
    return i+1