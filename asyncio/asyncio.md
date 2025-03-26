
### Intro

`asyncio` is a Python library used for concurrent programming using coroutines, event loops, and tasks.

Instead of using `threads` or `processes`, `asyncio` uses non-blocking I/O operations. 

It lets your program "pause" while waiting for something (like data from a `network`) and lets other tasks run in the meantime.

### Single vs Multi Thread

- `asyncio` is single-threaded by default.

- It uses: `One thread`, `One process`, With `an event loop` that handles many tasks cooperatively


### Why Use Asyncio?

- To handle multiple tasks concurrently (like `HTTP requests`, `database queries`, etc.)
- To avoid blocking code
- Efficient use of resources — good for I/O-bound tasks, not CPU-bound

### example scenario when to use Asyncio

- Ask yourself
Is my program waiting on something (like network or disk)? Or is it working hard on the CPU (like image processing or crunching numbers)?

| **Task Type** | **Examples**                          | **Use this...**                              |
|---------------|---------------------------------------|----------------------------------------------|
| **I/O-bound** | Web scraping, API calls, file I/O     |  `asyncio` OR `threading`                    |
| **CPU-bound** | Image processing, ML training         | `multiprocessing`                            |
| **Mixed**     | Some of both                          | Maybe a hybrid!                              |


### When to Use asyncio
- You are making many API calls, or web scraping
- You want to handle thousands of network connections
- You can use or write non-blocking code (like `aiohttp`, `aiomysql`, etc.). 





# ⚡ Asyncio vs Threading vs Multiprocessing — Summary Table

| Feature                 | `asyncio`                          | `threading`                          | `multiprocessing`                     |
|-------------------------|------------------------------------|--------------------------------------|---------------------------------------|
| **Use for**             | I/O-bound tasks                    | I/O-bound (esp. legacy code)         | CPU-bound tasks                       |
| **Concurrency Type**    | Cooperative (coroutines)           | Pre-emptive (OS-level)               | True parallelism                      |
| **Overhead**            | Very low                           | Medium (due to context switching)    | High (separate processes)             |
| **Shared Memory**       | Yes                                | Yes                                  | No (needs inter-process comm.)        |
| **Debugging**           | Easier                             | Tricky                               | Tricky                                |
| **Blocking Code Support** | Needs non-blocking code           | Can use blocking code                | Can use blocking code                |


### Resources

Asyncio in Python - Full Tutorial - https://www.youtube.com/watch?v=Qb9s3UiMSTA