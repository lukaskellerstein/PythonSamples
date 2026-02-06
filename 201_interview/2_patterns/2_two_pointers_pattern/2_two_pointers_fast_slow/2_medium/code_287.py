from typing import List


# ============================================================
# PROBLEM: Find the Duplicate Number (LeetCode 287)
# ============================================================
# Difficulty: Medium
# Pattern: Fast/Slow Pointers (Floyd's Cycle Detection)
#
# Given an array of integers nums containing n + 1 integers
# where each integer is in the range [1, n] inclusive, there
# is only one repeated number. Return this repeated number.
# You must solve it without modifying the array and using
# only constant extra space.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1, 3, 4, 2, 2]
#   Output: 2
#   Explanation: 2 appears twice in the array.
#
# Example 2:
#   Input: nums = [3, 1, 3, 4, 2]
#   Output: 3
#   Explanation: 3 appears twice in the array.
#
# Example 3:
#   Input: nums = [3, 3, 3, 3, 3]
#   Output: 3
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= n <= 10^5
# - nums.length == n + 1
# - 1 <= nums[i] <= n
# - There is only one repeated number, but it could be repeated
#   more than once
# - You must NOT modify the array
# - You must use only O(1) extra space
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums = [1, 3, 4, 2, 2]
#
# Treat array as linked list: index -> nums[index]
#   0 -> 1 -> 3 -> 2 -> 4 -> 2 -> 4 -> 2 ...
#                   ^              |
#                   +--------------+
#
# The duplicate number (2) is the entrance to the cycle.
#
# Floyd's Cycle Detection:
#   Phase 1: Find meeting point inside cycle
#     slow = nums[slow], fast = nums[nums[fast]]
#   Phase 2: Find cycle entrance (the duplicate)
#     Reset slow to start, move both at same speed
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def find_duplicate_brute_force(nums: List[int]) -> int:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Floyd's Cycle Detection)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def find_duplicate(nums: List[int]) -> int:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    test_cases = [
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 1, 2], 1),
    ]

    pass
