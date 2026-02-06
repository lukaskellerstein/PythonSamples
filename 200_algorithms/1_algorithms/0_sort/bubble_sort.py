# ----------------------------------
# ----------------------------------
# BUBBLE SORT
# Simplest sorting algorithm, but inefficient for large datasets
#
# Time complexity: O(N²)
#
# https://www.geeksforgeeks.org/bubble-sort/
# ----------------------------------
# ----------------------------------

# Nested for-loop (non-optimized) version
def bubble_sort1(arr):
    arr_length = len(arr)
    last_index = arr_length - 1

    # Outer loop to traverse the entire array multiple times
    for i in range(arr_length):
        # Inner loop to compare adjacent elements
        for j in range(last_index - i):
            current_value = arr[j]
            next_value = arr[j + 1]

            # Swap if the current element is greater than the next
            if current_value > next_value:
                arr[j], arr[j + 1] = next_value, current_value

# Iterative (optimized) version with a 'swapped' variable
def bubble_sort2(arr):
    n = len(arr)

    # Outer loop continues until no more swaps are needed
    for i in range(n - 1):
        swapped = False

        # Inner loop for adjacent comparisons and swaps
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                # Swap elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps were made, array is already sorted
        if not swapped:
            break

    return arr

# Recursive version of bubble sort
def bubble_sort3(arr, n):
    # Base case: if the array size is 1, it's already sorted
    if n == 1:
        return

    # One pass of bubble sort, bubbling the largest element to the end
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            # Swap adjacent elements if they are in the wrong order
            arr[i], arr[i + 1] = arr[i + 1], arr[i]

    # Recursive call for the rest of the array
    bubble_sort3(arr, n - 1)

# ----------------------------------
# TEST
# ----------------------------------

arr = [5, 46, 34, 2, 6, 14, 9, 7, 50, 22]

print("Original array:", arr)

# Uncomment the version you want to test
# bubble_sort1(arr)
# bubble_sort2(arr)
bubble_sort3(arr, len(arr))

print("Sorted array:", arr)
