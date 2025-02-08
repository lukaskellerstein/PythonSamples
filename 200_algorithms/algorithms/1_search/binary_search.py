# ----------------------------------
# ----------------------------------
# BINARY SEARCH
# divide and conquer algorithm.
#
# Time complexity: O(log n)
#
# SORTED Array/List !!!!
#
# https://www.geeksforgeeks.org/binary-search/
# ----------------------------------
# ----------------------------------

# --------------------------------------------
# RECURSIVE VERSION
# --------------------------------------------

def binary_search(arr, x, start, end):
    # Base condition
    if start > end:
        return False

    # Find the middle index
    mid = (start + end) // 2

    # Compare mid with the given key x
    if arr[mid] == x:
        return True

    # If element at mid is greater than x,
    # search in the left half of mid
    if arr[mid] > x:
        return binary_search(arr, x, start, mid - 1)
    else:
        # If element at mid is smaller than x,
        # search in the right half of mid
        return binary_search(arr, x, mid + 1, end)

# ----------------------------------
# ----------------------------------
# TEST CODE
search_value = 22
arr = [2, 5, 6, 7, 9, 14, 22, 34, 46, 50]

if binary_search(arr, search_value, 0, len(arr) - 1):
    print("Element found!")
else:
    print("Element not found!")
