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
# Add row
# ----------------------------------------------------

my_df.loc["D"] = [0, 0, 0, 0]
print(my_df)

# is row exist?
print("D" in my_df.index)
print("E" in my_df.index)
# or
print((my_df.index == "entry").any())


# ----------------------------------------------------
# Add column
# ----------------------------------------------------
my_df["Z0"] = [0, 0, 0, 0]
print(my_df)

# is row exist?
print("Z0" in my_df.columns)
print("Z1" in my_df.columns)
# or
print((my_df.columns == "Z0").any())


# ----------------------------------------------------
# Update row
# ----------------------------------------------------
my_df.loc["D"] = [1, 1, 1, 1, 1]
print(my_df)


# ----------------------------------------------------
# Update column
# ----------------------------------------------------
my_df["Z0"] = [1, 1, 1, 1]
print(my_df)

# ----------------------------------------------------
# Update cell
# ----------------------------------------------------

my_df.loc["D", "Z"] = 44
print(my_df)

# ----------------------------------------------------
# Get data - column - by column name
# ----------------------------------------------------

# by key
col1 = my_df["X"]
print(type(col1))
print(col1)

# col1 = my_df["XXXXX"]

# by index
col2 = my_df.iloc[:, 1]
print(type(col2))
print(col2)

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


# First
firstRow = my_df.head(1)

# Last
lastRow = my_df.tail(1)

# ----------------------------------------------------
# Get data - cell
# ----------------------------------------------------

# by key
cell1 = my_df.loc["A", "Z"]
print(type(cell1))
print(cell1)

# by "index" location
cell1 = my_df.iloc[0, 0]
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
