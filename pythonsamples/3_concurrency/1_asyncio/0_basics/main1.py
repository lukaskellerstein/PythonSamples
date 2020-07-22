import asyncio
import time


# -------------------------------------------------------
# RUN UNTIL COMPLETE
# -------------------------------------------------------
async def myCoroutine():
    i = 0
    while i < 10:
        await asyncio.sleep(1)
        i += 1
        print(i)


# ----------------------------------
# VAR 1 - Asyncio methods
# ----------------------------------

# coroutine 1
asyncio.run(myCoroutine())  # ------------------> Blocking LOOP

# ----------------------------------
# VAR 2 - Event loop
# ----------------------------------

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    try:
        loop.run_until_complete(myCoroutine())  # ------------------> Blocking LOOP

        # asyncio.ensure_future(myCoroutine())  # DOESN'T WORK

        # asyncio.create_task(myCoroutine()) # DOESN'T WORK

        # run loop forever
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
