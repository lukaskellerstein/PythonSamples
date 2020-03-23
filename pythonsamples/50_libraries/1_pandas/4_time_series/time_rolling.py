import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ----------------------------------------------------
# ----------------------------------------------------
# Time resampling - Time rolling --> Indicators
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

# df["close"].plot(figsize=(20, 6))

# ------------------------------
# SMA 14
# ------------------------------
# df.rolling(window=14).mean()["close"].plot()
# or
# df["SMA14"] = df.rolling(window=14).mean()["close"]
# print(df.head(28))
# df[["SMA14", "close"]].plot(figsize=(20, 6))


# ------------------------------
# Bollinger Bands
# ------------------------------
df["Close: 30 Day Mean"] = df["close"].rolling(window=20).mean()
df["Upper"] = df["Close: 30 Day Mean"] + 2 * df["close"].rolling(window=20).std()
df["Lower"] = df["Close: 30 Day Mean"] - 2 * df["close"].rolling(window=20).std()
df[["close", "Close: 30 Day Mean", "Upper", "Lower"]].plot(figsize=(16, 6))


plt.show()
