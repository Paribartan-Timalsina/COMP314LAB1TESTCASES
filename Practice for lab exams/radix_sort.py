main_array=[2,712,635,988,129,212,600,991,123,20,1,45,123]
def counting_sort(array):
    length = len(array)
    global main_array
    # Step 1: Find the largest element in the array
    largest = 0
    for i in range(length):
        if array[i] > largest:
            largest = array[i]
    
    # Step 2: Initialize counting_array, prefix_sum, and sorted_array
    counting_array = [0] * (largest + 1)
    prefix_sum = [0] * (largest + 1)
    sorted_array = [0] * length
    
    # Step 3: Count frequencies of each element in counting_array
    for i in range(length):
        counting_array[array[i]] += 1
    
    
    # Step 4: Calculate prefix sums in prefix_sum
    prefix_sum = counting_array.copy()
    for i in range(1, largest + 1):
        prefix_sum[i] += prefix_sum[i - 1]
    
    # Step 5: Place elements in sorted order using prefix_sum
    for j in range(length-1, -1, -1):
        sorted_array[prefix_sum[array[j]]-1] = main_array[j]
        prefix_sum[array[j]] -= 1
    main_array=sorted_array
    return sorted_array



first_place=[]
todividenumber=1
for i in range(3):
    for element in main_array:
        # element=str(element).zfill(3)
        # element=int(element)

        value=(element//todividenumber)%10
        first_place.append(value)
        print(first_place)
    print(counting_sort(first_place))
    first_place.clear()
    todividenumber=todividenumber*10













