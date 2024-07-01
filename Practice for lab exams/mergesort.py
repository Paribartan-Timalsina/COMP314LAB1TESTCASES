import sys
import matplotlib.pyplot as plt
import random
import time
def merge(array,left,mid,right):
    n1=mid-left+1
    n2=right-mid
    L=[0]*n1
    R=[0]*n2
    for i in range(n1):
        L[i]=array[i+left]
    for j in range(n2):
        R[j]=array[j+mid+1]
    L.append(sys.maxsize)
    R.append(sys.maxsize)
    i=0
    j=0
    for k in range(left,right+1):
        if(L[i] <= R[j]):
            array[k]=L[i]
            i=i+1
        elif(L[i]>R[j]):
            array[k]=R[j]
            j=j+1

def mergesort(array,left,right):
    if(left<right):
        mid=(right+left)//2
        mergesort(array,left,mid)
        mergesort(array,mid+1,right)
        merge(array,left,mid,right)



def generate_random_array(number_size):
    array=[]
    for i in range(number_size):
        array.append(random.randint(-1000,1000))
    return array

time_slice=[]
time_slice_reverse=[]
number=[]
for i in range(100,10000,100):
    number.append(i)
    array=generate_random_array(i)
    starttime=time.time_ns()
    mergesort(array,0,len(array)-1)
    endtime=time.time_ns()
    time_slice.append((endtime-starttime))
    reversed_array = array[::-1]
    starttime_reverse=time.time_ns()
    mergesort(reversed_array,0,len(array)-1)
    endtime_reverse=time.time_ns()
    time_slice_reverse.append((endtime_reverse-starttime_reverse))

fig, ax = plt.subplots(figsize=(5, 5))

ax.plot(number, time_slice, label="Merge Sort")
ax.plot(number, time_slice_reverse, label="Merge Sort Worst")
plt.tight_layout()
plt.show()
