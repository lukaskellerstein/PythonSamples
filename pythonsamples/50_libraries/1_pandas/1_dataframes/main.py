import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# DataFrames
# ----------------------------------------------------
# ----------------------------------------------------

labels = ["a", "b", "c"]

# -------------------------------
# Dictionary
# -------------------------------
my_df = pd.DataFrame({"a": [10, 20, 30], "b": [20, 40, 60], "c": [30, 60, 90]})
print(my_df)

# -------------------------------
# Numpy Array / Lists
# -------------------------------
my_df = pd.DataFrame(np.random.randn(3, 4), ["A", "B", "C"], ["W", "X", "Y", "Z"])
print(my_df)