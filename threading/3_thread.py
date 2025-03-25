import time
import concurrent.futures

start = time.perf_counter()


def do_something(id):
    print(f"sleeping 1 second...{id}")
    time.sleep(1)
    return "Done sleeping..."


# concurrent.futures.ThreadPoolExecutor()
# This creates a pool of worker threads.
# By default, it picks the number of threads based on your CPU, but you can set it manually with max_workers=....
with concurrent.futures.ThreadPoolExecutor() as executor:
    # executor.submit(do_something, id)
    # This submits a task to be run asynchronously in a thread.
    # It returns a Future object, which represents the eventual result.
    results = [executor.submit(do_something, id) for id in range(0, 10)]

    # This is a generator that yields each Future as soon as it’s done, not in order of submission.
    # It's efficient: you don’t wait for all to finish before printing results.
    for f in concurrent.futures.as_completed(results):
        # Retrieves the actual return value from the function once the thread completes.
        print(f.result())

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
