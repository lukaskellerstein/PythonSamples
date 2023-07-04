import asyncio
import time


# -------------------------------------------------------
# RUN FOREVER - MULTIPLE COROUTINES
# -------------------------------------------------------


async def firstWorker():
    while True:
        await asyncio.sleep(1)
        print("First Worker Executed")


async def secondWorker():
    while True:
        await asyncio.sleep(1)
        print("Second Worker Executed")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    try:

        asyncio.ensure_future(firstWorker())  # - RUN SIMULTANEOUSLY
        asyncio.ensure_future(secondWorker())  # - RUN SIMULTANEOUSLY
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
