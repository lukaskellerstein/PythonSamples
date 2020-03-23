import numpy as np

# ----------------------------------------------------
# ----------------------------------------------------
# Arrays
# ----------------------------------------------------
# ----------------------------------------------------

my_list = np.random.randn(20)
print(my_list)


# ----------------------------------------------------
# Copy array to a new instance
# ----------------------------------------------------

my_list2 = my_list.copy()
print(my_list2)


# some change in first array
my_list = [1, 2, 3]
print(my_list)

# copied list is untouched
print(my_list2)
