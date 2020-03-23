import numpy as np


# ----------------------------------------------------
# ----------------------------------------------------
# Matrix
# ----------------------------------------------------
# ----------------------------------------------------

my_list = np.random.randn(30)
my_matrix = my_list.reshape(6, 5)
print(my_matrix)


# ----------------------------------------------------
# Append a value (COLUMN) to the matrix
# ----------------------------------------------------

newArr1 = np.append(my_matrix, [[94], [95], [96], [97], [98], [99]], axis=1)
print(newArr1)


# ----------------------------------------------------
# Append a value (ROW) to the matrix
# ----------------------------------------------------

newArr = np.append(my_matrix, [[0, 0, 0, 0, 0]], axis=0)
print(newArr)


# ----------------------------------------------------
# Delete a value (COLUMN) from the matrix (At the index)
# ----------------------------------------------------
newArr = np.delete(my_matrix, 1, axis=1)
print(newArr)


# ----------------------------------------------------
# Delete a value (ROW) from the matrix (At the index)
# ----------------------------------------------------
newArr = np.delete(my_matrix, 1, axis=0)
print(newArr)


# ----------------------------------------------------
# Find a value in the array
# ----------------------------------------------------
rows, cols = np.where(newArr1 == 99)
print("where")
print(rows)
print(newArr1[rows])
print(cols)
print(newArr1[cols])

