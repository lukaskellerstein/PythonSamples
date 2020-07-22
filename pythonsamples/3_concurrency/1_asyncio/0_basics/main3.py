import asyncio


# -------------------------------------------------------------------
# MIX RUN FOREVER and RUN UNTIL COMPLETE
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


# ver - 3 - INFINITE COROUTINE -----------------
async def myCoroutineInfinite(timeout):
    while True:
        await asyncio.sleep(timeout)
        print(f"Task Executed (each {timeout} sec)")


# ----------------------------------
# VAR 1 - Asyncio methods
# ----------------------------------

await asyncio.gather(foo(future), bar(future))


# ----------------------------------
# VAR 2 - Event loop
# ----------------------------------

event_loop = asyncio.get_event_loop()
try:

    # coroutine 0 - infinite
    asyncio.ensure_future(myCoroutineInfinite(1))  # -------------> DONT Blocking LOOP

    # coroutine 1
    return_value = event_loop.run_until_complete(mycoroutine())  # -> Blocking LOOP
    print("return value: {!r}".format(return_value))

    # coroutine 2
    event_loop.run_until_complete(mycoroutine2("AAA"))  # ----------> Blocking LOOP

    # coroutine 0 - infinite
    asyncio.ensure_future(myCoroutineInfinite(2))  # ----------> DONT Blocking LOOP

    # run loop forever
    event_loop.run_forever()
finally:
    print("Closing Loop")
    event_loop.close()
