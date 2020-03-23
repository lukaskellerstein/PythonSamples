import numpy as np
import pandas as pd

# ----------------------------------------------------
# ----------------------------------------------------
# DataFrames - Join
# ----------------------------------------------------
# ----------------------------------------------------

left = pd.DataFrame(
    {"A": ["A0", "A1", "A2"], "B": ["B0", "B1", "B2"]}, index=["K0", "K1", "K2"]
)

right = pd.DataFrame(
    {"C": ["C0", "C2", "C3"], "D": ["D0", "D2", "D3"]}, index=["K0", "K2", "K3"]
)


# Concat ---------------------------------------------
newdf1 = left.join(right)
print(newdf1)

newdf2 = left.join(right, how="outer")
print(newdf2)

