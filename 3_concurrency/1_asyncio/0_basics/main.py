import asyncio


# -------------------------------------------------------------------
# COROUTINE - async methods
# -------------------------------------------------------------------


# ver - 1 - RETURN VALUE -------------
async def mycoroutine():
    # -------------
    # do something
    await asyncio.sleep(3)
    # -------------
    return "some value"


# ver - 2 - INPUT VALUE -------------
async def mycoroutine2(inputval):
    print(inputval)
    # -------------
    # do something
    await asyncio.sleep(3)
    # -------------


# ----------------------------------
# VAR 1 - Asyncio methods - RUN SIMULTANEOUSLY
# ----------------------------------

# coroutine 1
return_value = asyncio.run(mycoroutine())
print("return value: {!r}".format(return_value))

# coroutine 2
asyncio.run(mycoroutine2("AAA"))


# ----------------------------------
# VAR 2 - Asyncio methods + MAIN - RUN SIMULTANEOUSLY
# ----------------------------------
async def main():
    # run coroutines simultaniously
    await asyncio.gather(mycoroutine2("BBB"), mycoroutine2("CCC"))


asyncio.run(main())


# ----------------------------------
# VAR 3 - Event loop - RUN SIMULTANEOUSLY
# ----------------------------------

event_loop = asyncio.new_event_loop()
try:

    # coroutine 1
    return_value = event_loop.run_until_complete(mycoroutine())
    print("return value: {!r}".format(return_value))

    # coroutine 2
    event_loop.run_until_complete(mycoroutine2("AAA"))

finally:
    event_loop.close()
