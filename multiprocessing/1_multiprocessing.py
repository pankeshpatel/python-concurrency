import multiprocessing
import multiprocessing.process
import time


def do_something():
    print("Sleeping 1 second")
    time.sleep(1)
    print("Done sleeping")


if __name__ == "__main__":

    process_list = []

    start = time.perf_counter()

    for _ in range(0, 10):
        p = multiprocessing.Process(target=do_something)
        p.start()
        process_list.append(p)

    for p in process_list:
        p.join()

    # p1 = multiprocessing.Process(target=do_something)
    # p2 = multiprocessing.Process(target=do_something)

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
