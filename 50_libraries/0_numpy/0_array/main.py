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
# Arrays
# ----------------------------------------------------

# slow list
my_list = [1, 2, 3]
print(type(my_list))
print(my_list)

# very fast array ---------> numpy array
arr = np.array(my_list)
print(type(arr))
print(arr)


# slow range
my_range = list(range(0, 5))
print(type(my_range))
print(my_range)

# fast range ---------> numpy range
rng = np.arange(0, 5)
print(type(rng))
print(rng)
