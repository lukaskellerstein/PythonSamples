from concurrent.futures import ThreadPoolExecutor
import threading
import random

# WORKS ONLY WITH METHOD WITHOUT PARAMETERS
def aaa():
    print("AAAA")


def bbb():
    print("BBBB")


if __name__ == "__main__":

    # without Context manager
    executor = ThreadPoolExecutor(max_workers=3)
    # WORKS ONLY WITH METHOD WITHOUT PARAMETERS
    task1 = executor.submit(aaa)
    task2 = executor.submit(bbb)
