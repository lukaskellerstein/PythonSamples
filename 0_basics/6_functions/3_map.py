def addx(text):
    return str(text) + "X"


myArr = [1, 2, 3, 4, 5]

# ------------------------------------------------
result = map(addx, myArr)
# ------------------------------------------------

# WHY THIS IS NOT WORKING ????
print(list(result))

# [print(item) for item in result]
