import sys

# Initialize the memoization and split point arrays
def initialize_arrays(n):
    m_array = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    split = [[-1 for _ in range(n+1)] for _ in range(n+1)]
    return m_array, split

def matrix_multiplication(p0, i, j, m_array, split):
    if i == j:
        return 0
    if m_array[i][j] != -1:
        return m_array[i][j]
    m_array[i][j] = sys.maxsize
    for k in range(i, j):
        cost = matrix_multiplication(p0, i, k, m_array, split) + matrix_multiplication(p0, k+1, j, m_array, split) + p0[i-1] * p0[k] * p0[j]
        if cost < m_array[i][j]:
            m_array[i][j] = cost
            split[i][j] = k
    return m_array[i][j]

def print_optimal_parenthesis(split, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesis(split, i, split[i][j])
        print_optimal_parenthesis(split, split[i][j] + 1, j)
        print(")", end="")

    #this is the noob method of solving yet to be refined
    # index_array=[]
    # parentesie_array=[1,2,3,4]

    # for k in range(len(split[0])):
    #     index_array.append(split[1][k])
    # print(index_array)
    # for i in range(j,1,-1):
    #     print(split[1][i])
    #     value=split[1][i]
    #     needed_value=i
    #     parentesie_array.insert(0,"(")
    #     index2=parentesie_array.index(i)
    #     parentesie_array.insert(index2+1,")")
    #     index=parentesie_array.index(value)
    #     parentesie_array.insert(index+1,")")
    #     parentesie_array.insert(index+2,"(")
    # print(parentesie_array)






# Define the dimensions of matrices
p0 = [5, 4, 6, 2, 7]
n = len(p0) - 1

# Initialize m_array and split arrays to appropriate size
m_array, split = initialize_arrays(n)

# Call the function and print the result
min_cost = matrix_multiplication(p0, 1, n, m_array, split)
print(f"Minimum number of multiplications: {min_cost}")
print("Optimal parenthesization: ", end="")
print_optimal_parenthesis(split, 1, n)
