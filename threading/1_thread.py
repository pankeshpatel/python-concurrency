# this is paralle processing at thread-level

import time
import threading

start = time.perf_counter()


def do_something():
    print("Sleeping...")
    time.sleep(1)
    print("Done sleeping")


# threading.Thread
# threading.Thread(target=do_something) creates a new thread object that, when started, runs the do_something function.
# Threads are lightweight processes that share the same memory space.
t1 = threading.Thread(target=do_something)
t2 = threading.Thread(target=do_something)


# .start()
# Starts the execution of the thread.
# The function do_something begins running concurrently with the main thread and other threads.
t1.start()
t2.start()

# Blocks the calling thread (main program) until the thread it’s called on finishes.
# Ensures that the program doesn't print "Finished..." until both threads are done.
t1.join()
t2.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start, 2)} seconds")


# 🚧 Important Detail: GIL (Global Interpreter Lock)
# Python has a GIL (in CPython, the default implementation), which means:
# Only one thread can execute Python bytecode at a time.
# But for I/O-bound tasks (like sleep, file reading, API calls), the GIL is released, allowing other threads to run.
# So in this case:
# While one thread is sleeping (waiting), the GIL is released.
# The other thread can run in parallel — that's why this program benefits from threading.
