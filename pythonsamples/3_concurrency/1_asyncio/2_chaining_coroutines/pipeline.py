import asyncio


async def phase1(val1):
    print("in phase1", val1)
    # do something
    result = await phase2(val1 + "1")
    return result


async def phase2(val2):
    print("in phase2", val2)
    # do something
    result = await phase3(val2 + "2")
    return result


async def phase3(val3):
    print("in phase3", val3)
    return "result derived from {}".format(val3 + "3")  # -> RETURN VALUE


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(phase1("AAA"))
    print("return value: {!r}".format(return_value))
finally:
    event_loop.close()
