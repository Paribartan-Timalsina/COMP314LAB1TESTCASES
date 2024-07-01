import random
import math
import matplotlib.pyplot as plt
import time
def insertionsort(array):
    length=len(array)
    for i in range(1,length):
        key=i-1
        number=array[i]
        while(key >=0 and number < array[key]):
            array[key+1]=array[key]
            key=key-1
            
        array[key+1]=number
    return array


def generate_random_array(number):
    array=[]
    for j in range(number):
        array.append(random.randint(-1000,1000))
    return array

insertion_diff=[]
number=[]
insertion_diff_best=[]
for i in range(100,5000,50):
    number.append(i)
    array=generate_random_array(i)
    start_time=time.time_ns()
    sorted_array=insertionsort(array)
    end_time=time.time_ns()
    insertion_diff.append((end_time-start_time))

    start_time_best=time.time_ns()
    insertionsort(sorted_array)
    end_time_best=time.time_ns()
    insertion_diff_best.append((end_time_best-start_time_best))

fig, ax = plt.subplots(figsize=(16, 12))
ax.plot(number,insertion_diff,label="Insertion diff")
ax.plot(number,insertion_diff_best,label="Insertion diff best")
plt.tight_layout()
plt.show()
