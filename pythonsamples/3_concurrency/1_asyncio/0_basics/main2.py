import asyncio

# -------------------------------------------------------
# RUN FOREVER
# -------------------------------------------------------
async def myCoroutine():
    while True:
        await asyncio.sleep(1)
        print("Task Executed")


# ----------------------------------
# VAR 1 - Asyncio methods
# ----------------------------------
# NO WAY

# ----------------------------------
# VAR 2 - Event loop
# ----------------------------------

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    try:
        asyncio.ensure_future(myCoroutine())  # ------------------> DONT Blocking LOOP

        # run loop forever
        loop.run_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Closing Loop")
        loop.close()
