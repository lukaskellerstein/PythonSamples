import numpy as np

# ----------------------------------------------------
# ----------------------------------------------------
# Arrays - OPERATIONS
# ----------------------------------------------------
# ----------------------------------------------------


my_list = np.random.randn(20)
print(my_list)


# ----------------------------------------------------
# Sum
# ----------------------------------------------------

print(my_list.sum())


# ----------------------------------------------------
# Cumulative Sum
# ----------------------------------------------------

print(my_list.cumsum())

# ----------------------------------------------------
# Min, Max
# ----------------------------------------------------
print(my_list.min())  # minimal value
print(my_list.argmin())  # index of minimal value
print(my_list.max())  # maximal value
print(my_list.argmax())  # index of maximum value


# ----------------------------------------------------
# Avg
# ----------------------------------------------------

# The mean or average is (1+1+2+3+4)/5 = 2.2
# The median is "2" (the central value).
# The mode is "1" (it occurs most often).
# The midrange is (4+1)/2 = 2.5

print(np.mean(my_list))  # arithmetic average
print(np.average(my_list))  # weighted average (default weight = 1)
print(np.median(my_list))  # median


# ----------------------------------------------------
# Variance
# ----------------------------------------------------
print(np.var(my_list))


# ----------------------------------------------------
# Standard deviation
# ----------------------------------------------------
print(np.std(my_list))


# ----------------------------------------------------
# Reshape
#
# Arrays --> Matrix
#
# ----------------------------------------------------

my_list = np.arange(25)
print(my_list)

my_mtx = my_list.reshape(5, 5)
print(my_mtx)
