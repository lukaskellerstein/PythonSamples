import pymongo
import pandas as pd


# connect to mongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]


# ------------------------------------------
# MONGO -> PANDAS
# ------------------------------------------
samples = mycol.find()
df = pd.DataFrame(samples)
print(df.head())


# ------------------------------------------
# PANDAS -> MONGO
# ------------------------------------------
df = pd.DataFrame(
    {
        "name": ["Braund", "Cummings", "Heikkinen", "Allen"],
        "address": ["Prague 1", "Prague 2", "Prague 3", "Prague 4"],
    }
)
data = df.to_dict(orient="records")
mycol.insert_many(data)

for x in mycol.find():
    print(x)
