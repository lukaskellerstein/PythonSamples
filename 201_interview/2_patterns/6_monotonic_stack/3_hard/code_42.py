from typing import List


# ============================================================
# PROBLEM: Trapping Rain Water (LeetCode 42)
# ============================================================
# Difficulty: Hard
# Pattern: Monotonic Stack / Two Pointers
#
# Given n non-negative integers representing an elevation map where the
# width of each bar is 1, compute how much water it can trap after raining.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#   Output: 6
#   Explanation: 6 units of rain water are trapped (see visualization below).
#
# Example 2:
#   Input: height = [4, 2, 0, 3, 2, 5]
#   Output: 9
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - n == height.length
# - 1 <= n <= 2 * 10^4
# - 0 <= height[i] <= 10^5
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#
#                         |
#             |  W  W  W  |
#    |  W  |  |  |  W  |  |
# ___________________________________
#  0  1  0  2  1  0  1  3  2  1  2  1
#
# W = trapped water
#
# Water at each position = min(max_left, max_right) - height[i]
#   position 2: min(1, 3) - 0 = 1
#   position 4: min(2, 3) - 1 = 1
#   position 5: min(2, 3) - 0 = 2
#   position 6: min(2, 3) - 1 = 1
#   position 9: min(3, 2) - 1 = 1
#   Total = 6
#


# ============================================================
# PART 1 — BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def trap_brute_force(height: List[int]) -> int:
    pass


# ============================================================
# PART 2 — OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach (monotonic stack or two pointers)
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def trap(height: List[int]) -> int:
    pass


# ============================================================
# PART 3 — TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
