import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# DataFrames - multi-level index
# ----------------------------------------------------
# ----------------------------------------------------
outside = ["G1", "G1", "G1", "G2", "G2", "G2"]
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(np.random.randn(6, 2), hier_index, ["A", "B"])

print(df)


# ----------------------------------------------------
# Get data - row
# ----------------------------------------------------

row1 = df.loc["G1"]
print(row1)

# multi-level selection
row2 = df.loc["G1"].loc[1]
print(row2)

# select cell
cell1 = df.loc["G1"].loc[1]["B"]
print(cell1)

# cross selection
rows1 = df.xs(1, level=1)
print(rows1)
