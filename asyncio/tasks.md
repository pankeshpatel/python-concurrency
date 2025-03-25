
### Tasks

- We did not get any performance benefits in 3_asyncio.py as it is sequential.
- To run the corouting of 3_asyncio.py, we need to use the concept called `Tasks`.


#### What Are `Tasks` in asyncio?

In asyncio, a Task is a wrapper around a coroutine. It tells the event loop:
``Please schedule this coroutine to run as soon as possible — and manage its execution for me.``
You can start multiple coroutines using Tasks, and they'll run concurrently.


### Why Use Tasks?

By default, when you just write:

```python
   await my_coroutine()
```

- It runs that coroutine and waits for it to finish — like a normal function call.
- But if you want to start multiple coroutines at the same time, you need to wrap them in Tasks.

- Refer `4_asyncio.py`




📌 **Key Differences: `await` vs `create_task()`**

| Pattern                   | Behavior                                       |
|---------------------------|------------------------------------------------|
| `await coroutine()`       | Runs one coroutine at a time                   |
| `asyncio.create_task()`   | Schedules coroutine to run concurrently        |
| `await task`              | Waits for that specific task to finish         |
| `asyncio.gather()`        | Waits for **multiple tasks** at once           |



### `asyncio.gather()` (Refer `5_asyncio.py`)

`asyncio.gather()` is used to 
- run multiple coroutines concurrently
- Wait for all of them to finish
- Collect their results (in order)

Think of it as:
"Bundle these coroutines together and bring me all the results when they’re done."

```python
results = await asyncio.gather(coro1(), coro2(), coro3())
```

- All coroutines start at the same time
- gather() waits for all to finish
- It returns their results as a list (in the same order you passed them)

#### Error Handling in gather()

If any coroutine raises an exception, gather():
    - Cancels all other tasks
    - Raises that exception after all tasks finish

But! You can tell `gather()` to return exceptions instead~(Refer `7_asyncio.py`):

```python3
    await asyncio.gather(task1, task2, return_exceptions=True)
```

🧩 **Summary Table**

| Feature                     | `asyncio.gather()`                                |
|-----------------------------|---------------------------------------------------|
| **Runs tasks concurrently** | ✅ Yes                                            |
| **Returns results**         | ✅ Yes, as a list in original order               |
| **Stops on error?**         | ✅ Yes, unless `return_exceptions=True`           |
| **Creates tasks?**          | ✅ Yes, it wraps coroutines into tasks            |



### `asyncio.TaskGroup` (Refer `6_asyncio.py`)

It is  a modern and cleaner way to manage multiple async tasks with error handling.

- A new, cleaner way to manage multiple tasks together
- Replaces manually using asyncio.create_task() + await gather(...)

- Automatically:
    - Starts all tasks
    - Waits for all of them to complete
    - Cancels the rest if any task fails
    - Collects exceptions after all tasks are done


- asyncio.TaskGroup was introduced in Python 3.11.

- If you're using an earlier version, you need to use asyncio.create_task() and asyncio.gather() manually.

✅ **Summary: Why Use `TaskGroup`**

| Feature              | Benefit                                             |
|----------------------|-----------------------------------------------------|
| **Auto-starts tasks** | ✅ No need to call `create_task()` separately       |
| **Built-in error handling** | ✅ Cancels remaining tasks if any fail         |
| **Cleaner syntax**    | ✅ Easier to manage task lifecycles                 |
| **Waits for all tasks** | ✅ Exits only when all are done or failed         |
