import pandas as pd
import random


def getRandomColumns():
    return [str(random.randint(0, 1000)) for it in range(7)]


my_df = pd.DataFrame(
    columns=[
        "id",
        "symbol",
        "subsymbol",
        "bidSize",
        "bid",
        "ask",
        "askSize",
        "high",
        "low",
        "close",
    ],
)
my_df.set_index(["symbol", "subsymbol"], inplace=True)

print(my_df)


my_df.loc[
    ("CL", "CLN0"),
] = getRandomColumns()
my_df.loc[
    ("CL", "CLX0"),
] = getRandomColumns()
my_df.loc[
    ("CL", "CLZ0"),
] = getRandomColumns()


my_df.loc[
    ("GC", "GCN0"),
] = getRandomColumns()
my_df.loc[
    ("GC", "GCX0"),
] = getRandomColumns()
my_df.loc[
    ("GC", "GCZ0"),
] = getRandomColumns()

print(my_df)
