# this is multi-tasking

import time
import asyncio


async def do_something(id):
    print(f"Sleeping...{id}")
    await asyncio.sleep(1)
    print(f"Done sleeping...{id}")


async def main():

    start = time.perf_counter()
    t1 = asyncio.create_task(do_something("1"))
    t2 = asyncio.create_task(do_something("2"))

    await t1
    await t2
    finish = time.perf_counter()
    print(f"Finished in {round(finish-start, 2)} seconds")


asyncio.run(main())
