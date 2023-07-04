# variant 1
def myfilter(text):
    return True if str(text).startswith("A") else False


# variant 2 - shorter
def myfilter2(text):
    return str(text).startswith("A")


myArr = ["Adam", "Lukas", "Anna"]


# ------------------------------------------------
result = filter(myfilter, myArr)
# ------------------------------------------------

# WHY THIS IS NOT WORKING ????
print(result)

[print(item) for item in result]
