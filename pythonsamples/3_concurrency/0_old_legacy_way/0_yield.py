import asyncio

# -------------------------------------------------------------------
# YIELD - keyword for async produce or insert a value
# -------------------------------------------------------------------

# ----------------------
# produce - generator
# ----------------------
def my_method_asynchronous():
    yield "some value1"  # ---------------------------> RETURN VALUE


# generator object
obj1 = my_method_asynchronous()

# run generator
myvar1 = obj1.__next__()
print(myvar1)


# ----------------------
# consume - coroutine
# ----------------------

# ver - 1 - RETURN VALUE -------------
@asyncio.coroutine
def my_coroutine():
    # -----------------
    # some calculations
    # -----------------
    yield "some value2"  # ---------------------------> RETURN VALUE


# coroutine object
obj_coroutine = my_coroutine()

# run generator
val1 = obj_coroutine.__next__()
print(val1)

# ver - 2 - INPUT VALUE --------------
@asyncio.coroutine
def my_coroutine2(initVal: str):
    # print(data)
    print(initVal)
    while True:  # --------------------------------> Running FOREVER
        data = yield  # ---------------------------> INPUT VALUE
        # -----------------
        # some calculations
        # -----------------
        print(data)
        print(initVal)


# coroutine object
obj_coroutine2 = my_coroutine2("aaa")

# run generator
obj_coroutine2.__next__()
obj_coroutine2.send("some value3")  # -------------> CAN be called multiple times
obj_coroutine2.send("some value4")  # -------------> CAN be called multiple times
obj_coroutine2.send("some value5")  # -------------> CAN be called multiple times
