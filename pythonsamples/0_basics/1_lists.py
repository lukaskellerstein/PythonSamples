print("Basics - Lists")

myArray = [1, 2, 3, 4]
myArrayStrings = ["a", "b", "c"]

# ------------------------------------
# Operations (1 Array)
# ------------------------------------

# add
myArray.append(5)
print(myArray)

# get
myValue1 = myArray[0]

# check if value is in the array
if 2 in myArray:
    print("2 is in myArray")
else:
    print("none")

# slice
mySlice1 = myArray[:2]
print(mySlice1)
mySlice2 = myArray[2:]
print(mySlice2)

# remove
myArrayStrings.remove("b")
print(myArrayStrings)

# remove last
myArray.pop()
print(myArray)

# length
aaa = len(myArray)
print(aaa)

# min, max
print(min(myArray))
print(max(myArray))


# ------------------------------------
# Operations (2 Arrays)
# ------------------------------------

# zip (!! result array will have same amount of items
# as the array with THE LESS items)

result = zip(myArray, myArrayStrings)
for i in result:
    print(i)
