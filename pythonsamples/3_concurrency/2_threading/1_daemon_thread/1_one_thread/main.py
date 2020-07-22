import logging
import threading
import time

# -------------------------------------------------------------
# Threads that are daemons, are just killed
# wherever they are when the program is exiting.
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
    t1 = threading.Thread(
        name="my-daemon-thread", target=thread_function, args=("A"), daemon=True
    )
    logging.info("Main    : before running thread")
    t1.start()
    # --------------------------------------------------------------

    logging.info(f"Main    : amount of threads - {threading.active_count()}")
    [print(t) for t in threading.enumerate()]
    logging.info("Main    : all done")
