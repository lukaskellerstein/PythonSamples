# --------------------------------------------------------------------
#
# Numpy is numerical library for Python
#
# - allows extremely fast data generation and handling !!!!!
# - using Numpy Arrays are more efficient for data handling than normal Python List !!!!!
#
# --------------------------------------------------------------------
import numpy as np

# ----------------------------------------------------
# Matrix
# ----------------------------------------------------

# slow matrix
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(type(my_matrix))
print(my_matrix)

# fast matrix ---------> numpy matrix/array
matrix = np.array(my_matrix)
print(type(matrix))
print(matrix)

