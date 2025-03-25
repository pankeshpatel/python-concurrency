import asyncio


async def fetch_data(delay):
    print("Fetching data...")
    # This causes the coroutine to:
    # Pause and say:
    # “I’ll sleep for 2 seconds. Event loop, go do something else in the meantime.”

    # The event loop waits 2 seconds.
    # Then it resumes the coroutine at:
    await asyncio.sleep(delay)

    print("Data Fetched")
    return {"data": "some data"}


async def main():
    print("Start of the main coroutine")

    # The following line creates a coroutine object.
    # But fetch_data(2) does NOT run yet.
    task = fetch_data(2)

    print("End of main coroutine")

    # The event loop says: “Okay, now it’s time to run `fetch_data(2)`` coroutine!”
    # It jumps into `fetch_data(2)`
    result = await task
    print(f"Received result: {result}")


asyncio.run(main())
