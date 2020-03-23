import pymongo

# connect to mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# ------------------------------------------
# FIND ONE
# ------------------------------------------
x = mycol.find_one()
print(x)

# ------------------------------------------
# FIND ALL
# ------------------------------------------
for x in mycol.find():
    print(x)

# ------------------------------------------
# FIND (define returned columns)
# ------------------------------------------
for x in mycol.find({}, {"_id": 0, "name": 1, "address": 1}):
    print(x)

# ------------------------------------------
# FIND (define number returned rows)
# ------------------------------------------
for x in mycol.find().limit(5):
    print(x)

# ------------------------------------------
# FIND (get count)
# ------------------------------------------

print(mycol.find().count())
