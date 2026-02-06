from typing import List


# ============================================================
# PROBLEM: Range Sum Query - Immutable (LeetCode 303)
# ============================================================
# Difficulty: Easy
# Pattern: Prefix Sum
#
# Given an integer array nums, implement a class that handles
# multiple queries to calculate the sum of elements between
# indices left and right (inclusive). The array does not change
# between queries.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#          query: sumRange(2, 6)
#   Output: 25
#   Explanation: 3 + 4 + 5 + 6 + 7 = 25
#
# Example 2:
#   Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#          query: sumRange(0, 0)
#   Output: 1
#   Explanation: Only element at index 0.
#
# Example 3:
#   Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#          query: sumRange(0, 9)
#   Output: 55
#   Explanation: Sum of all elements 1 through 10.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= nums.length <= 10^4
# - -10^5 <= nums[i] <= 10^5
# - 0 <= left <= right < nums.length
# - At most 10^4 calls will be made to sumRange
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums:         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index:         0  1  2  3  4  5  6  7  8   9
#
# prefix_sum: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
# index:       0  1  2  3   4   5   6   7   8   9  10
#
# sumRange(2, 6) = prefix_sum[7] - prefix_sum[2] = 28 - 3 = 25
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???) init, O(???) per query
# Space Complexity: O(???)


class NumArrayBruteForce:

    def __init__(self, nums: List[int]):
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Prefix Sum)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???) init, O(???) per query
# Space Complexity: O(???)


class NumArray:

    def __init__(self, nums: List[int]):
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    test_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    test_queries = [
        (0, 0),   # Expected: 1
        (0, 9),   # Expected: 55
        (2, 6),   # Expected: 25
        (5, 8),   # Expected: 30
    ]

    pass
