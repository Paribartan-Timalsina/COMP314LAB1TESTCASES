import unittest
import random
# def initialize_globals():
#     global x, solution_found
#     x = [[0 for _ in range(4)] for _ in range(4)]
#     solution_found = False
x = [[0 for _ in range(4)] for _ in range(4)]
solution_found = False
def place(k, i):
    for j in range(k):
        if x[j][i] == 1:
            return False
    m, n = k, i
    while m >= 0 and n >= 0:
        if x[m][n] == 1:
            return False
        m -= 1
        n -= 1
    m, n = k, i
    while m >= 0 and n < 4:
        if x[m][n] == 1:
            return False
        m -= 1
        n += 1
    return True

def n_queens(k, n):
    global solution_found
    if solution_found:
        return None
    for i in range(100):
        random_number=random.randint(0,100)%n
        if place(k, random_number):
            x[k][random_number] = 1
            if k == n - 1:
                solution_found = True
                return [row[:] for row in x]
            else:
                result = n_queens(k + 1, n)
                if result is not None:
                    return result
            x[k][random_number] = 0
    return None

print(n_queens(0,4))

# # Unit testing
# class MyTest(unittest.TestCase):
#     def test_nqueens(self):
#         initialize_globals()
#         expected = [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]
#         self.assertListEqual(n_queens(0, 4), expected)

# if __name__ == "__main__":
#     unittest.main()
 