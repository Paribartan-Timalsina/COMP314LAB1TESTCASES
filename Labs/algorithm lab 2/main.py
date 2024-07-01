import random
import time
import matplotlib.pyplot as plt
from src.insertion_sort import insertion_sort
from src.selection_sort import selection_sort
from src.merge_sort import merge_sort
from src.quick_sort import quick_sort
import sys
sys.setrecursionlimit(2000000)

def quicksortBestCaseArray(arr, start_index = 0, end_index  = None):
    if end_index is None:
        end_index = len(arr) - 1

    if start_index >= end_index:
        return

    if (start_index == 0) and (end_index == (len(arr) - 1)):  # only sorting once
        arr.sort()

    median = (start_index + end_index) // 2

    i = median
    # moving the median to last index
    while i < end_index:
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        i += 1

    quicksortBestCaseArray(arr, start_index, median - 1)
    quicksortBestCaseArray(arr, median, end_index - 1)
    return arr

def mergesortWorstCase(arr,sort=True):
    n = len(arr)
    if n <= 1:
        return arr

    if n == 2:
        arr[0], arr[1] = arr[1], arr[0]
        return arr
    if sort:
        arr = sorted(arr)
    else:
        arr = arr.copy()
    left_arr = arr[::2]
    right_arr = arr[1::2]
    return mergesortWorstCase(left_arr,sort=False) + mergesortWorstCase(right_arr,sort=False)

# Function to generate a list of n random numbers within a specified range
def get_n_random(n: int):
    return [random.randint(-1000, 10000) for _ in range(n)]

# Main function to execute performance comparison of sorting algorithms
def main():
    # Initialize variables for the test
    total_test = 10000 # Total number of elements to test up to
    increment = 100  # Increment for each test

    # Lists to store time differences for each sorting scenario
    select_diff, insert_diff, insert_diff_best, insert_diff_worst = [], [], [], []
    quick_diff, quick_diff_worst, merge_diff, merge_diff_best, merge_diff_worst,quick_diff_best = [], [], [], [], [],[]
    number = []  # List to store the number of elements sorted in each test

    # Loop to test sorting algorithms with different sizes of data
    for i in range(10, total_test, increment):
        random_array = get_n_random(i)  # Generate a random array

        try:
            # Selection Sort
            selection_start = time.time_ns()
            selection_sort(random_array.copy())
            selection_end = time.time_ns()

            # Insertion Sort
            insertion_start = time.time_ns()
            insertion_sorted = insertion_sort(random_array.copy())
            insertion_end = time.time_ns()

            # Insertion Sort Best Case (already sorted array)
            insertion_start_best = time.time_ns()
            insertion_sort(insertion_sorted.copy())
            insertion_end_best = time.time_ns()

            # Insertion Sort Worst Case (reverse sorted array)
            insertion_sorted_reverse = insertion_sorted[::-1]
            insertion_start_worst = time.time_ns()
            insertion_sort(insertion_sorted_reverse.copy())
            insertion_end_worst = time.time_ns()

            # Merge Sort
            merge_start = time.time_ns()
            merge_sorted = merge_sort(random_array.copy(), 0, len(random_array) - 1)
            merge_end = time.time_ns()

            # Quick Sort
            quick_start = time.time_ns()
            quick_sorted = quick_sort(random_array.copy(), 0, len(random_array) - 1)
            quick_end = time.time_ns()

            # Quick Sort Worst Case (reverse sorted array)
            quick_start_worst = time.time_ns()
            quick_sort(quick_sorted, 0, len(quick_sorted) - 1)
            quick_end_worst = time.time_ns()


            # Quick Sort Best Case 
            quick_sorted_best_case = quicksortBestCaseArray(random_array.copy())
            quick_start_best = time.time_ns()
            quick_sort(quick_sorted_best_case, 0, len(quick_sorted_best_case) - 1)
            quick_end_best = time.time_ns()

            # Merge Sort Best Case (already sorted array)
            merge_start_best = time.time_ns()
            merge_sort(merge_sorted.copy(), 0, len(merge_sorted) - 1)
            merge_end_best = time.time_ns()

            # Merge Sort Worst Case (reverse sorted array)
            merge_sorted_worst_case_array = mergesortWorstCase(random_array.copy())
            merge_start_worst = time.time_ns()
            merge_sort(merge_sorted_worst_case_array.copy(), 0, len(merge_sorted_worst_case_array) - 1)
            merge_end_worst = time.time_ns()

            # Record the time differences for each scenario
            select_diff.append((selection_end - selection_start) * 1e-6)
            insert_diff.append((insertion_end - insertion_start) * 1e-6)
            insert_diff_best.append((insertion_end_best - insertion_start_best) * 1e-6)
            insert_diff_worst.append((insertion_end_worst - insertion_start_worst) * 1e-6)
            merge_diff.append((merge_end - merge_start) * 1e-6)
            quick_diff.append((quick_end - quick_start) * 1e-6)
            merge_diff_best.append((merge_end_best - merge_start_best) * 1e-6)
            merge_diff_worst.append((merge_end_worst - merge_start_worst) * 1e-6)
            quick_diff_worst.append((quick_end_worst - quick_start_worst) * 1e-6)
            quick_diff_best.append((quick_end_best - quick_start_best) * 1e-6)
            number.append(i)  # Record the number of elements sorted

        except Exception as e:
            print(f"An error occurred at {i} elements: {e}")

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    axes[0, 0].plot(number, select_diff, label="Selection Sort")
    axes[0, 0].plot(number, insert_diff, label="Insertion Sort")
    axes[0, 0].plot(number, insert_diff_best, label="Insertion Sort Best")
    axes[0, 0].plot(number, insert_diff_worst, label="Insertion Sort Worst")
    axes[0, 0].legend(loc="upper left")
    axes[0, 0].set_xlabel("Number of elements")
    axes[0, 0].set_ylabel("Time (milliseconds)")
    axes[0, 0].set_title("Insertion and Selection Sorts")
    axes[0, 0].grid(True)

    axes[0, 1].plot(number, quick_diff, label="Quick Sort")
    axes[0, 1].plot(number, merge_diff, label="Merge Sort")
    axes[0, 1].legend(loc="upper left")
    axes[0, 1].set_xlabel("Number of elements")
    axes[0, 1].set_ylabel("Time (milliseconds)")
    axes[0, 1].set_title("Quick and Merge Sorts")
    axes[0, 1].grid(True)

    axes[1, 0].plot(number, merge_diff_worst, label="Merge Sort Worst")
    axes[1, 0].plot(number, quick_diff_worst, label="Quick Sort Worst")
    axes[1, 0].legend(loc="upper left")
    axes[1, 0].set_xlabel("Number of elements")
    axes[1, 0].set_ylabel("Time (milliseconds)")
    axes[1, 0].set_title("Merge and Quick Sorts (Worst Case)")
    axes[1, 0].grid(True)

    axes[1, 1].plot(number, merge_diff_best, label="Merge Sort Best")
    axes[1, 1].plot(number, quick_diff_best, label="Quick Sort Best")
    axes[1, 1].legend(loc="upper left")
    axes[1, 1].set_xlabel("Number of elements")
    axes[1, 1].set_ylabel("Time (milliseconds)")
    axes[1, 1].set_title("Merge and Quick Sorts (Best Case)")
    axes[1, 1].grid(True)

    plt.tight_layout()
    plt.show()
# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
