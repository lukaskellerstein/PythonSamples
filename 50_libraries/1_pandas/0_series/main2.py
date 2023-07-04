import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# Series - operations
# ----------------------------------------------------
# ----------------------------------------------------
keys1 = ["Subaru", "Audi", "Bmw"]
my_arr1 = np.array([160, 200, 300])
series1 = pd.Series(my_arr1, index=keys1)
print(series1)

keys2 = ["Subaru", "Bugatti", "Ferrari", "Porsche"]
my_arr2 = np.array([300, 1000, 750, 660])
series2 = pd.Series(my_arr2, index=keys2)
print(series1)


# Addition (+) - will sum only the values for the same keys in both series
res1 = series1 + series2
print(res1)

# Subtraction (-)
res2 = series1 - series2
print(res2)

# Multiplication (*)
res3 = series1 * 2
print(res3)

# Division (/)
res3 = series1 / 2
print(res3)

# Exponentiation - umocneni
res6 = series1 ** 2
print(res6)

