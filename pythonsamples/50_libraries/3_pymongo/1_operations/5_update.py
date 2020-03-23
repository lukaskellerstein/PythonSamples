import pymongo

# connect to mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# ------------------------------------------
# UPDATE ONE
# ------------------------------------------
myquery = {"address": "Valley 345"}
newvalues = {"$set": {"address": "Canyon 123"}}

mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)


# ------------------------------------------
# UPDATE MANY
# ------------------------------------------
myquery = {"address": {"$regex": "^S"}}
newvalues = {"$set": {"name": "Minnie"}}

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")
