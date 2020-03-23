import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# DataFrames
# ----------------------------------------------------
# ----------------------------------------------------
my_df = pd.DataFrame(np.random.randn(3, 4), ["A", "B", "C"], ["W", "X", "Y", "Z"])
print(my_df)


# ----------------------------------------------------
# Get data - column - by column name
# ----------------------------------------------------
col1 = my_df["X"]
print(type(col1))
print(col1)

# multiple columns at once
cols1 = my_df[["X", "Y"]]
print(type(cols1))
print(cols1)

# ----------------------------------------------------
# Get data - row
# ----------------------------------------------------

# by key
row1 = my_df.loc["A"]
print(type(row1))
print(row1)

# by index
row2 = my_df.iloc[0]
print(type(row2))
print(row2)


# ----------------------------------------------------
# Get data - cell
# ----------------------------------------------------

# by key
cell1 = my_df.loc["A", "Z"]
print(type(cell1))
print(cell1)


# ----------------------------------------------------
# Get data - sub dataframe
# ----------------------------------------------------

# by key
subdf1 = my_df.loc[["A", "B"], ["X", "Y", "Z"]]
print(type(subdf1))
print(subdf1)

# ----------------------------------------------------
# Delete column
# ----------------------------------------------------
new_df1 = my_df.drop("Z", axis=1)  # same as .drop("Z", axis=0)
print(new_df1)

# or to take affect on origin datafram
my_df.drop("W", axis=1, inplace=True)
print(my_df)

# ----------------------------------------------------
# Delete row
# ----------------------------------------------------
new_df2 = my_df.drop("B", axis=0)
print(new_df2)


# ----------------------------------------------------
# Apply function (to each item)
# ----------------------------------------------------
bbb = my_df["X"].apply(lambda x: x * x)
print(bbb)
