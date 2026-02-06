
# ============================================================
# PROBLEM: Longest Increasing Subsequence (LeetCode 300)
# ============================================================
# Difficulty: Medium
# Pattern: Dynamic Programming (1D Linear)
#
# Given an integer array nums, return the length of the longest
# strictly increasing subsequence. A subsequence is derived from the
# array by deleting some or no elements without changing the order
# of the remaining elements.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [10,9,2,5,3,7,101,18]
#   Output: 4
#   Explanation: The longest increasing subsequence is [2,3,7,101].
#
# Example 2:
#   Input: nums = [0,1,0,3,2,3]
#   Output: 4
#   Explanation: The longest increasing subsequence is [0,1,2,3].
#
# Example 3:
#   Input: nums = [7,7,7,7,7,7,7]
#   Output: 1
#   Explanation: All elements are the same, so LIS length is 1.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= nums.length <= 2500
# - -10^4 <= nums[i] <= 10^4
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums = [10, 9, 2, 5, 3, 7, 101, 18]
#
# DP approach (O(n^2)):
# dp[i] = length of LIS ending at index i
#
# Index:   0    1    2    3    4    5     6     7
# nums:   10    9    2    5    3    7   101    18
# dp:      1    1    1    2    2    3     4     4
#
# dp[3]=2: subsequence [2,5]
# dp[5]=3: subsequence [2,3,7] or [2,5,7]
# dp[6]=4: subsequence [2,3,7,101]
#
# Answer: max(dp) = 4
#
# Optimal (O(n log n)) uses patience sorting with binary search.
#

from typing import List


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Recursion: include/exclude)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def length_of_lis_brute_force(nums: List[int]) -> int:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Binary Search + Patience Sorting)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def length_of_lis(nums: List[int]) -> int:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
