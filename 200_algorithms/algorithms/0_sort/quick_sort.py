# ----------------------------------
# ----------------------------------
# QUICK SORT
# A divide-and-conquer algorithm
#
# Time complexity: O(N log N)
# Space complexity: O(log N) for recursion
#
# https://www.geeksforgeeks.org/quick-sort/
# https://www.digitalocean.com/community/tutorials/js-quick-sort
# ----------------------------------
# ----------------------------------

# Helper function to swap two elements in an array
def swap(arr, first_index, second_index):
    arr[first_index], arr[second_index] = arr[second_index], arr[first_index]

# Partition function to rearrange elements around the pivot
def partition(arr, left, right):
    midpoint = (left + right) // 2
    pivot = arr[midpoint]

    # Continue partitioning while the left pointer is less than or equal to the right pointer
    while left <= right:
        # Move the left pointer to the right until an element greater than the pivot is found
        while arr[left] < pivot:
            left += 1

        # Move the right pointer to the left until an element smaller than the pivot is found
        while arr[right] > pivot:
            right -= 1

        # If pointers have not crossed, swap elements and move the pointers inward
        if left <= right:
            swap(arr, left, right)
            left += 1
            right -= 1

    return left

# Quick sort function
def quick_sort(arr, left, right):
    if left < right:
        # Partition the array and get the index where partitioning ends
        index = partition(arr, left, right)

        # Recursively apply quick sort to the left and right partitions
        quick_sort(arr, left, index - 1)
        quick_sort(arr, index, right)

    return arr

# ----------------------------------
# TEST
# ----------------------------------

arr = [5, 46, 34, 2, 6, 14, 9, 7, 50, 22]

print("Unsorted Array:", arr)

# Call the quick sort function
sorted_arr = quick_sort(arr, 0, len(arr) - 1)

print("Sorted Array:", sorted_arr)
