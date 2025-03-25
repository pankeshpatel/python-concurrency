### python-concurrency

- `asyncio` (single thread, event-loop): It is a Python library used for concurrent programming using coroutines, event loops, and tasks.
- `threading` :
- `multiprocessing` :


#### Usage `asyncio` vs `threading` vs `multiprocessing`

- Ask yourself
Is my program waiting on something (like network or disk)? Or is it working hard on the CPU (like image processing or crunching numbers)?

| **Task Type** | **Examples**                          | **Use this...**                              |
|---------------|---------------------------------------|----------------------------------------------|
| **I/O-bound** | Web scraping, API calls, file I/O     |  `asyncio` OR `threading`                    |
| **CPU-bound** | Image processing, ML training         | `multiprocessing`                            |
| **Mixed**     | Some of both                          | Maybe a hybrid!                              |



#### ⚡ Asyncio vs Threading vs Multiprocessing — Summary Table

| Feature                 | `asyncio`                          | `threading`                          | `multiprocessing`                     |
|-------------------------|------------------------------------|--------------------------------------|---------------------------------------|
| **Use for**             | I/O-bound tasks                    | I/O-bound (esp. legacy code)         | CPU-bound tasks                       |
| **Concurrency Type**    | Cooperative (coroutines)           | Pre-emptive (OS-level)               | True parallelism                      |
| **Overhead**            | Very low                           | Medium (due to context switching)    | High (separate processes)             |
| **Shared Memory**       | Yes                                | Yes                                  | No (needs inter-process comm.)        |
| **Debugging**           | Easier                             | Tricky                               | Tricky                                |
| **Blocking Code Support** | Needs non-blocking code           | Can use blocking code                | Can use blocking code                |






#### Resources:
    - Asyncio in Python - Full Tutorial (Tech with Tim) - https://www.youtube.com/watch?v=Qb9s3UiMSTA
 