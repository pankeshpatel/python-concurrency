import asyncio


async def successful_task():
    await asyncio.sleep(1)
    return "✅ Success!"


async def failing_task():
    await asyncio.sleep(1)
    raise ValueError("❌ Something went wrong in failing_task")


async def main():
    results = await asyncio.gather(
        successful_task(),
        failing_task(),
        return_exceptions=True,  # Catch exceptions instead of raising
    )

    for i, result in enumerate(results, start=1):
        if isinstance(result, Exception):
            print(f"Task {i} failed with exception: {result}")
        else:
            print(f"Task {i} completed with result: {result}")


asyncio.run(main())
