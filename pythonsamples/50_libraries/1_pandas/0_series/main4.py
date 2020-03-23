import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# Series - operations
# ----------------------------------------------------
# ----------------------------------------------------
keys1 = ["Subaru", "Audi", "Bmw", "Mecedes", "Lamborghini", "Porsche"]
my_arr1 = np.array([160, 200, 300, 400, 500, 450])
series1 = pd.Series(my_arr1, index=keys1)
print(series1)

# ------------------------
# Conditional selection
# ------------------------
resultBooleans = series1 > 200
print(resultBooleans)

resultArr = series1[resultBooleans]
print(resultArr)


# oneliner
print(series1[series1 > 200])
