from typing import List


# ============================================================
# PROBLEM: Subarray Sum Equals K (LeetCode 560)
# ============================================================
# Difficulty: Medium
# Pattern: Prefix Sum + HashMap
#
# Given an array of integers nums and an integer k, return the
# total number of contiguous subarrays whose sum equals k.
# A subarray is a contiguous non-empty sequence of elements
# within an array.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
#   Output: 4
#   Explanation: Subarrays that sum to 7:
#                [3, 4], [7], [7, 2, -3, 1], [1, 4, 2]
#
# Example 2:
#   Input: nums = [1, 1, 1], k = 2
#   Output: 2
#   Explanation: [1, 1] at index 0-1 and [1, 1] at index 1-2
#
# Example 3:
#   Input: nums = [1, 2, 3], k = 3
#   Output: 2
#   Explanation: [1, 2] and [3]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= nums.length <= 2 * 10^4
# - -1000 <= nums[i] <= 1000
# - -10^7 <= k <= 10^7
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
#
# Prefix sums:
#   index:       0  1  2   3   4   5   6   7   8
#   prefix:   [0, 3, 7, 14, 16, 13, 14, 18, 20]
#
# Key insight: if prefix_sum[j] - prefix_sum[i] = k,
# then the subarray from index i+1 to j sums to k.
# So for each prefix_sum, we check if (prefix_sum - k) was seen before.
#
# Subarrays that sum to 7:
#   [3, 4]           -> 3 + 4 = 7
#   [7]              -> 7 = 7
#   [7, 2, -3, 1]    -> 7 + 2 - 3 + 1 = 7
#   [1, 4, 2]        -> 1 + 4 + 2 = 7
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def subarray_sum_brute_force(nums: List[int], k: int) -> int:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Prefix Sum + HashMap)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def subarray_sum(nums: List[int], k: int) -> int:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    test_cases = [
        ([3, 4, 7, 2, -3, 1, 4, 2], 7),  # Expected: 4
        ([1, 1, 1], 2),                   # Expected: 2
        ([1, 2, 3], 3),                   # Expected: 2
        ([1], 1),                         # Expected: 1
        ([1, -1, 0], 0),                  # Expected: 3
    ]

    pass
