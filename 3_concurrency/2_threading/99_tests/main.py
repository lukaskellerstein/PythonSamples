import threading
import os
import time
import numpy as np


def BasicOperation():
    # square of number
    def square(number):
        return number * number

    # cube of a number
    def cube(number):
        return number ** 3

    # nth power of a number
    def nth_power(number, power):
        return number ** power

    # sum of n numbers
    def sum_of_n_numbers(number):
        return number * (number + 1) / 2

    # using functions to drive a program ...
    print("square of 5 is ", square(5))
    print("cube of 5 is ", cube(5))
    print("5 raise to power 2 is ", nth_power(5, 2))
    print("sum of first 5 numbers is", sum_of_n_numbers(5))


def DotProduct():
    A = np.arange(1000000).reshape(5000, 200)
    B = np.arange(1000000).reshape(200, 5000)
    Dot = np.dot(A, B)
    print(Dot)


if __name__ == "__main__":
    # -----------------------------------
    # without threading ...
    # -----------------------------------
    start = time.time()
    BasicOperation()
    Mid = time.time() - start
    print("Mid time taken : ", Mid, "seconds")
    DotProduct()
    end = time.time() - start
    print("Full time taken : ", end, "seconds")

    # -----------------------------------
    # with threading ...
    # -----------------------------------
    start = time.time()
    Thread_1 = threading.Thread(target=BasicOperation, name=" Basic Operation Thread ")
    Thread_2 = threading.Thread(target=DotProduct, name=" Dot Product Thread ")
    Thread_1.start()
    Thread_2.start()

    # waint until thread_1 is finished, than continue
    Thread_1.join()
    Mid = time.time() - start
    print("Mid time taken : ", Mid, "seconds")

    # waint until thread_2 is finished, than continue
    Thread_2.join()
    end = time.time() - start
    print("Full time taken : ", end, "seconds")
