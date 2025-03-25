#### What Does “Non-Blocking Code” Mean?

Normally, when a function does something like:

- calling an API
- reading from a file
- querying a database

It blocks (i.e., stops) the whole program until that action is complete.

```python
import requests

def get_data():
    response = requests.get("https://example.com")
    print(response.text)

# This blocks until response is received
```
So if you had 100 such calls, your program would wait for each one to finish one-by-one — very slow!

#### Non-Blocking Code

- Non-blocking code does not stop your program while waiting. It allows your program to continue running other tasks.
- With non-blocking libraries, like `aiohttp`, you can write code that "pauses" using `await` but lets the event loop keep going in the background.

```python
import aiohttp
import asyncio

async def get_data():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://example.com") as response:
            text = await response.text()
            print(text)

asyncio.run(get_data())
```

Here:

- `await` tells Python: "I'm waiting here, but you can run other stuff in the meantime."
- `aiohttp` is built using non-blocking sockets under the hood.
- No thread is blocked, so other tasks can continue.


Non-blocking code allows multiple operations to happen at the same time in one thread — it's the backbone of efficient asyncio apps.