# ------------------------------------------------
# LAMBDA expression = ANONYMOUS function
# ------------------------------------------------


# normal function
def sum1(a, b):
    return a + b


# vs

# anonymous function (one parameter)
lambda a: a * 2
# anonymous function (two parameter)
lambda a, b: a + b

# |
# |
# |
# V

myArr = [1, 2, 3, 4, 5]
result = map(lambda a: a * 2, myArr)

print(result)

[print(item) for item in result]
