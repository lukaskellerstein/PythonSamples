from functools import reduce


def sum(x, y):
    return x + y


myArr = [1, 2, 3, 4, 5]

fact = reduce(sum, myArr)

print("Sum: ", fact)
