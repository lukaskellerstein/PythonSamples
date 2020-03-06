def addx(text):
    return str(text) + "X"


myArr = [1, 2, 3, 4, 5]

# ------------------------------------------------
result = map(addx, myArr)
# ------------------------------------------------

# WHY THIS IS NOT WORKING ????
print(result)

[print(item) for item in result]
