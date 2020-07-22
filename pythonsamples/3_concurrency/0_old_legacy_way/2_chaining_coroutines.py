import asyncio


@asyncio.coroutine
def outer():
    print("in outer")
    print("waiting for result1")
    result1 = yield from phase1()  # ---------> INPUT VALUE FROM different coroutine
    print("waiting for result2")
    result2 = yield from phase2(result1)  # ---> INPUT VALUE FROM different coroutine
    return (result1, result2)


@asyncio.coroutine
def phase1():
    print("in phase1")
    return "result1"  # ----------------------> RETURN VALUE


@asyncio.coroutine
def phase2(arg):
    print("in phase2")
    return "result2 derived from {}".format(arg)  # -> RETURN VALUE


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(outer())
    print("return value: {!r}".format(return_value))
finally:
    event_loop.close()
