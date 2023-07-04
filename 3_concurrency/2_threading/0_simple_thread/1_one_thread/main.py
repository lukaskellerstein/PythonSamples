import logging
import threading
import time

# -------------------------------------------------------------
# If a program is running simple Threads,
# then the program will wait for those threads to complete before it terminates.
# -------------------------------------------------------------


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

    # --------------------------------------------------------------
    t1 = threading.Thread(name="my-thread", target=thread_function, args=("A"))
    logging.info("Main    : before running thread")
    t1.start()
    # --------------------------------------------------------------

    logging.info(f"Main    : amount of threads - {threading.active_count()}")
    [print(t) for t in threading.enumerate()]
    logging.info("Main    : all done")
