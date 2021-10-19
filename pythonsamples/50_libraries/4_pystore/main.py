import pystore
import quandl

# Set storage path (optional, default is `~/pystore`)
pystore.set_path("./db/pystore")

# List stores
pystore.list_stores()

# Connect to datastore (create it if not exist)
store = pystore.store("mydatastore")

# List existing collections
store.list_collections()

# Access a collection (create it if not exist)
collection = store.collection("NASDAQ")

# List items in collection
collection.list_items()

# Load some data from Quandl
aapl = quandl.get("WIKI/AAPL", authtoken="73JMr-Fhopzju62Q3Nvz")

# Store the first 100 rows of the data in the collection under "AAPL"
collection.write("AAPL", aapl[:100], metadata={"source": "Quandl"}, overwrite=True)


item = collection.item("AAPL")
print(item)
print(item.data)
aaa = item.to_pandas()


# Reading the item's data
item = collection.item("AAPL")
data = item.data  # <-- Dask dataframe (see dask.pydata.org)
metadata = item.metadata
df = item.to_pandas()

print(df)

# Append the rest of the rows to the "AAPL" item
collection.append("AAPL", aapl[100:], npartitions=item.data.npartitions)

print(collection.item("AAPL").to_pandas())

# Reading the item's data
item = collection.item("AAPL")
data = item.data
metadata = item.metadata
df = item.to_pandas()

print(df)

# --- Query functionality ---

# Query avaialable symbols based on metadata
collection.list_items(some_key="some_value", other_key="other_value")


# --- Snapshot functionality ---

# # Snapshot a collection
# # (Point-in-time named reference for all current symbols in a collection)
# collection.create_snapshot('snapshot_name')

# # List available snapshots
# collection.list_snapshots()

# # Get a version of a symbol given a snapshot name
# collection.item('AAPL', snapshot='snapshot_name')

# # Delete a collection snapshot
# collection.delete_snapshot('snapshot_name')


# # ...


# # Delete the item from the current version
# collection.delete_item('AAPL')

# # Delete the collection
# store.delete_collection('NASDAQ')
