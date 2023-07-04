import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Time resampling - Aggregation of data to different Time Frames
# ----------------------------------------------------
# ----------------------------------------------------

# read the dataset from CSV and remove the index column
df = pd.read_csv("TSLA.csv", index_col="date", parse_dates=True)


df["close"].plot(kind="line", figsize=(20, 5))

plt.show()
