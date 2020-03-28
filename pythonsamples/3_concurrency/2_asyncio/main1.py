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


def main():
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(myCoroutine())
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()


if __name__ == "__main__":
    main()
