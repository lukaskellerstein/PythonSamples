# ----------------------------------
# ----------------------------------
# INSERTION SORT
# Similar to sorting cards in hand
#
# Default sort() in JavaScript uses insertion sort in Chrome's V8 engine 
# for small arrays (<= 10 elements)
#
# Time complexity: O(N²)
# Space complexity: O(1)
#
# https://www.geeksforgeeks.org/insertion-sort/
# ----------------------------------
# ----------------------------------

def insertion_sort(arr):
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        current = arr[i]
        left_index = i - 1

        # Shift elements to the right to create space for `current`
        while left_index >= 0 and arr[left_index] > current:
            arr[left_index + 1] = arr[left_index]
            left_index -= 1

        # Insert `current` into its correct position
        arr[left_index + 1] = current

# ----------------------------------
# TEST
# ----------------------------------

arr = [5, 46, 34, 2, 6, 14, 9, 7, 50, 22]

print("Original array:", arr)

# Call the insertion sort function
insertion_sort(arr)

print("Sorted array:", arr)
