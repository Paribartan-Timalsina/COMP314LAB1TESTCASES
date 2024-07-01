def bucket_sort(a):
    # Normalize the array
    a = [x / 100 for x in a]
    
    n = len(a)
    global_array = [[] for _ in range(n)]
    b = []

    # Distribute the elements into buckets
    for value in a:
        index = int(n * value)
        global_array[index].append(value)

    # Sort each bucket and collect the results
    for bucket in global_array:
        bucket.sort()
        b.extend(bucket)

    # Rescale the values to original
    b = [x * 100 for x in b]

    print("Sorted array:", b)
    print("Buckets:", global_array)

# Test case
a = [78, 17, 39, 26, 72, 94, 21, 12, 23, 68]
bucket_sort(a)
