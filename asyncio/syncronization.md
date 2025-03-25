### What is Lock? (Refer `9_asyncio.py`)

- A Lock is a synchronization primitive that ensures only one thread or task can access a critical section (shared resource) at a time.

- Think of it like:
    - A single-key door — only one person can enter at a time, and others must wait until the key is returned.


#### When to Use a Lock
Use a lock when:
- Multiple threads or coroutines are modifying shared data.
- You want to avoid race conditions (unpredictable outcomes from concurrent access).

#### 🔁 Types of Locks in Python

| **Type**             | **Module**     | **Use case**                       |
|----------------------|----------------|------------------------------------|
| `threading.Lock`     | `threading`    | Used in multithreading             |
| `asyncio.Lock`       | `asyncio`      | Used in asynchronous programs      |



### What is a Semaphore? (Refer `10_asyncio.py`)
- A semaphore is a synchronization primitive that controls access to a shared resource by 
allowing up to a fixed number of tasks to access it at the same time.

- Think of it as a counter that limits how many tasks can enter a "critical section" at once.

- If the counter is 0, new tasks must wait until some task releases the semaphore.

#### Analogy: Bathroom with Multiple Stalls

- Imagine a public bathroom with 3 stalls. If 3 people are inside:
    - A 4th person has to wait until someone exits.
    - Each person entering the bathroom decreases the count, and exiting increases it.

This is how a semaphore works.

####  How It Works Internally
- `asyncio.Semaphore(n)` creates a semaphore with a counter of `n`.
- When a coroutine enters the async `with semaphore:` block:
    - If the `counter > 0:` It proceeds, and the counter is decremented.
    - If the `counter == 0:` It waits (is paused).

- When the block exits, the counter is incremented, and waiting coroutines may resume.

#### Use Cases of Semaphore
- Database connections (limit to N connections).
- API rate-limiting (limit concurrent requests).
- Thread pools or task pools.
- Resource pools (e.g., file handles, network ports).


#### 🔁 Difference Between Lock and Semaphore

| **Feature**            | **Lock**                      | **Semaphore**                        |
|------------------------|-------------------------------|--------------------------------------|
| Access limit           | Only 1 task                   | Multiple tasks (n)                   |
| Use case               | Exclusive access              | Limited shared access                |
| Asyncio equivalent     | `asyncio.Lock()`              | `asyncio.Semaphore(n)`               |


### What is an Event?

- An Event is a flag-based synchronization primitive. 
  It acts like a signal between threads (or coroutines), letting one wait for something to happen — like a green light.


#### How It Works Internally
An Event object maintains an internal boolean flag:

- Initially False (meaning: no signal).
- `.wait()` blocks until the flag becomes `True`.
- `.set()` sets the flag to `True`, unblocking all waiting threads or coroutines.
- `.clear()` resets it to `False` again.


#### Use Cases of Event
- Wait for some condition to become true.
- Coordinate startup or shutdown between multiple threads/tasks.
- Trigger an action when some state is reached.



#### 🔁 Event vs Lock vs Semaphore

| **Feature**       | **Event**                       | **Lock**             | **Semaphore**               |
|-------------------|----------------------------------|-----------------------|-----------------------------|
| Purpose           | Signal/waiting for a flag        | Exclusive access      | Limit concurrent access     |
| Blocks?           | Yes, until `set()`               | Yes, until acquired   | Yes, until count > 0        |
| Manual reset?     | Yes (`clear()`)                  | No (auto)             | No (auto)                   |
