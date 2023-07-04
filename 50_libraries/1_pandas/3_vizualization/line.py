import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Visualization
# ----------------------------------------------------
# ----------------------------------------------------

# read the dataset from CSV
df = pd.read_csv("TSLA.csv")

# print a first few rows of data
df.head()

# show bars of one column
df.plot.line(x="date", y="close", figsize=(12, 5))

# Show the plot
plt.show()
