# Defines a function named `selection_sort` that accepts a list `arr` as its argument.
def selection_sort(arr:list):
    # Loops through each index of the list except the last one.
    for i in range(len(arr)):
        # Initially assumes the smallest element is at the current position `i`.
        smallest = i
        # Inner loop to find the index of the smallest element in the remaining unsorted part of the list.
        for j in range(i+1, len(arr)):
            # If a smaller element is found, update the `smallest` with the new index.
            if arr[j] < arr[smallest]:
                smallest = j
        # Swaps the smallest found element with the element at the current position `i`.
        temp = arr[smallest]  # Temporary storage for the element at index `smallest`.
        arr[smallest] = arr[i]  # Places the current element at the `smallest` position.
        arr[i] = temp  # Moves the smallest element found to the current position.
    
    # Returns the sorted list after iterating through all elements.
    return arr
