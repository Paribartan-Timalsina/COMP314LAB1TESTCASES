profit = [50, 100, 150, 200]
weights = [8, 16, 32, 40]
m = 64
n = len(profit)
#HERE 
# m is the TOTAL CAPACITY
# n is the number of objects
def dynamic_ks(n, m, profit, weights,array):
    # Base case: If there are no items or capacity is 0, the profit is 0
    if n == 0 or m == 0:
        return 0
    
    # If the value is already computed, return it to save computation time (Memoization)
    if array[n][m] != -1:
        return array[n][m]
    
    # If the weight of the nth item is more than the current capacity, skip this item
    if weights[n-1] > m:
        array[n][m] = dynamic_ks(n-1, m, profit, weights, array)
    else:
        # Otherwise, find the maximum value by either including or excluding the nth item
        # Include the item: profit of nth item + result of remaining capacity and remaining items
        # Exclude the item: result of remaining capacity with the same items
        array[n][m] = max(profit[n-1] + dynamic_ks(n-1, m-weights[n-1], profit, weights, array), 
                          dynamic_ks(n-1, m, profit, weights, array))
    
    # Store the computed value in the array and return it
    return array[n][m]

def dynamic_knapsack(n, m, profit, weights):
    # Create a 2D array initialized to -1 to store intermediate results
    array = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    
    # Compute the maximum value that can be obtained with given items and capacity
    maximum_value = dynamic_ks(n, m, profit, weights, array)
    
    return maximum_value






# print(f"Maximum Profit: {dynamic_knapsack(n, m, profit, weights)}")

