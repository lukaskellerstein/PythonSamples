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
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====


def largest_rectangle_area_brute_force(heights: List[int]) -> int:
    pass


# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====


def largest_rectangle_area(heights: List[int]) -> int:
    pass


# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([2, 1, 5, 6, 2, 3],),
            "expected": 10,
        },
        {
            "args": ([2, 4],),
            "expected": 4,
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = largest_rectangle_area_brute_force(*args)
        result2 = largest_rectangle_area(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
