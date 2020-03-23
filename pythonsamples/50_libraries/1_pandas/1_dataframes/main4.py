import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# DataFrames - operations
# ----------------------------------------------------
# ----------------------------------------------------
my_df = pd.DataFrame(np.random.randn(3, 4), ["A", "B", "C"], ["W", "X", "Y", "Z"])
print(my_df)

# ------------------------
# Conditional selection - DataFrame
# ------------------------
resultBooleans = my_df > 0
print(resultBooleans)

result_df = my_df[resultBooleans]
print(result_df)

# oneliner
print(my_df[my_df > 0])

# multiple conditions
print(my_df[(my_df > 0) & (my_df < 1)])  # and
print(my_df[(my_df > 0) | (my_df < 1)])  # or


# ------------------------
# Conditional selection - Columns
# ------------------------

res1 = my_df["W"] > 0
print(res1)

result_df = my_df[res1]
print(result_df)

# oneliner
print(my_df[my_df["W"] > 0])

# multiple conditions
print(my_df[(my_df["W"] > 0) & (my_df["W"] < 1)])  # and
print(my_df[(my_df["W"] > 0) | (my_df["W"] < 1)])  # or

