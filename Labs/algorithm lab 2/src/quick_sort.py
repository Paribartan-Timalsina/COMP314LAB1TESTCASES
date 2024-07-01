from src.partition import partition

def quick_sort(arr,left,right):
    if left<right:
        middle = partition(arr,left,right)
        quick_sort(arr,left,middle-1)
        quick_sort(arr,middle+1,right)
    return arr


    