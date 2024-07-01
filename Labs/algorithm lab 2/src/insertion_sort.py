# Defines a function named `insertion_sort` that takes a list named `arr` as its parameter.
def insertion_sort(arr:list):
    # Iterates over each element in the list by its index.
    for i in range(len(arr)):
        # Initializes `j` to the index immediately before the current index `i`.
        j = i-1
        # Stores the value of the current element in a variable named `key`.
        key = arr[i]
        # Moves elements of `arr[0..i-1]`, that are greater than `key`, to one position ahead
        # of their current position. This loop continues as long as `j` is not negative
        # and the element at index `j` is greater than `key`.
        while(j >= 0 and arr[j] > key):
            arr[j+1] = arr[j]  # Moves the element at index `j` to the right.
            j = j-1  # Decreases `j` by 1 to move left through the list.
        
        # After finding the correct position for `key`, it is inserted.
        arr[j+1] = key
    
    # Once the entire list has been iterated over, the now-sorted list is returned.
    return arr
