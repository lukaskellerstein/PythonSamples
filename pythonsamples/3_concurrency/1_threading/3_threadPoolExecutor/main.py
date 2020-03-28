import logging
import threading
import time
from concurrent.futures import ThreadPoolExecutor


def thread_function(name, timeout):
    print(name)
    logging.info("Thread %s: starting", name)
    time.sleep(timeout)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":

    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

    # Context manager (with) for ThreadPoolExecutor
    with ThreadPoolExecutor(max_workers=10) as executor:
        task1 = executor.submit(thread_function, "A", 2)
        task2 = executor.submit(thread_function, "B", 2)

    logging.info(f"Main    : amount of threads - {threading.active_count()}")
    [print(t) for t in threading.enumerate()]
    logging.info("Main    : all done")
