print("Basics - IF-ELSE, FOR, WHILE")

# ---------------------------------
# IF-ELSE
# ---------------------------------
myVar = "car"

if myVar == "car":
    print("Vrrrrrrr vrrrrrr")
elif myVar == "phone":
    print("Crrrrr Crrrrrrr")
else:
    print("SILENCE")


# ONELINER - ternary operator
print("Aaaaaaaaaaaaaaa") if myVar == "car" else print("Bbbbbbbbbbbbb")


# ---------------------------------
# FOR EACH - Array
# ---------------------------------
myVar2 = [1, 2, 3, 4, 5]

for item in myVar2:
    print(item)

# enumerate function
for value in enumerate(myVar2):
    print(value)

for index, value in enumerate(myVar2):
    print(index)
    print(value)

# iterate and change
newMyVar1 = []
for item in myVar2:
    newMyVar1.append(str(item) + "X")
print(newMyVar1)

# iterate and change - ONELINER
newMyVar2 = [str(item) + "X" for item in myVar2]
print(newMyVar2)


# iterate and change - with condition
newMyVar1 = []
for item in myVar2:
    if item > 2:
        newMyVar1.append(str(item) + "X")
    else:
        newMyVar1.append("TOO LOW")
print(newMyVar1)

# iterate and change - with condition - ONELINER
newMyVar2 = [str(item) + "X" if item > 2 else "TOO LOW" for item in myVar2]
print(newMyVar2)


# iterate and work with 2 arrays
myVar3 = ["a", "b", "c", "d", "e"]
newMyVar1 = []
for item1 in myVar2:
    for item2 in myVar3:
        newMyVar1.append(str(item1) + str(item2))
print(newMyVar1)

# iterate and work with 2 arrays - ONELINER
newMyVar2 = [str(item1) + str(item2) for item1 in myVar2 for item2 in myVar3]
print(newMyVar2)


# ---------------------------------
# FOR EACH - String
# ---------------------------------
word = "alphabet"

for item in word:
    print(item)

for value in enumerate(word):
    print(value)

for index, value in enumerate(word):
    print(index)
    print(value)


# iterate and change
newMyVar1 = []
for item in word:
    newMyVar1.append(item + "X")
print(newMyVar1)

# iterate and change - ONELINER
newMyVar2 = [item + "X" for item in word]
print(newMyVar2)


# ---------------------------------
# FOR EACH - Dictionary
# ---------------------------------
myDict = {"name": "myName", "description": "asdfasdfasfda"}

for k, v in myDict.items():
    print(k, v)


# ---------------------------------
# WHILE
# ---------------------------------
while len(myVar2) > 0:
    print("...popping...")
    myVar2.pop()

