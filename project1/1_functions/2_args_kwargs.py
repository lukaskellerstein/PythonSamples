# dynamic amount of parameters => tuple
def myfunction(*args):
    print(args)
    [print(item) for item in args]


myfunction(1, 2, "a", "b", [100, 200], {"name": "lukas", "age": "33"})


# dynamic amount of parameters with names => dictionary
def myfunction(**kwargs):
    print(kwargs)
    [print(item) for item in kwargs]


myfunction(
    var1=1,
    var2=2,
    var3="a",
    var4="b",
    var5=[100, 200],
    var6={"name": "lukas", "age": "33"},
)


def myfunction(*args, **kwargs):
    print(args)
    print(kwargs)
    [print(item) for item in args]
    [print(item) for item in kwargs]


myfunction(
    1,
    2,
    "a",
    "b",
    [100, 200],
    {"name": "lukas", "age": "33"},
    var1=1,
    var2=2,
    var3="a",
    var4="b",
    var5=[100, 200],
    var6={"name": "lukas", "age": "33"},
)

