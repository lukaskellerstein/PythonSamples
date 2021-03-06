import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# DataFrames - Merge
# ----------------------------------------------------
# ----------------------------------------------------

# Simple Merge ---------------------------------------------
left = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)

right = pd.DataFrame(
    {
        "key": ["K0", "K1", "K2", "K3"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

newdf1 = pd.merge(left, right, how="inner", on="key")
print(newdf1)


# Advanced Merge ---------------------------------------------
left = pd.DataFrame(
    {
        "key1": ["K0", "K0", "K1", "K2"],
        "key2": ["K0", "K1", "K0", "K1"],
        "A": ["A0", "A1", "A2", "A3"],
        "B": ["B0", "B1", "B2", "B3"],
    }
)

right = pd.DataFrame(
    {
        "key1": ["K0", "K1", "K1", "K2"],
        "key2": ["K0", "K0", "K0", "K0"],
        "C": ["C0", "C1", "C2", "C3"],
        "D": ["D0", "D1", "D2", "D3"],
    }
)

newdf2 = pd.merge(left, right, on=["key1", "key2"])
print(newdf2)

newdf3 = pd.merge(left, right, how="outer", on=["key1", "key2"])
print(newdf3)

newdf4 = pd.merge(left, right, how="right", on=["key1", "key2"])
print(newdf4)

newdf5 = pd.merge(left, right, how="left", on=["key1", "key2"])
print(newdf5)

