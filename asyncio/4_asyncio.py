# We did not get any performance benefits in 3_asyncio.py as it is sequential.

# To run the corouting of 3_asyncio.py, we need to use the concept called `Tasks`.


# In asyncio, a Task is a wrapper around a coroutine. It tells the event loop:
##“Please schedule this coroutine to run as soon as possible — and manage its execution for me.”
# You can start multiple coroutines using Tasks, and they'll run concurrently.


### Why Use Tasks?
### By default, when you just write:

# ```python
#   await my_coroutine()
# ```

# It runs that coroutine and waits for it to finish — like a normal function call.

# But if you want to start multiple coroutines at the same time, you need to wrap them in Tasks.


import asyncio


async def fetch_data(id):
    print(f"Task {id} started")
    await asyncio.sleep(2)
    print(f"Task {id} finished")
    return f"Data from {id}"


async def main():
    # Create Tasks (not call) for running the corouting concurrently
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    print("Both tasks started!")

    # call these coroutines
    result1 = await task1
    result2 = await task2

    print(f"Result1: {result1}")
    print(f"Result2: {result2}")


asyncio.run(main())
