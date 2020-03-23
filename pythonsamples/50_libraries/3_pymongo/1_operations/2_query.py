import pymongo

# connect to mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# ------------------------------------------
# Simple QUERY
# ------------------------------------------
myquery = {"address": "Park Lane 38"}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)


# ------------------------------------------
# Advanced QUERY
# ------------------------------------------
myquery = {"address": {"$gt": "S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)


# ------------------------------------------
# Regex QUERY
#
# Regular expressions can only be used to query strings. !!
# ------------------------------------------
myquery = {"address": {"$regex": "^S"}}

mydoc = mycol.find(myquery)

for x in mydoc:
    print(x)

