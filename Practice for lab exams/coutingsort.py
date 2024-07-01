array=[10,15,14,13,11,20,19]

length=len(array)
sorted_array=[0]*(length)
largest=0
for i in range(length):
    if(array[i]>largest):
        largest=array[i]
print(largest)
counting_array=[0]*(largest+1)
prefix_sum=[0]*(largest+1)

for i in range(length):
    counting_array[array[i]]=counting_array[array[i]]+1
prefix_sum=counting_array.copy()
# #prefix_sum
for i in range(1,largest+1):
    prefix_sum[i]=prefix_sum[i] + prefix_sum[i-1]

for j in range(length-1,-1,-1):
    sorted_array[prefix_sum[array[j]]-1]=array[j]
    prefix_sum[array[j]]=prefix_sum[array[j]]-1

print(sorted_array)