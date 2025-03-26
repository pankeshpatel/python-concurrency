### Similarities: `threading` vs `asyncio.gather()` (Refer `1_thread.py` and `2_thread.py`, `2.1_thread.py`)

- Both:
    - Allow you to run multiple tasks concurrently.
    - Work well for I/O-bound tasks (like sleeping, API calls, file/network operations).
    - Can reduce total runtime when tasks would otherwise block (like sleep or waiting for a response).


### 🧵 **Key Differences** `threading` vs `asyncio.gather()`

| Feature                   | `threading`                                                 | `asyncio`                                                           |
|---------------------------|-------------------------------------------------------------|----------------------------------------------------------------------|
| **Concurrency Model**     | Preemptive threading (OS-level scheduling)                  | Cooperative multitasking (coroutines yield control)                 |
| **Memory & Resources**    | Heavier (each thread uses memory stack)                     | Lightweight (all coroutines run in the same thread)                 |
| **GIL Effect**            | GIL blocks CPU-bound code                                   | GIL still applies, but no context switch unless you `await`         |
| **Best For**              | I/O-bound or blocking tasks                                 | I/O-bound, non-blocking async functions                             |
| **Execution Context**     | Each thread runs independently                              | One event loop, tasks must yield (`await`)                          |
| **Blocking Code Support** | Supports blocking code like `time.sleep()`                  | Must use `asyncio.sleep()` or non-blocking alternatives             |
| **Error Handling**        | Exception per thread                                        | Gathered exceptions handled together                                |


### 🧵 **What’s Different Internally** `threading` vs `asyncio.gather()`

| Feature      | `threading`                                                | `asyncio`                                                       |
|--------------|-------------------------------------------------------------|------------------------------------------------------------------|
| **Style**    | Multi-threaded (preemptive)                                 | Single-threaded (cooperative)                                   |
| **Control**  | OS decides when each thread runs                            | You (with `await`) decide when to pause and resume              |
| **Blocking?**| Can use blocking functions like `time.sleep()`              | Must use non-blocking versions like `asyncio.sleep()`           |
| **Overhead** | Each thread uses memory and OS resources                    | Coroutines are very lightweight (run in same thread)            |
| **GIL**      | Threads release GIL during I/O                              | Async uses only one thread, avoids GIL issues                   |


#### Example Analogy
- Imagine a chef cooking several dishes:
    - With threads: You hire multiple cooks (threads). When one cook is waiting for a dish to boil, another can work.
    - With asyncio: One very smart cook switches between dishes on their own — while one boils, they chop veggies for the next.

Both work, both reduce waiting time — just with different strategies.

### When to Use threading
- You have I/O tasks but your libraries are blocking (like standard requests, or open() for files)
- You are working with legacy libraries that don’t support async

```python
# Using requests, which is blocking
def download(url):
    response = requests.get(url)

threads = [threading.Thread(target=download, args=(url,)) for url in urls]
```

### `concurrent.futures` (Refer `3_thread.py` and `4_thread.py`)

The purpose of concurrent.futures — one of Python's most elegant and powerful modules for running code concurrently.

- `concurrent.futures` is a high-level concurrency module introduced in Python 3.2. It provides a simple interface for running tasks asynchronously using either:
    - `Threads` (ThreadPoolExecutor) for I/O-bound tasks
    - `Processes` (ProcessPoolExecutor) for CPU-bound tasks

It abstracts away the complexity of managing threads or processes manually — so you can focus on what you want to run, not how it runs.


### Resources:

- Python Threading Tutorial: Run Code Concurrently Using the Threading Module - https://www.youtube.com/watch?v=IEEhzQoKtQU&t=625s