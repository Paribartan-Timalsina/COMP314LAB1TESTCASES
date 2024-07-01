def greedy_knapsack(profit, weights, capacity, factor):
    combination_array = ["0"] * len(profit)  # Initialize combination array to store item inclusion
    current_profit = 0  # Initialize current profit to 0
    sorted_factor = sorted(factor, reverse=True)  # Sort the factor array in descending order

    # Iterate through each sorted factor
    for i in range(len(sorted_factor)):
        # Iterate through each item
        for j in range(len(weights)):
            # If the item has the current sorted factor and there is remaining capacity
            if (profit[j] / weights[j] == sorted_factor[i] and capacity > 0):
                # If the item can fit in the remaining capacity
                if (weights[j] <= capacity):
                    current_profit = current_profit + profit[j]  # Add item's profit to current profit
                    capacity = capacity - weights[j]  # Reduce the remaining capacity
                    combination_array[j] = "1"  # Mark the item as fully included
                else:
                    # If the item can't fit fully, include the fractional part
                    current_profit = current_profit + (capacity * profit[j] / weights[j])  # Add fractional profit
                    combination_array[j] = capacity / weights[j]  # Mark the fraction of the item included
                    capacity = 0  # No capacity left
                
                profit[j] = 0  # Mark the item as used

    return current_profit, combination_array  # Return the maximum profit and the combination array

# # Example Usage
# profit = [50, 100, 150, 200]
# weights = [8, 16, 32, 40]
# capacity = 65
# factor = []

# # Calculate profit-to-weight ratio for each item
# for i in range(len(profit)):
#     factor.append(profit[i] / weights[i])

# # Get the maximum profit and combination of items
# max_profit, combination_array = greedy_knapsack(profit, weights, capacity, factor)
# print("Maximum Profit:", max_profit)
# print("Combination:", combination_array)
