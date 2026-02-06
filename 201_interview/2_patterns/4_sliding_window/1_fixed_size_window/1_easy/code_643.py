from typing import List


# ============================================================
# PROBLEM: Maximum Average Subarray I (LeetCode 643)
# ============================================================
# Difficulty: Easy
# Pattern: Sliding Window (Fixed Size)
#
# Given an integer array nums and an integer k, find the contiguous
# subarray of length k that has the maximum average value, and return
# this value. You must find a subarray of exactly length k.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1, 12, -5, -6, 50, 3], k = 4
#   Output: 12.75
#   Explanation: Maximum average is (12 + (-5) + (-6) + 50) / 4 = 12.75
#
# Example 2:
#   Input: nums = [5], k = 1
#   Output: 5.0
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - n == nums.length
# - 1 <= k <= n <= 10^5
# - -10^4 <= nums[i] <= 10^4
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums = [1, 12, -5, -6, 50, 3],  k = 4
#
# Window 1: [1, 12, -5, -6]  -> sum =  2,  avg = 0.50
# Window 2: [12, -5, -6, 50] -> sum = 51,  avg = 12.75  <-- max
# Window 3: [-5, -6, 50,  3] -> sum = 42,  avg = 10.50
#
# Sliding: remove leftmost, add rightmost each step.
#


# ============================================================
# PART 1 — BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def find_max_average_brute_force(nums: List[int], k: int) -> float:
    pass


# ============================================================
# PART 2 — OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def find_max_average(nums: List[int], k: int) -> float:
    pass


# ============================================================
# PART 3 — TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
