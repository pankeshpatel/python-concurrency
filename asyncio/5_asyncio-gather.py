# gather() is a quick way (compared to create_task()) to concurrently run multiple coroutines
# It has missing error handling

import asyncio


async def fetch_data(id):
    print(f"Task {id} started")
    await asyncio.sleep(2)
    print(f"Task {id} finished")
    return f"Data from {id}"


async def main():

    # run coroutne concurrently and gather their return values
    # takes two coroutine objects: fetch_data(1) and fetch_data(2)
    # It wraps both in Tasks under the hood (so you don't need to use create_task() manually)
    # Then it schedules them to run concurrently
    # It waits (await) for both to finish

    results = await asyncio.gather(fetch_data(1), fetch_data(2))

    for result in results:
        print(f"{result}")


asyncio.run(main())
