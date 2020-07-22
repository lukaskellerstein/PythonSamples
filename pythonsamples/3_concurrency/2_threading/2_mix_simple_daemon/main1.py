import logging
import threading
import time

# -------------------------------------------------------------
# If a program is running simple Threads,
# then the program will wait for those threads to complete before it terminates.
# -------------------------------------------------------------


def thread_function(name, timeout):
    logging.info("Thread %s: starting", name)
    time.sleep(timeout)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")

    # FIRST THREAD
    # --------------------------------------------------------------
    t1 = threading.Thread(name="my-thread-1", target=thread_function, args=("A", 5))
    logging.info("Main    : before running thread-1")
    t1.start()
    # --------------------------------------------------------------

    # SECOND THREAD
    # --------------------------------------------------------------
    t2 = threading.Thread(
        name="my-thread-2", target=thread_function, args=("B", 2), daemon=True
    )
    logging.info("Main    : before running thread-2")
    t2.start()
    # --------------------------------------------------------------

    # !!!!!!!!!!!!!!!!!!!!!!!!
    # Because non-daemon thread is 5sec and daemon is 2sec. We dont have to wait to
    # daemon thread to end
    # !!!!!!!!!!!!!!!!!!!!!!!!

    logging.info(f"Main    : amount of threads - {threading.active_count()}")
    [print(t) for t in threading.enumerate()]
    logging.info("Main    : all done")
