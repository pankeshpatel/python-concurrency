### What is an Event Loop?

The event loop is the heart of asyncio.

It’s like a task manager in your program that keeps checking:

- “Is anything ready to run now?”
- “Is anything done waiting?”
- “If so, let’s run it!”

It runs in a loop, picking tasks to run, pausing them when they’re waiting, and resuming them when ready.

### Simple Analogy: A Cook in a Kitchen

Imagine a cook (the event loop) preparing three dishes (tasks):

- 🍳 Dish 1: Needs to cook on the stove for 5 minutes.
- 🥗 Dish 2: Just needs chopping.
- 🍝 Dish 3: Needs to boil for 3 minutes.

If the cook waits for each one to finish before starting the next, it’s slow.

But instead:

- He starts Dish 1, puts it on the stove → ⏳ (waits to cook)
- While it cooks, he works on Dish 2
- Then puts Dish 3 to boil → ⏳
- Goes back to Dish 1 when it’s ready
- And so on…

⚡ He’s juggling tasks efficiently, never just standing around.
That’s exactly what the event loop does.


✅ **Key Features of Event Loop**

| Feature             | Meaning                                           |
|---------------------|---------------------------------------------------|
| **Single thread**   | Runs in one thread (by default)                   |
| **Schedules tasks** | Starts, pauses, resumes coroutines                |
| **Never blocks**    | Only switches tasks when one is *waiting*         |
| **Runs forever**    | Until all tasks are done or loop is stopped       |

```python

Start 
  |
  V
+----------------------+
|  Event Loop Starts   |
+----------------------+
          |
          V
+-------------------------------+
| Are there pending tasks?     |
+-------------------------------+
          | Yes
          V
+-------------------------------------------+
| Pick the next task that is ready to run   |
+-------------------------------------------+
          |
          V
+-------------------------------+
| Run the task until it 'await's|
+-------------------------------+
          |
          V
+-------------------------------------------+
| Save task state and return to event loop  |
+-------------------------------------------+
          |
          V
+---------------------------+
| Check if any tasks are now|
| ready to resume (done I/O)|
+---------------------------+
          |
          V
+--------------------+
| Continue the loop  |
+--------------------+
          |
         ...
      (Loop continues)

```

#### What's Happening Here?
- The event loop `runs forever`, checking for tasks to run.
- When a task hits an await, it yields control back to the event loop.
- The loop then picks the next ready task and starts/resumes it.
- Once tasks are done, the loop eventually stops.
