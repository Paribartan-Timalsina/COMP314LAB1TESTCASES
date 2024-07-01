
# Define a list of profits and weights for each item
profit = [20, 30, 40, 50]
weights = [5, 10, 15, 20]

# Define the capacity of the knapsack
capacity = 30

# Function to convert a decimal number to binary
def convert_to_binary(num):
    binary_str = ""
    # Loop to build the binary representation of the number
    while num > 0:
        # Add the remainder of num divided by 2 to the binary string
        binary_str = str(num % 2) + binary_str
        # Update num to be the quotient of num divided by 2
        num = num // 2
    return binary_str

# Function to find the maximum profit using a brute-force approach
def bruteforce(capacity, length, profit, weights):
    max_profit = 0
    # Calculate the total number of possible combinations (2^length)
    total_combinations = pow(2, length)
    result = []  # Initialize result list
    # Iterate through each combination
    for i in range(total_combinations):
        # Convert the current combination index to binary
        binary_value = convert_to_binary(i)
        # Pad the binary string with leading zeros to match the length of the item list
        binary_value = binary_value.zfill(length)  
        
        current_profit = 0
        current_weight = 0
        # Iterate through each bit in the binary string
        for j in range(len(binary_value)):
            # If the bit is 1, include the corresponding item

            if binary_value[j] == "1" and weights[j]<capacity:
                current_profit += profit[j]
                current_weight += weights[j]
        # Check if the current combination is valid and if it has a higher profit than the max profit found so far
        if current_weight <= capacity and current_profit > max_profit:
            max_profit = current_profit


            # Create a list with each character enclosed in quotes
            result = [f'{char}' for char in binary_value]
    return max_profit, result

# # Calculate the maximum profit
# max_profit,combination = bruteforce(capacity, len(profit), profit, weights)
# print("Maximum Profit:", max_profit)
# print("Combination:", combination)




