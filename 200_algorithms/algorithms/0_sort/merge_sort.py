# ----------------------------------
# ----------------------------------
# MERGE SORT
# A divide-and-conquer algorithm
#
# Default sort() in JavaScript uses merge sort in Mozilla Firefox and Safari
#
# Time complexity: O(N log N)
# Space complexity: O(N)
#
# https://www.geeksforgeeks.org/merge-sort/
# ----------------------------------
# ----------------------------------

# Helper function to merge two sorted arrays
def merge(left, right):
    result = []

    # Compare elements from both arrays and add the smallest one to `result`
    while left and right:
        if left[0] > right[0]:
            result.append(right.pop(0))  # Remove and add the smallest element from `right`
        else:
            result.append(left.pop(0))   # Remove and add the smallest element from `left`

    # Concatenate any remaining elements from `left` or `right`
    return result + left + right

# Testing the merge helper function
arr1 = [2, 5, 10, 57]
arr2 = [9, 12, 13]
print("Merged array:", merge(arr1, arr2))

# Merge sort function
def merge_sort(arr):
    # Base case: If the array has 1 or no elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the midpoint to divide the array into two halves
    midpoint = len(arr) // 2

    # Recursively sort both halves
    left_ordered = merge_sort(arr[:midpoint])
    right_ordered = merge_sort(arr[midpoint:])

    # Merge the sorted halves
    return merge(left_ordered, right_ordered)

# ----------------------------------
# TEST
# ----------------------------------

arr = [5, 46, 34, 2, 6, 14, 9, 7, 50, 22]

print("Original array:", arr)

# Call the merge sort function
sorted_arr = merge_sort(arr)

print("Sorted array:", sorted_arr)
