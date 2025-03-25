import asyncio


# This is a coroutine
# Coroutines are like `pause-able` functions that return a special object.
async def main():
    print("Start of main co-routine")


# Step 1. Creates a new event loop:
## Python starts an event loop specifically for this run.
## Think of it as the manager that will handle all async tasks.

# Step 2. Schedules the coroutine main() to run:
## The coroutine object main() is submitted to the loop.
## It's now ready to be executed.

# Step 3. Starts running the event loop:
## The event loop begins processing the coroutine.
## It steps into main() and executes the first line.

# Step 4. Coroutine completes:
## Since there’s nothing else to await, the coroutine ends.
## The event loop sees no more tasks to run.

# Step 5. Shuts down the event loop:
## Cleans up everything and exits.

asyncio.run(main())
