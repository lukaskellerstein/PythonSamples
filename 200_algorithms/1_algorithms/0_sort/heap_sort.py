# ----------------------------------
# ----------------------------------
# HEAP SORT
# Uses a MinHeap data structure to sort the array
#
# Time complexity: O(N log N)
# Space complexity: O(N)
#
# https://www.geeksforgeeks.org/heap-sort/
# ----------------------------------
# ----------------------------------

# time complexity - O(n log n)
# Space complexity - O(n)


# Hack to access the code outside this folder
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from data_structures.non_linear_data_structures.my_heap.min_heap import MyMinHeap

# Heap sort function
def heap_sort(arr):
    # Step 1: Create a MinHeap and insert all elements from the array
    min_heap = MyMinHeap()
    for value in arr:
        min_heap.insert(value)

    # Step 2: Extract elements one by one in sorted order
    sorted_array = []
    while len(min_heap.arr) > 0:
        # Always remove the root of the heap, which is the smallest element
        sorted_array.append(min_heap.arr[0])
        min_heap.remove(min_heap.arr[0])

    return sorted_array

# ----------------------------------
# TEST
# ----------------------------------

arr = [5, 46, 34, 2, 6, 14, 9, 7, 50, 22]

print("Original Array:", arr)

# Call the heap sort function
sorted_arr = heap_sort(arr)

print("Sorted Array:", sorted_arr)


# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------

# In-place variant

# time complexity - O(n log n)
# Space complexity - O(1)