import numpy as np

# ----------------------------------------------------
# ----------------------------------------------------
# Arrays
# ----------------------------------------------------
# ----------------------------------------------------
my_list = np.random.randn(20)
print(my_list)

# ------------------------
# Conditional selection
# ------------------------
resultBooleans = my_list > 0
print(resultBooleans)

resultArr = my_list[resultBooleans]
print(resultArr)


# oneliner
print(my_list[my_list > 0])
