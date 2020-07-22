import pandas as pd


my_df = pd.DataFrame(columns=["Datetime", "Open", "High", "Low", "Close", "Volume"])
my_df.set_index(["Datetime"], inplace=True)

print(my_df)
