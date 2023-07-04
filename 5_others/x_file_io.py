print("Basics - File IO")


myFile = open("../pyproject.toml")
allFileString = myFile.read()  # READ => return STRING
print(allFileString)
myFile.close()

myFile2 = open("../pyproject.toml")
allFileLines = myFile2.readlines()  # READ LINE BY LINE => return ARRAY
print(allFileLines)
myFile2.close()


# ENHACEMENT - don't have to close -------------------------- ?
with open("../pyproject.toml") as myFile3:
    aaa = myFile3.readline()
print(aaa)


# write to the file
with open("../pyproject.toml", mode="a") as myFile4:
    myFile4.write("AAAA")

# read
with open("../pyproject.toml") as myFile5:
    aaa = myFile5.read()
print(aaa)


# FILE MODES = A - modify, R - read, W - write (and create if doesn't exist)
# as in Linux
with open("../pyproject.toml", mode="w") as myFile4:
    myFile4.write("AAAA")
