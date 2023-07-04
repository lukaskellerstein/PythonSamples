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

# B         business day frequency
# C         custom business day frequency (experimental)
# D         calendar day frequency
# W         weekly frequency
# M         month end frequency
# SM        semi-month end frequency (15th and end of month)
# BM        business month end frequency
# CBM       custom business month end frequency
# MS        month start frequency
# SMS       semi-month start frequency (1st and 15th)
# BMS       business month start frequency
# CBMS      custom business month start frequency
# Q         quarter end frequency
# BQ        business quarter endfrequency
# QS        quarter start frequency
# BQS       business quarter start frequency
# A         year end frequency
# BA, BY    business year end frequency
# AS, YS    year start frequency
# BAS, BYS  business year start frequency
# BH        business hour frequency
# H         hourly frequency
# T, min    minutely frequency
# S         secondly frequency
# L, ms     milliseconds
# U, us     microseconds
# N         nanoseconds

# yearly statistics
print(df.resample(rule="A").mean())
print(df.resample(rule="A").std())

# quartelly statistics
print(df.resample(rule="Q").mean())
print(df.resample(rule="Q").std())

# monthly average
print(df.resample(rule="M").mean())
print(df.resample(rule="M").std())


# ------------------------------------------------------
# ------------------------------------------------------
# ------------------------------------------------------

df["close"].resample(rule="A").mean().plot(kind="bar", figsize=(20, 5))

plt.show()
