print("Basics - Dictionary")

# create a dictionary
myDict = {"name": "myName", "description": "asdfasdfasfda"}
print(myDict)

# add to dictionary
myDict["id"] = "1"
print(myDict)

myDict["someobj"]["aaa"] = "bbb"
print(myDict)

# get
myVal = myDict["name"]
print(myVal)

# remove
myDict.pop("description")
print(myDict)


# --------------------------
# Dictionary as complex object
# --------------------------

# create / define
myObj = {
    "id": "asdfasfd",
    "name": "Subaru",
    "engine": {"valves-count": "4", "valve-size": "2000"},  # object
    "drivers": ["Lukas", "Anna"],  # array
}
print(myObj)

# access a key in deep object
engineValveCount = myObj["engine"]["valves-count"]
print(engineValveCount)

# check if key is in the object
if "valves-count" in myObj["engine"]:
    print("has a valve-count")

# get keys and values of the object
print(myObj.keys())
print(myObj.values())
