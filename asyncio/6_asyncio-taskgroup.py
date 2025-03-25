# asyncio.TaskGroup, which is a modern
# and cleaner way to manage multiple async tasks with error handling.


# A new, cleaner way to manage multiple tasks together
# Replaces manually using asyncio.create_task() + await gather(...)

# Automatically:
## Starts all tasks
## Waits for all of them to complete
## Cancels the rest if any task fails
## Collects exceptions after all tasks are done


# asyncio.TaskGroup was introduced in Python 3.11.
# If you're using an earlier version, you need to use asyncio.create_task() and asyncio.gather() manually.

# ✅ **Summary: Why Use `TaskGroup`**

# | Feature              | Benefit                                             |
# |----------------------|-----------------------------------------------------|
# | **Auto-starts tasks** | ✅ No need to call `create_task()` separately       |
# | **Built-in error handling** | ✅ Cancels remaining tasks if any fail         |
# | **Cleaner syntax**    | ✅ Easier to manage task lifecycles                 |
# | **Waits for all tasks** | ✅ Exits only when all are done or failed         |


import asyncio


async def fetch_data(id, sleep_time):
    print(f"Coroutine {id} starting to fetch data")
    await asyncio.sleep(sleep_time)
    return {"id": id, "data": f"Sample data from coroutine {id}"}


async def main():
    tasks = []
    # TaskGroup() provides built-in error handling
    # If any of the tasks is getting failed(), the other tasks are cancelled.
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    results = [task.result() for task in tasks]

    for result in results:
        print(f"Received Results: {result}")


asyncio.run(main())
