import asyncio

# a shared variable
shared_resources = 0


# An Asyncio Lock
lock = asyncio.Lock()


async def modify_shared_resources():
    global shared_resources

    # async with lock: asynchronously waits until it can acquire the lock,
    # and automatically releases it when the block ends.

    async with lock:
        # Critical Section starts
        print(f"Resource before modification: {shared_resources}")
        shared_resources += 1
        await asyncio.sleep(1)
        print(f"Resource after modification: {shared_resources}")
        # Crirical section ends
    # Lock is released


async def main():
    await asyncio.gather(*(modify_shared_resources() for _ in range(0, 5)))


asyncio.run(main())
