import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# Series
# ----------------------------------------------------
# ----------------------------------------------------

labels = ["a", "b", "c"]

# -------------------------------
# List
# -------------------------------
my_list = [10, 20, 30]
series1 = pd.Series(my_list, index=labels)
print(series1)

# -------------------------------
# Dictionary
# -------------------------------
my_dict = {"a": 10, "b": 20, "c": 30}
series2 = pd.Series(my_dict)
print(series2)

# -------------------------------
# Numpy Array
# -------------------------------
my_arr = np.array([10, 20, 30])
series2 = pd.Series(my_arr, index=labels)
print(series2)