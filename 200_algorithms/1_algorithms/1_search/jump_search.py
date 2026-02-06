# ----------------------------------
# ----------------------------------
# JUMP SEARCH
#
# Time complexity: O(√n)
#
# SORTED Array/List !!!!
#
# https://www.geeksforgeeks.org/jump-search/
# ----------------------------------
# ----------------------------------

import math

def jump_search(array_to_search, value_to_search):
    length = len(array_to_search)
    step_size = math.floor(math.sqrt(length))

    lower_bound = 0
    step = step_size

    # Finding the block where the value might be present
    while array_to_search[min(step, length) - 1] < value_to_search:
        lower_bound = step
        step += step_size
        if lower_bound >= length:
            return -1

    # Linear search within the block
    upper_bound = min(step, length)
    while lower_bound < upper_bound and array_to_search[lower_bound] < value_to_search:
        lower_bound += 1

    # Check if the element is found
    if lower_bound < length and array_to_search[lower_bound] == value_to_search:
        return lower_bound

    return -1

# ----------------------------------
# ----------------------------------
# TEST CODE
search_value = 22
arr = [2, 5, 6, 7, 9, 14, 22, 34, 46, 50]

position = jump_search(arr, search_value)
if position != -1:
    print("Found at position:", position)
else:
    print("Value not found")
