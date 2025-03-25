import time
import threading

start = time.perf_counter()


def do_something(id):
    print(f"sleeping 1 second...{id}")
    time.sleep(1)
    print(f"Done sleeping...{id}")


threads = []

for i in range(0, 10):
    t = threading.Thread(target=do_something, args=(i,))
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")
