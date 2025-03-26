### What is multiprocessing in Python?
multiprocessing is a Python module that lets you run multiple processes in parallel, 
allowing true concurrency by bypassing Python’s Global Interpreter Lock (GIL). 
Each process has its own Python interpreter and memory space.


### How does multiprocessing work?

When you use multiprocessing:
- It spawns multiple processes, each running independently.
- Each process runs in its own memory space (like separate programs).
- You can share data between processes using Queues, Pipes, or shared memory.
- It's great for CPU-bound tasks like image processing, data crunching, etc.


### 🔁 How is it different from `threading`?

| **Feature**     | **`multiprocessing`**                                 | **`threading`**                                      |
|------------------|--------------------------------------------------------|-------------------------------------------------------|
| Runs on          | Multiple **processes**                                 | Multiple **threads** in a single process              |
| Memory           | Each process has **separate memory**                   | Threads share **same memory space**                   |
| GIL              | **Bypasses GIL** – true parallelism                    | **Limited by GIL** – only one thread runs at a time   |
| Best for         | **CPU-bound** tasks                                     | **I/O-bound** tasks                                   |
| Overhead         | Higher (more memory & slower to start)                 | Lower overhead                                        |

### 🔁 How is it different from `asyncio`?

| **Feature**     | **`multiprocessing`**                              | **`asyncio`**                                           |
|------------------|-----------------------------------------------------|----------------------------------------------------------|
| Type             | Parallelism (multiple processes)                   | Concurrency (single-threaded, async tasks)              |
| GIL              | **Bypasses GIL**                                   | Still runs within the GIL                               |
| Best for         | **CPU-bound** tasks                                 | **I/O-bound** tasks like APIs, DB calls                 |
| Execution        | Multiple processes                                  | Single-threaded, non-blocking event loop               |
| Syntax           | Uses `Process`, `Queue`, etc.                       | Uses `async`, `await`, `async def`                      |



### When to Use multiprocessing

- You have CPU-bound tasks
- You want to utilize multiple CPU cores

```python
# Process large images on multiple cores
from multiprocessing import Pool

with Pool(4) as pool:
    results = pool.map(process_image, image_files)
```

### Resources

- Python Multiprocessing Tutorial: Run Code in Parallel Using the Multiprocessing Module: https://www.youtube.com/watch?v=fKl2JW_qrso