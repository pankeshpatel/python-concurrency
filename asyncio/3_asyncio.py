import asyncio


async def fetch_data(delay, id):
    print(f"Fetching data...{id}")

    # It tells the event loop:
    ##"Hey, I want to sleep for delay seconds,
    ## but while I’m sleeping, feel free to do something else!"

    # The coroutine that called await asyncio.sleep() is paused, and control returns to the event loop.
    # After the time is up, the event loop resumes the coroutine where it left off.
    await asyncio.sleep(delay)

    print(f"Data fetched...{id}")
    return {"data": "Some data", "id": id}


async def main():
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    # You're awaiting task1 before starting task2.
    # So it's effectively sequential, even though you're using async/await.
    result1 = await task1
    print(f"Received Result: {result1}")

    result2 = await task2
    print(f"Received Result: {result2}")


asyncio.run(main())
