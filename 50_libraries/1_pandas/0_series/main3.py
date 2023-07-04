import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# Series - indexing
# ----------------------------------------------------
# ----------------------------------------------------
keys1 = ["Subaru", "Audi", "Bmw", "Mecedes", "Lamborghini", "Porsche"]
my_arr1 = np.array([160, 200, 300, 400, 500, 450])
series1 = pd.Series(my_arr1, index=keys1)
print(series1)


# ------------------------
# select by index
# ------------------------
res1 = series1[3:5]
print(res1)

res2 = series1[2:]
print(res2)

res3 = series1[:2]
print(res3)


# ------------------------
# change by index
# ------------------------

series1[3:5] = 100
print(series1)

