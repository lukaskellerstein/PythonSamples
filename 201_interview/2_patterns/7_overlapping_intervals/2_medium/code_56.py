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
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def merge_brute_force(intervals: List[List[int]]) -> List[List[int]]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def merge(intervals: List[List[int]]) -> List[List[int]]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1: Multiple overlapping intervals
    assert merge_brute_force([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]

    # Test case 2: Touching intervals
    assert merge_brute_force([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]

    # Test case 3: Single interval
    assert merge_brute_force([[1, 5]]) == [[1, 5]]
    assert merge([[1, 5]]) == [[1, 5]]

    # Test case 4: All overlapping
    assert merge([[1, 4], [2, 3]]) == [[1, 4]]

    print("All test cases passed!")
