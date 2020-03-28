import asyncio
import random

# -------------------------------------------------------
# RUN UNTIL COMPLETE - MULTIPLE COROUTINES
# -------------------------------------------------------


async def myCoroutine(id):
    process_time = random.randint(1, 10)
    await asyncio.sleep(process_time)
    print(f"Couroutine {id} has completed after {process_time} seconds")


async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.ensure_future(myCoroutine(i)))

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
