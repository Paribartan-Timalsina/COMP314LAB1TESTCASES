import random
import time
import matplotlib.pyplot as plt
from src.insertion_sort import insertion_sort
from src.selection_sort import selection_sort


# Function to generate a list of n random numbers within a specified range
def get_n_random(n: int):
    return [random.randint(-1000, 10000) for _ in range(n)]


# Main function to execute performance comparison of sorting algorithms
def main():
    # Initialize variables for the test
    total_test = 5000  # Total number of elements to test up to
    increment = 100  # Increment for each test

    # Lists to store time differences for each sorting scenario
    select_diff, insert_diff, insert_diff_best, insert_diff_worst = [], [], [], []

    number = []  # List to store the number of elements sorted in each test

    # Loop to test sorting algorithms with different sizes of data
    for i in range(10, total_test + 1, increment):
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

            # Record the time differences for each scenario
            select_diff.append((selection_end - selection_start) * 1e-6)
            insert_diff.append((insertion_end - insertion_start) * 1e-6)
            insert_diff_best.append((insertion_end_best - insertion_start_best) * 1e-6)
            insert_diff_worst.append((insertion_end_worst - insertion_start_worst) * 1e-6)
            number.append(i)  # Record the number of elements sorted

        except Exception as e:
            print(f"An error occurred at {i} elements: {e}")

    fig, ax = plt.subplots(figsize=(16, 12))

    ax.plot(number, select_diff, label="Selection Sort")
    ax.plot(number, insert_diff, label="Insertion Sort")
    ax.plot(number, insert_diff_best, label="Insertion Sort Best")
    ax.plot(number, insert_diff_worst, label="Insertion Sort Worst")
    ax.legend(loc="upper left")
    ax.set_xlabel("Number of elements")
    ax.set_ylabel("Time (milliseconds)")
    ax.set_title("Insertion and Selection Sorts")
    ax.grid(True)

    plt.tight_layout()
    plt.show()


# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
