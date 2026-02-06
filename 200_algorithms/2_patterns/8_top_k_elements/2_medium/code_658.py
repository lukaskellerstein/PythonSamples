
# -----------------------
# Find K Closest Elements (LeetCode 658)
# -----------------------

# Difficulty: Medium

# Problem: Given a sorted integer array arr, two integers k and x, return the k
# closest integers to x in the array. The result should also be sorted in
# ascending order.
#
# An integer a is closer to x than an integer b if:
# - |a - x| < |b - x|, or
# - |a - x| == |b - x| and a < b

# -----------------------

# Example:
# arr = [1,2,3,4,5], k = 4, x = 3 -> [1,2,3,4]
# arr = [1,1,2,3,4,5], k = 4, x = -1 -> [1,1,2,3]

# ----------------------------------------------------
# Binary Search solution (Optimal)
#
# time complexity = O(log(n-k) + k) - binary search + building result
# space complexity = O(1) - excluding output array
#
# Idea: Binary search for the left boundary of the k-element window.
# Compare arr[mid] and arr[mid+k] to decide which side is closer to x.
# ----------------------------------------------------


def find_closest_elements(arr, k, x):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2

        # Compare distance from x to arr[mid] vs arr[mid + k]
        # If arr[mid] is farther, move left boundary right
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid

    return arr[left:left + k]


# Example
print(find_closest_elements([1, 2, 3, 4, 5], 4, 3))  # [1, 2, 3, 4]
print(find_closest_elements([1, 1, 2, 3, 4, 5], 4, -1))  # [1, 1, 2, 3]
print(find_closest_elements([1, 2, 3, 4, 5], 4, -1))  # [1, 2, 3, 4]


# ----------------------------------------------------
# Two Pointers solution (Optimal Alternative)
#
# time complexity = O(n - k) - shrink from both ends
# space complexity = O(1) - excluding output array
#
# Idea: Start with the full array, remove elements from ends until k remain.
# ----------------------------------------------------


def find_closest_elements_two_pointers(arr, k, x):
    left = 0
    right = len(arr) - 1

    # Remove elements until we have exactly k elements
    while right - left >= k:
        # Compare distances from x
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        elif abs(arr[left] - x) < abs(arr[right] - x):
            right -= 1
        else:
            # Equal distance, prefer smaller element (left)
            right -= 1

    return arr[left:right + 1]


# Example
print(find_closest_elements_two_pointers([1, 2, 3, 4, 5], 4, 3))  # [1, 2, 3, 4]
print(find_closest_elements_two_pointers([1, 1, 2, 3, 4, 5], 4, -1))  # [1, 1, 2, 3]
print(find_closest_elements_two_pointers([1, 2, 3, 4, 5], 4, -1))  # [1, 2, 3, 4]


# ----------------------------------------------------
# Heap solution
#
# time complexity = O(n log k) - heap operations for each element
# space complexity = O(k) - heap size
#
# Idea: Use max-heap to keep track of k closest elements.
# ----------------------------------------------------

import heapq


def find_closest_elements_heap(arr, k, x):
    # Max heap: store (-distance, -value) to get farthest element at top
    # We use -value to handle tie-breaking (prefer smaller values)
    heap = []

    for num in arr:
        dist = abs(num - x)
        # Push (-distance, -num) so larger distances and larger nums pop first
        heapq.heappush(heap, (-dist, -num))

        if len(heap) > k:
            heapq.heappop(heap)

    # Extract elements and sort
    result = [-item[1] for item in heap]
    result.sort()
    return result


# Example
print(find_closest_elements_heap([1, 2, 3, 4, 5], 4, 3))  # [1, 2, 3, 4]
print(find_closest_elements_heap([1, 1, 2, 3, 4, 5], 4, -1))  # [1, 1, 2, 3]
print(find_closest_elements_heap([1, 2, 3, 4, 5], 4, -1))  # [1, 2, 3, 4]


# ----------------------------------------------------
# Brute Force solution (Sort by Distance)
#
# time complexity = O(n log n) - sorting all elements by distance
# space complexity = O(n) - storing all elements with distances
# ----------------------------------------------------


def find_closest_elements_brute_force(arr, k, x):
    # Sort by distance to x, then by value for tie-breaking
    sorted_by_distance = sorted(arr, key=lambda num: (abs(num - x), num))

    # Take first k elements and sort them
    result = sorted_by_distance[:k]
    result.sort()
    return result


# Example
print(find_closest_elements_brute_force([1, 2, 3, 4, 5], 4, 3))  # [1, 2, 3, 4]
print(find_closest_elements_brute_force([1, 1, 2, 3, 4, 5], 4, -1))  # [1, 1, 2, 3]
print(find_closest_elements_brute_force([1, 2, 3, 4, 5], 4, -1))  # [1, 2, 3, 4]
