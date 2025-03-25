import asyncio


async def access_resource(semaphore, resource_id):
    async with semaphore:
        print(f"Accessing resources {resource_id}")
        await asyncio.sleep(1)
        print(f"Releasing resources {resource_id}")


async def main():
    semaphore = asyncio.Semaphore(2)
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(0, 5)))


asyncio.run(main())
