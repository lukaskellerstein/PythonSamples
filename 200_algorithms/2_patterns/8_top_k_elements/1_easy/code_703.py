
# -----------------------
# Kth Largest Element in a Stream (LeetCode 703)
# -----------------------

# Difficulty: Easy

# Problem: Design a class to find the kth largest element in a stream.
# Note that it is the kth largest element in the sorted order, not the
# kth distinct element.
# Implement KthLargest class:
#   - KthLargest(int k, int[] nums) Initializes the object with the integer k
#     and the stream of integers nums.
#   - int add(int val) Appends the integer val to the stream and returns the
#     element representing the kth largest element in the stream.

# -----------------------
# VISUALIZATION
# -----------------------
#
# k = 3, nums = [4, 5, 8, 2]
#
# Min-heap of size k=3 keeps the 3 largest elements:
# Initial: sort -> [2, 4, 5, 8], keep top 3 -> heap = [5, 8, 5] min-heap = [5, 5, 8]
# Actually: heapify [4, 5, 8, 2] -> pop until size=3 -> heap = [4, 5, 8]
#
# add(3):  heap=[4,5,8], 3 < 4(min) -> skip, return 4
# add(5):  heap=[4,5,8], push 5, pop min -> heap=[5,5,8], return 5
# add(10): heap=[5,5,8], push 10, pop min -> heap=[5,8,10], return 5
# add(9):  heap=[5,8,10], push 9, pop min -> heap=[8,9,10], return 8
# add(4):  heap=[8,9,10], 4 < 8(min) -> skip, return 8
#
# -----------------------

import heapq
from typing import List


# ----------------------------------------------------
# Min-Heap solution (Optimal)
#
# time complexity = O(n log k) init + O(log k) per add
# space complexity = O(k) - heap of size k
# ----------------------------------------------------

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)

        # Keep only the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)

        if len(self.heap) > self.k:
            heapq.heappop(self.heap)

        return self.heap[0]


# Example
kl = KthLargest(3, [4, 5, 8, 2])
print(kl.add(3))   # 4
print(kl.add(5))   # 5
print(kl.add(10))  # 5
print(kl.add(9))   # 8
print(kl.add(4))   # 8


# ----------------------------------------------------
# Brute Force solution (Sort on every add)
#
# time complexity = O(n log n) per add
# space complexity = O(n) - storing all elements
# ----------------------------------------------------

class KthLargestBruteForce:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        
        # ascending 1,2,3
        # self.nums.sort()

        # descending 3,2,1
        self.nums.sort(reverse=True)

        return self.nums[self.k - 1]


# Example
kl_bf = KthLargestBruteForce(3, [4, 5, 8, 2])
print(kl_bf.add(3))   # 4
print(kl_bf.add(5))   # 5
print(kl_bf.add(10))  # 5
print(kl_bf.add(9))   # 8
print(kl_bf.add(4))   # 8


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    print("\nKth Largest Element in Stream Results:")
    print("-" * 45)

    # Test case 1: k=3
    kl1 = KthLargest(3, [4, 5, 8, 2])
    kl2 = KthLargestBruteForce(3, [4, 5, 8, 2])
    adds = [3, 5, 10, 9, 4]
    print(f"k=3, init=[4,5,8,2]")
    print(f"{'add(val)':<12} {'Heap':<10} {'Brute':<10}")
    print("-" * 32)
    for val in adds:
        r1 = kl1.add(val)
        r2 = kl2.add(val)
        print(f"add({val})".ljust(12) + f"{r1}".ljust(10) + f"{r2}".ljust(10))

    # Test case 2: k=1
    print(f"\nk=1, init=[]")
    kl3 = KthLargest(1, [])
    kl4 = KthLargestBruteForce(1, [])
    adds2 = [-3, -2, -4, 0, 4]
    print(f"{'add(val)':<12} {'Heap':<10} {'Brute':<10}")
    print("-" * 32)
    for val in adds2:
        r1 = kl3.add(val)
        r2 = kl4.add(val)
        print(f"add({val})".ljust(12) + f"{r1}".ljust(10) + f"{r2}".ljust(10))
