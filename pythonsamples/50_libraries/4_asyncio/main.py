import asyncio


# --------------------------
# COROUTINE - asynchronous method (like Goroutine in Golang)
# --------------------------
async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")


asyncio.run(main())
