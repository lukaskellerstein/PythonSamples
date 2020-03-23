import numpy as np
import pandas as pd


# ----------------------------------------------------
# ----------------------------------------------------
# Series
# ----------------------------------------------------
# ----------------------------------------------------
keys = ["Subaru", "Audi", "Bmw"]
my_arr = np.array([10, 20, 30])

series1 = pd.Series(my_arr, index=keys)

# ----------------------------------------------------
# Get data
# ----------------------------------------------------
subaru = series1["Subaru"]
print(subaru)

# get multiple at once
cars = series1[["Subaru", "Audi"]]
print(cars)

# ----------------------------------------------------
# Set data
# ----------------------------------------------------
series1["Audi"] = 999
print(series1)

# ----------------------------------------------------
# Append data
# ----------------------------------------------------
newSeries = pd.Series([300, 400], index=["Bugatti", "Ferrari"])
concetenateSerie = series1.append(newSeries)
print(concetenateSerie)

# ----------------------------------------------------
# Delete data
# ----------------------------------------------------
newSeries1 = series1.drop(["Bmw"])
print(newSeries1)

# ----------------------------------------------------
# Filter serie
# ----------------------------------------------------
aaa = series1.where(series1 > 50)
print(aaa)

# ----------------------------------------------------
# Filter serie (and items which doesn't meet condition ---> replace them)
# ----------------------------------------------------
aaa = series1.where(series1 > 50, 5)
print(aaa)

# ----------------------------------------------------
# Apply function (to each item)
# ----------------------------------------------------
bbb = series1.apply(lambda x: x * x)
print(bbb)
