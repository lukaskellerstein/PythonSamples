
# -----------------------
# Kth Largest Element in an Array (LeetCode 215)
# -----------------------

# Difficulty: Medium

# Problem: Given an integer array nums and an integer k, return the kth largest
# element in the array. Note that it is the kth largest element in the sorted
# order, not the kth distinct element.

# -----------------------

# For given array [3,2,1,5,6,4] and k=2, return the 2nd largest element.
nums = [3, 2, 1, 5, 6, 4]
k = 2

# ----------------------------------------------------
# Min-Heap solution
#
# time complexity = O(n log k) - push/pop on heap of size k for each element
# space complexity = O(k) - heap stores at most k elements
# ----------------------------------------------------

import heapq


def find_kth_largest(nums, k):
    # Min-heap of size k — the root is always the kth largest
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        # If heap exceeds size k, remove the smallest
        if len(heap) > k:
            heapq.heappop(heap)

    # The root of the min-heap is the kth largest element
    return heap[0]


# Example
print(find_kth_largest(nums, k))  # 5


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n log n) - sorting the entire array
# space complexity = O(n) - sorted copy of the array
# ----------------------------------------------------


def find_kth_largest_brute_force(nums, k):
    # Sort in descending order and pick the kth element
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k - 1]


# Example
print(find_kth_largest_brute_force(nums, k))  # 5
