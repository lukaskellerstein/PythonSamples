import pystore
import pandas as pd
import numpy as np

# my_df = pd.DataFrame(["AAPL", "GOOG"], columns=["Symbol"])
my_df = pd.DataFrame([["abcd", "abcd", "abcd", "abcd"]], columns=["W", "X", "Y", "Z"])
my_df.index = range(1, len(my_df) + 1)
print(my_df)


pystore.set_path("./db/pystore")
store = pystore.store("mydatastore")
collection = store.collection("test")

collection.write("AAA", my_df, overwrite=True)

item = collection.item("AAA")
print(item.to_pandas())

# print(collection.item("AAA").to_pandas())

# my_new_df = pd.DataFrame(["UBER"], columns=["Symbol"])
my_new_df = pd.DataFrame([["xyz", "xyz", "xyz", "xyz"]], columns=["W", "X", "Y", "Z"])
my_new_df.index = range(2, len(my_df) + 2)
print(my_new_df)


item = collection.item("AAA")
collection.append("AAA", my_new_df, npartitions=item.data.npartitions)

item = collection.item("AAA")
print(item.to_pandas())

# print(collection.item("AAA").to_pandas())
