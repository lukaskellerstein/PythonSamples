# ----------------------------------
# ----------------------------------
# SELECTION SORT
#
# Time complexity: O(N²)
# Space complexity: O(1)
#
# https://www.geeksforgeeks.org/selection-sort-algorithm-2/
# ----------------------------------
# ----------------------------------

def selection_sort(array):
    n = len(array)

    # Outer loop for traversing each element of the array
    for i in range(n - 1):
        # Assume the minimum element is at the current position
        min_index = i

        # Inner loop to find the minimum element in the unsorted part of the array
        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of the unsorted part
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]

    return array

# ----------------------------------
# TEST
# ----------------------------------

arr = [5, 46, 34, 2, 6, 14, 9, 7, 50, 22]

print("Original array:", arr)

# Call the selection sort function
selection_sort(arr)

print("Sorted array:", arr)
