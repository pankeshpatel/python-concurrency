import multiprocessing
import time


def do_something(seconds):
    print(f"Sleeping {seconds} second")
    time.sleep(seconds)
    print("Done sleeping")


if __name__ == "__main__":

    process_list = []

    start = time.perf_counter()

    for _ in range(0, 10):
        p = multiprocessing.Process(target=do_something, args=[1.5])  # arguments
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
