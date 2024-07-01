import math
from src.merge import merge
def merge_sort(arr:list,left,right):
    if(left<right):
        middle = math.floor(left + (right - left) / 2)
        
        merge_sort(arr, left, middle)
        merge_sort(arr, middle + 1, right)

        merge(arr, left, middle, right)
    return arr





