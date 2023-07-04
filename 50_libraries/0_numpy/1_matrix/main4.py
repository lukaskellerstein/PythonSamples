import numpy as np

# ----------------------------------------------------
# ----------------------------------------------------
# Matrix - OPERATIONS
# ----------------------------------------------------
# ----------------------------------------------------

my_list = np.random.randn(30)
my_matrix = my_list.reshape(6, 5)
print(my_matrix)


# ----------------------------------------------------
# Sum
# ----------------------------------------------------

print(my_matrix.sum(axis=1))  # sum for each row
print(my_matrix.sum(axis=0))  # sum for each column


# ----------------------------------------------------
# Cumulative Sum
# ----------------------------------------------------

print(my_matrix.cumsum(axis=1))  # sum for each row
print(my_matrix.cumsum(axis=0))  # sum for each column

# ----------------------------------------------------
# Min, Max
# ----------------------------------------------------

print(my_matrix.min(axis=1))  # minimal value for each row
print(my_matrix.argmin(axis=1))  # index of minimal value for each row

print(my_matrix.min(axis=0))  # minimal value for each column
print(my_matrix.argmin(axis=0))  # index of minimal value for each column

print(my_matrix.max(axis=1))  # maximal value for each row
print(my_matrix.argmax(axis=1))  # index of maximum value for each row

print(my_matrix.max(axis=0))  # maximal value for each column
print(my_matrix.argmax(axis=0))  # index of maximum value for each column

# ----------------------------------------------------
# Avg
# ----------------------------------------------------

# The mean or average is (1+1+2+3+4)/5 = 2.2
# The median is "2" (the central value).
# The mode is "1" (it occurs most often).
# The midrange is (4+1)/2 = 2.5

print(np.mean(my_matrix, axis=1))  # arithmetic average for each row
print(np.average(my_matrix, axis=1))  # weighted average (default weight = 1) for each row
print(np.median(my_matrix, axis=1)  # median for each row

print(np.mean(my_matrix, axis=0))  # arithmetic average for each column
print(np.average(my_matrix, axis=0))  # weighted average (default weight = 1) for each column
print(np.median(my_matrix, axis=0)  # median for each column

# ----------------------------------------------------
# Variance
# ----------------------------------------------------
print(np.var(my_matrix, axis=1))  # variantion for each row
print(np.var(my_matrix, axis=0))  # variantion for each column

# ----------------------------------------------------
# Standard deviation
# ----------------------------------------------------
print(np.std(my_matrix, axis=1))  # stddev for each row
print(np.std(my_matrix, axis=0))  # stddev for each column
