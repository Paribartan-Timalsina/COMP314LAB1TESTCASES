# def heapify(array,i,n):
#     left=2*i+1
#     right=2*i+2
#     largest=i
#     if(left < n and array[left]>array[i] ):
#         largest=left
#     if(right < n and array[right]>array[largest] ):
#         largest=right
#     if(largest!=i):
#         array[largest],array[i]=array[i],array[largest]
#         heapify(array,largest,n)


# def build_max_heap(array):
#     for i in range(len(array)//2-1,-1,-1):
#         heapify(array,i,len(array))

# def heapsort(array):
#     build_max_heap(array)
#     for i in range(len(array)-1,0,-1):
#         array[i],array[0]=array[0],array[i]
#         heapify(array,0,i)
# array=[7,6,8,9,2,6,9,100,0,-23]
# heapsort(array)
# print(array)
def heapify(array,i,n):
    left=2*i+1
    right=2*i+2
    largest=i
    if(left < n and array[left]>array[largest]):
        largest=left
    if(right < n and array[right]>array[largest]):
        largest=right
    if(largest != i):
        array[i],array[largest]=array[largest],array[i]
        heapify(array,largest,n)
def build_max_heap(array):
    for i in range(len(array)//2-1,-1,-1):
        heapify(array,i,len(array))
def heapsort(array):
    build_max_heap(array)
    print(array)
    for i in range(len(array)-1,0,-1):
        array[0],array[i]=array[i],array[0]
        heapify(array,0,i)
array=[7,6,8,9,2,6,9,100,0,-23]
heapsort(array)
print(array)

