### What is a Future?
A Future represents a result of a computation that may not have completed yet. 
It acts as a placeholder for a value that will be available in the future.

Futures are commonly used with concurrent programming to manage asynchronous tasks.


### Where are Futures Used?
- `concurrent.futures` module (standard library)
- `asyncio` module (for async I/O programming)
- Both modules use Futures, but in different contexts.


### Futures with asyncio (Refer `8_asyncio.py`)

- `asyncio.Future` represents a placeholder for a result in an event loop. 
You typically don't create these directly (tasks and high-level APIs handle it), 
but understanding them is crucial for advanced async programming.