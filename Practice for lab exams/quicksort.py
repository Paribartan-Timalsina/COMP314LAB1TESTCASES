def partition(array,left,right):
    pivot=array[right]
    moving_pointer=left-1
    for i in range(left,right):
        if(array[i] <= pivot):
            moving_pointer=moving_pointer+1
            array[i],array[moving_pointer]=array[moving_pointer],array[i]
    array[right],array[moving_pointer+1]=array[moving_pointer+1],array[right]
    return moving_pointer+1

def quicksort(array,left,right):
    if(left<right):
        pivot=partition(array,left,right)
        quicksort(array,left,pivot-1)
        quicksort(array,pivot+1,right)

array=[7,6,8,9,2,6,9,10]
quicksort(array,0,len(array)-1)
print(array)