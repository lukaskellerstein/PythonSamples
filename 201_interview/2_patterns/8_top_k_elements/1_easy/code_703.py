from typing import List

# ============================================================
# PROBLEM: Kth Largest Element in a Stream (LeetCode 703)
# ============================================================
# Difficulty: Easy
# Pattern: Top K Elements
#
# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
#
# Implement the KthLargest class:
#   - KthLargest(int k, int[] nums) initializes the object with the integer k
#     and the stream of integers nums.
#   - int add(int val) appends the integer val to the stream and returns the
#     element representing the kth largest element in the stream.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input:
#     KthLargest(3, [4, 5, 8, 2])
#     add(3)  -> 4
#     add(5)  -> 5
#     add(10) -> 5
#     add(9)  -> 8
#     add(4)  -> 8
#   Explanation:
#     After init, stream = [4,5,8,2]. Top 3 largest = [4,5,8], 3rd largest = 4.
#     add(3):  stream=[2,3,4,5,8],   3rd largest = 4
#     add(5):  stream=[2,3,4,5,5,8], 3rd largest = 5
#     add(10): stream=[2,3,4,5,5,8,10], 3rd largest = 5
#     add(9):  stream=[2,3,4,5,5,8,9,10], 3rd largest = 8
#     add(4):  stream=[2,3,4,4,5,5,8,9,10], 3rd largest = 8
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= k <= 10^4
# - 0 <= nums.length <= 10^4
# - -10^4 <= nums[i] <= 10^4
# - -10^4 <= val <= 10^4
# - At most 10^4 calls will be made to add
# - It is guaranteed that there will be at least k elements when you search for the kth element
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# k = 3, nums = [4, 5, 8, 2]
#
# Min-heap of size k=3 keeps the 3 largest elements:
#
#   Init:  heap = [4, 5, 8]  (2 is removed as smallest)
#          kth largest (heap top) = 4
#
#   add(3):  3 < 4 (heap min) -> don't add -> heap = [4, 5, 8]  -> return 4
#   add(5):  push 5 -> [4,5,5,8] -> pop min -> heap = [5, 5, 8] -> return 5
#   add(10): push 10 -> [5,5,8,10] -> pop min -> heap = [5,8,10] -> return 5
#   add(9):  push 9 -> [5,8,9,10] -> pop min -> heap = [8,9,10]  -> return 8
#   add(4):  4 < 8 (heap min) -> don't add -> heap = [8, 9, 10]  -> return 8
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???) for __init__, O(???) for add
# Space Complexity: O(???)


class KthLargestBruteForce:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???) for __init__, O(???) for add
# Space Complexity: O(???)


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1: Basic usage with k=3
    kl = KthLargest(3, [4, 5, 8, 2])
    assert kl.add(3) == 4
    assert kl.add(5) == 5
    assert kl.add(10) == 5
    assert kl.add(9) == 8
    assert kl.add(4) == 8

    # Test case 2: Brute force with k=3
    kl_bf = KthLargestBruteForce(3, [4, 5, 8, 2])
    assert kl_bf.add(3) == 4
    assert kl_bf.add(5) == 5
    assert kl_bf.add(10) == 5
    assert kl_bf.add(9) == 8
    assert kl_bf.add(4) == 8

    # Test case 3: k=1, empty init
    kl2 = KthLargest(1, [])
    assert kl2.add(-3) == -3
    assert kl2.add(-2) == -2
    assert kl2.add(-4) == -2
    assert kl2.add(0) == 0
    assert kl2.add(4) == 4

    print("All test cases passed!")
