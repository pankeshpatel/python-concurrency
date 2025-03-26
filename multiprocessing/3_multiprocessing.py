import concurrent.futures
import time


def do_something(seconds):
    print(f"Sleeping {seconds} second")
    time.sleep(seconds)
    return f"Do Something..{seconds}"


if __name__ == "__main__":

    process_list = []

    start = time.perf_counter()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs = [5, 4, 3, 2, 1]
        # results = [executor.submit(do_something, sec) for sec in secs]

        # for f in concurrent.futures.as_completed(results):
        #     print(f.result())

        results = executor.map(do_something, secs)
        for result in results:
            print(result)

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
