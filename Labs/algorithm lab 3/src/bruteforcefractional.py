def fractional_knapsack(item_weights, item_profits, max_capacity):
    num_items = len(item_weights)  # Number of items
    optimal_combination = [0] * num_items  # To store the best combination of items
    max_profit = 0.0  # Initialize the maximum profit to 0

    total_combinations = 2 ** num_items  # Total possible combinations (2^num_items)

    # Iterate through all possible combinations
    for combination in range(total_combinations):
        current_combination = [0] * num_items  # To store the current combination of items
        current_profit = 0.0  # Profit for the current combination
        current_capacity = max_capacity  # Remaining capacity of the knapsack
        comb_num = combination  # Current combination number

        # Iterate through each item to check if it's included in the current combination
        for index in range(num_items):
            binary_choice = comb_num % 2  # Determine if the item is included (1) or not (0)
            comb_num = comb_num // 2  # Move to the next item

            # If the item is included in the current combination
            if binary_choice == 1:
                # Check if the item can fit in the remaining capacity
                if item_weights[index] <= current_capacity:
                    current_combination[index] = 1  # Mark the item as included
                    current_profit += item_profits[index]  # Add the item's profit to the current profit
                    current_capacity -= item_weights[index]  # Decrease the remaining capacity

        # If there's space left in the knapsack, consider fractional weights
        if current_capacity > 0:
            best_fractional_combination = current_combination[:]  # Copy the current combination
            best_fractional_profit = current_profit  # Copy the current profit

            # Iterate through each item to check for fractional inclusion
            for index in range(num_items):
                if current_combination[index] == 0:  # If the item is not already included
                    fraction = min(1, current_capacity / item_weights[index])  # Determine the fraction of the item that can fit
                    potential_profit = current_profit + fraction * item_profits[index]  # Calculate the potential profit with the fractional item

                    # Update the best fractional profit and combination if this combination is better
                    if potential_profit > best_fractional_profit:
                        best_fractional_profit = potential_profit
                        best_fractional_combination = current_combination[:]
                        best_fractional_combination[index] = fraction

            current_combination = best_fractional_combination  # Update the current combination with the best fractional combination
            current_profit = best_fractional_profit  # Update the current profit with the best fractional profit
            current_capacity = 0  # No capacity left

        # Update the maximum profit and optimal combination if the current profit is higher
        if current_profit > max_profit:
            optimal_combination = current_combination[:]
            max_profit = current_profit

    return max_profit, optimal_combination  # Return the maximum profit and the optimal combination of items

# weights = [10, 20, 30]
# profit = [60, 100, 120]
# capacity = 50
# max_profit, optimal_combination = fractional_knapsack(weights, profit, capacity)
# print("Maximum Profit:", max_profit)
# print("Combination:", optimal_combination)
