# import sys

# def matrix_multiply_tabu(p0, n, array, sarray):
#     # Initialize the array with 0 for the diagonal and infinity for other entries
#     for i in range(1, n+1):
#         for j in range(1, n+1):
#             if i == j:
#                 array[i][j] = 0
#             else:
#                 array[i][j] = float('inf')

#     # Fill the array using tabulation
#     for d in range(1, n):
#         for i in range(1, n-d+1):
#             j = i + d
#             for k in range(i, j):
#                 cost = array[i][k] + array[k+1][j] + p0[i-1] * p0[k] * p0[j]
#                 if cost < array[i][j]:
#                     array[i][j] = cost
#                     sarray[i][j] = k

# def print_optimal_parenthesis(sarray, i, j):
#     if i == j:
#         print(f"A{i}", end="")
#     else:
#         print("(", end="")
#         print_optimal_parenthesis(sarray, i, sarray[i][j])
#         print_optimal_parenthesis(sarray, sarray[i][j] + 1, j)
#         print(")", end="")

# # Define the dimensions of matrices
# p0 = [5, 4, 6, 2, 7]
# n = len(p0) - 1

# # Initialize the array and sarray to appropriate size
# array = [[0 for _ in range(n+1)] for _ in range(n+1)]
# sarray = [[0 for _ in range(n+1)] for _ in range(n+1)]

# # Call the function
# matrix_multiply_tabu(p0, n, array, sarray)

# # Print the result
# print(f"Minimum number of multiplications: {array[1][n]}")
# print("Optimal parenthesization: ", end="")
# print_optimal_parenthesis(sarray, 1, n)
# print()  # For newline after the parenthesization


def matrix_multiplication_tabu(p0):
    length=len(p0)
    array = [[0 for _ in range(length)] for _ in range(length)]
    for i in range(len(p0)):
        for j in range(len(p0)):
            if(i==j):
                array[i][j]=0
            else:
                array[i][j]=float("inf")
    
    for d in range(1,len(p0)-1):
        for i in range(1,len(p0)-1-d+1):
            j=i+d
            for k in range(i,j):
                value=array[i][k]+array[k+1][j]+p0[i-1]*p0[k]*p0[j]
                if(value<array[i][j]):
                    array[i][j]=value
    print(array)
p0 = [5, 4, 6, 2, 7]
matrix_multiplication_tabu(p0)


    