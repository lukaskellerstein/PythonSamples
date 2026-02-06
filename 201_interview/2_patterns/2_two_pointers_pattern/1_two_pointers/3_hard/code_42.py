from typing import List


# ============================================================
# PROBLEM: Trapping Rain Water (LeetCode 42)
# ============================================================
# Difficulty: Hard
# Pattern: Two Pointers
#
# Given n non-negative integers representing an elevation map
# where each bar has width 1, compute how much water it can
# trap after raining. This is a classic Google interview problem.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#   Output: 6
#   Explanation: 6 units of rain water are trapped between bars.
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
# Input:  [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
#
# Legend: # = ground (elevation), ~ = trapped water
#
#     3 |               #
#     2 |       # ~ ~ ~ # # ~ #
#     1 |   # ~ # # ~ # # # # # #
#       +-------------------------
#         0 1 2 3 4 5 6 7 8 9 10 11  <- index
#         0 1 0 2 1 0 1 3 2 1 2  1   <- height
#         0 0 1 0 1 2 1 0 0 1 0  0   <- water at each position
#                                    -----
#                          Total:    6
#
# Water at each index = min(max_left, max_right) - height[i]
#   - index 2: min(1, 3) - 0 = 1
#   - index 4: min(2, 3) - 1 = 1
#   - index 5: min(2, 3) - 0 = 2
#   - index 6: min(2, 3) - 1 = 1
#   - index 9: min(3, 2) - 1 = 1
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def trap_brute_force(height: List[int]) -> int:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Two Pointers)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def trap(height: List[int]) -> int:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    test_cases = [
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 0, 1], 1),
        ([3, 0, 0, 2, 0, 4], 10),
        ([], 0),
    ]

    pass
