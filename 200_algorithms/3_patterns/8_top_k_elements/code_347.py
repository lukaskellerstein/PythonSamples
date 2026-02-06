
# -----------------------
# Top K Frequent Elements (LeetCode 347)
# -----------------------

# Difficulty: Medium

# Problem: Given an integer array nums and an integer k, return the k most
# frequent elements. You may return the answer in any order. It is guaranteed
# that the answer is unique.

# -----------------------

# For given array [1,1,1,2,2,3] and k=2, return the 2 most frequent elements.
nums = [1, 1, 1, 2, 2, 3]
k = 2

# ----------------------------------------------------
# HashMap + Min-Heap solution
#
# time complexity = O(n log k) - count frequencies O(n), heap operations O(n log k)
# space complexity = O(n) - hashmap stores up to n entries
# ----------------------------------------------------

import heapq
from collections import Counter


def top_k_frequent(nums, k):
    # Count frequency of each element
    count = Counter(nums)

    # Use a min-heap of size k — keeps the k most frequent
    heap = []

    for num, freq in count.items():
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for freq, num in heap]


# Example
print(top_k_frequent(nums, k))  # [1, 2]


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n log n) - counting O(n), sorting all frequencies O(n log n)
# space complexity = O(n) - hashmap stores up to n entries
# ----------------------------------------------------


def top_k_frequent_brute_force(nums, k):
    # Count frequency of each element
    count = Counter(nums)

    # Sort by frequency in descending order and take first k
    sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return [num for num, freq in sorted_items[:k]]


# Example
print(top_k_frequent_brute_force(nums, k))  # [1, 2]
