import asyncio

# -------------------------------------------------------
# RUN FOREVER
# -------------------------------------------------------


async def myCoroutine():
    while True:
        await asyncio.sleep(1)
        print("Task Executed")


def main():
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(myCoroutine())
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()


main()
