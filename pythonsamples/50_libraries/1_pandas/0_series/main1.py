import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Series
# ----------------------------------------------------
# ----------------------------------------------------
keys = ["1", "2", "3", "4", "5", "6", "7", "8"]
my_arr = np.array([0, -5, 10, 20, 20, -50, 40, 60])

series1 = pd.Series(my_arr, index=keys)
print(series1)


# ----------------------------------------------------
# Count
# ----------------------------------------------------
print(series1.size)


# ----------------------------------------------------
# Value Counts = Histogram
# ----------------------------------------------------
print(series1.value_counts())


# ----------------------------------------------------
# Sum
# ----------------------------------------------------
print(series1.sum())

# ----------------------------------------------------
# Cumulative Sum
# ----------------------------------------------------
cumsum = series1.cumsum()
print(cumsum)
cumsum.plot()


# cumulate minimum
print(series1.cummin())

# cumulate maximum
print(series1.cummax())


# ----------------------------------------------------
# Min, Max
# ----------------------------------------------------
print(series1.min())
print(series1.max())


# ----------------------------------------------------
# Avg
# ----------------------------------------------------

# The mean or average is (1+1+2+3+4)/5 = 2.2
# The median is "2" (the central value).
# The mode is "1" (it occurs most often).
# The midrange is (4+1)/2 = 2.5

print(series1.mean())  # arithmetic average
print(series1.median())  # median
print(series1.mode())  # mode


# ----------------------------------------------------
# Variance
# ----------------------------------------------------
print(series1.var())


# ----------------------------------------------------
# Standard deviation
# ----------------------------------------------------
print(series1.std(ddof=2))


# ----------------------------------------------------
# ----------------------------------------------------
# PLOT
# ----------------------------------------------------
# ----------------------------------------------------
series1.plot()
plt.show()