import asyncio


async def set_future_result(future, value):
    await asyncio.sleep(2)

    # set the result of the future
    future.set_result(value)

    print(f"Set the future's result to: {value}")


async def main():

    # create a future object
    # It gets the current event loop.
    loop = asyncio.get_running_loop()

    # It creates an empty `Future` object **tied to this event loop**.
    # At this point, `future.done()` is `False`, and `future.result()` would raise an error if called.
    future = loop.create_future()

    # schedule setting the future's result
    # set_future_result(future, "ready")  calls the coroutine function and creates a coroutine object,
    # It does not execute the function body yet.

    # asyncio.create_task(...):
    # ✅ Schedules the coroutine object to run in the background on the event loop.
    # ✅ Returns a Task that will run the coroutine.
    # The body (await asyncio.sleep(2), etc.) will be run later when the loop gets to it.

    asyncio.create_task(set_future_result(future, "ready"))

    # wait for the future's result (not )
    # This is the beautiful part 🎯:
    # main() is now paused here, waiting for the Future to be resolved.
    # It says: “I’ll chill until someone calls future.set_result(...).”
    result = await future
    print(f"Received the future result: {result}")


asyncio.run(main())
