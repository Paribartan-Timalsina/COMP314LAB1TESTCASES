import unittest
import random
# def initialize_globals():
#     global x, solution_found
#     x = [[0 for _ in range(4)] for _ in range(4)]
#     solution_found = False
x = [[0 for _ in range(4)] for _ in range(4)]
solution_found = False
def place(row, i):
    for j in range(row):
        if x[j][i] == 1:
            return False
    m, n = row, i
    while m >= 0 and n >= 0:
        if x[m][n] == 1:
            return False
        m -= 1
        n -= 1
    m, n = row, i
    while m >= 0 and n < 4:
        if x[m][n] == 1:
            return False
        m -= 1
        n += 1
    return True

def n_queens(x,row, n):
    if row==n:
            return True
    for _ in range(n):
        random_number=random.randint(0,100)%n
        if place(row, random_number):
            x[row][random_number] = 1
            if (n_queens(x,row + 1, n)):
                return True
            x[row][random_number] = 0
    return False

n_queens(x,0,4)
print(x)

# # Unit testing
# class MyTest(unittest.TestCase):
#     def test_nqueens(self):
#         initialize_globals()
#         expected = [[0, 1, 0, 0], [0, 0, 0, 1], [1, 0, 0, 0], [0, 0, 1, 0]]
#         self.assertListEqual(n_queens(0, 4), expected)

# if __name__ == "__main__":
#     unittest.main()
 