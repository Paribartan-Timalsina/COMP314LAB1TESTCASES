def bubblesort(array):
    length=len(array)
    for i in range(length-2):
        for j in range(length-1):
            if(array[j+1]<array[j]):
                array[j+1],array[j]=array[j],array[j+1]

array=[7,6,8,9,2,6,9,10]
bubblesort(array)
print(array)