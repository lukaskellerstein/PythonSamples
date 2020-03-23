import pymongo

# connect to mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")


# Relational concept  |	MongoDB equivalent
# -----------------------------------------
# Database	          | Database
# Tables	          | Collections
# Rows	              | Documents
# Index	              | Index


# ------------------------------------------
# DB
# ------------------------------------------

# check if DB exists
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")

# get the database
mydb = myclient["mydatabase"]
print(mydb)


# ------------------------------------------
# Collection = Table
# ------------------------------------------

# check if collection exists
collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")

# get collection
mycol = mydb["customers"]
print(mycol)

# delete collection
# mycol.drop()
