from typing import List

# ============================================================
# PROBLEM: Merge Intervals (LeetCode 56)
# ============================================================
# Difficulty: Medium
# Pattern: Overlapping Intervals
#
# Given an array of intervals where intervals[i] = [start_i, end_i], merge all
# overlapping intervals and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#   Explanation: [1,3] and [2,6] overlap, so they merge into [1,6].
#
# Example 2:
#   Input: intervals = [[1,4],[4,5]]
#   Output: [[1,5]]
#   Explanation: [1,4] and [4,5] are considered overlapping (they share endpoint 4).
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= intervals.length <= 10^4
# - intervals[i].length == 2
# - 0 <= start_i <= end_i <= 10^4
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Input: [[1,3],[2,6],[8,10],[15,18]]
#
#   1  2  3  4  5  6  7  8  9  10 ... 15 16 17 18
#   |==|==|                               Interval [1,3]
#      |==|==|==|==|                       Interval [2,6]
#                     |==|==|              Interval [8,10]
#                                 |==|==|==|  Interval [15,18]
#
# After merge:
#   |==|==|==|==|==|                       Merged  [1,6]
#                     |==|==|              Kept    [8,10]
#                                 |==|==|==|  Kept    [15,18]
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

def merge_brute_force(intervals: List[List[int]]) -> List[List[int]]:
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

def merge(intervals: List[List[int]]) -> List[List[int]]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([[1, 3], [2, 6], [8, 10], [15, 18]],),
            "expected": [[1, 6], [8, 10], [15, 18]]
        },
        {
            "args": ([[1, 4], [4, 5]],),
            "expected": [[1, 5]]
        },
        {
            "args": ([[1, 5]],),
            "expected": [[1, 5]]
        },
        {
            "args": ([[1, 4], [2, 3]],),
            "expected": [[1, 4]]
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = merge_brute_force(*args)
        result2 = merge(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
