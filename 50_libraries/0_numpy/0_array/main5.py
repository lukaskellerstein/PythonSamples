import numpy as np

# ----------------------------------------------------
# ----------------------------------------------------
# Arrays - operations
# ----------------------------------------------------
# ----------------------------------------------------

my_list = np.arange(10)
print(my_list)

# Addition (+)
res1 = my_list + my_list
print(res1)

# Subtraction (-)
res2 = res1 - my_list
print(res2)

# Multiplication (*)
res3 = my_list * 10
print(res3)

# Division (/)
res4 = res3 / 5
print(res4)

res5 = 1 / res3
print(res5)

# Exponentiation - umocneni
res6 = my_list ** 2
print(res6)

res7 = np.exp2(my_list)
print(res7)


# Root - odmocneni
res8 = np.sqrt(my_list)
print(res8)
