import pymongo

# connect to mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# ------------------------------------------
# DELETE ONE
# ------------------------------------------
myquery = {"address": "Mountain 21"}
mycol.delete_one(myquery)


# ------------------------------------------
# DELETE MANY
# ------------------------------------------
myquery = {"address": {"$regex": "^S"}}
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")


# ------------------------------------------
# DELETE ALL
# ------------------------------------------
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")
