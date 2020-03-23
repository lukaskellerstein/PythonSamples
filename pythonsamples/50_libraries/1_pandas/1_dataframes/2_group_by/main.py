import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# DataFrames - group by
# ----------------------------------------------------
# ----------------------------------------------------

d = {
    "Company": ["GOOG", "GOOG", "MSFT", "MSFT", "FB", "FB"],
    "Person": ["Sam", "Charlie", "Amy", "Vanessa", "Carl", "Sarah"],
    "Sales": [200, 120, 340, 124, 243, 350],
}
df = pd.DataFrame(d)
print(df)


# ----------------------------------------------------
# Group by Column
# ----------------------------------------------------

newdf1 = df.groupby("Company")
print(newdf1)

# all statistics
print(newdf1.describe())

# seprarate statistics
print(newdf1.count())
print(newdf1.min())
print(newdf1.max())
print(newdf1.mean())
print(newdf1.sum())
print(newdf1.std())


# with location
print(newdf1.mean().loc["FB"])

