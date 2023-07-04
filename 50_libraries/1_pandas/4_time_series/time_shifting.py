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

# print a first few rows of data
print(df.head())

# print a last few rows of data
print(df.tail())

# check if data-types of columns
print(df.info())

#  remove the unwanted columns
df.drop("Unnamed: 0", 1, inplace=True)
df.drop("volume", 1, inplace=True)
df.drop("average", 1, inplace=True)
df.drop("barCount", 1, inplace=True)
print(df)

# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------

print(df.tshift(freq="M").head())

print(df.tshift(freq="A").head())
