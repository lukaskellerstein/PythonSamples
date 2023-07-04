import pymongo

# connect to mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# ------------------------------------------
# SORT
# ------------------------------------------

# sort("name", 1) #ascending
# sort("name", -1) #descending

mydoc = mycol.find().sort("name", -1)

for x in mydoc:
    print(x)

