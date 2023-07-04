import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# DataFrames - missing data
# ----------------------------------------------------
# ----------------------------------------------------

d = {"A": [1, 2, np.nan], "B": [1, np.nan, np.nan], "C": [1, 2, 3]}
df = pd.DataFrame(d)
print(df)


# ------------------------
# Remove NaN rows
# ------------------------
newdf1 = df.dropna(axis=0)
print(newdf1)

# only if there is more than 1 NaN value in row
newdf2 = df.dropna(axis=0, thresh=2)
print(newdf2)

# ------------------------
# Remove NaN columns
# ------------------------
newdf3 = df.dropna(axis=1)
print(newdf3)

# only if there is more than 1 NaN value in row
newdf4 = df.dropna(axis=1, thresh=2)
print(newdf4)


# ------------------------
# Fill NaN with default value
# ------------------------
newdf5 = df.fillna(value="XXXX")
print(newdf5)


# ------------------------
# Fill NaN with calculated value
# ------------------------
newdf6 = df["A"].fillna(value=df["A"].mean())
print(newdf6)
