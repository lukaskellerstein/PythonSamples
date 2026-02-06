from typing import List


# ============================================================
# PROBLEM: Largest Rectangle in Histogram (LeetCode 84)
# ============================================================
# Difficulty: Hard
# Pattern: Monotonic Stack (Increasing Stack)
#
# Given an array of integers heights representing the histogram's bar
# height where the width of each bar is 1, return the area of the largest
# rectangle in the histogram.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: heights = [2, 1, 5, 6, 2, 3]
#   Output: 10
#   Explanation: The largest rectangle is formed by bars at indices 2 and 3
#                (heights 5 and 6) with width 2 -> area = 5 * 2 = 10.
#
# Example 2:
#   Input: heights = [2, 4]
#   Output: 4
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= heights.length <= 10^5
# - 0 <= heights[i] <= 10^4
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# heights = [2, 1, 5, 6, 2, 3]
#
#              |
#           |  |
#           |  |
#           |  |  .  |
#  |        |  |  |  |
#  |  |     |  |  |  |
# ________________________
#  2  1  5  6  2  3
#
# Largest rectangle: height=5, width=2 (bars at index 2,3) -> area=10
#
#              |
#           |XX|
#           |XX|
#           |  |  .  |
#  |        |  |  |  |
#  |  |     |  |  |  |
# ________________________
#  2  1  5  6  2  3
#
# For each bar, the rectangle extends left and right until hitting
# a bar shorter than it. Monotonic stack efficiently finds these boundaries.
#


# ============================================================
# PART 1 — BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def largest_rectangle_area_brute_force(heights: List[int]) -> int:
    pass


# ============================================================
# PART 2 — OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach using a monotonic increasing stack
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def largest_rectangle_area(heights: List[int]) -> int:
    pass


# ============================================================
# PART 3 — TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
