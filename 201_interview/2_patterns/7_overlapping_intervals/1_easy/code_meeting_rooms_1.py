from typing import List

# ============================================================
# PROBLEM: Meeting Rooms I (LeetCode 252)
# ============================================================
# Difficulty: Easy
# Pattern: Overlapping Intervals
#
# Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
# determine if a person could attend all meetings. In other words, check whether
# any two meetings overlap. If no meetings overlap, return True; otherwise False.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: intervals = [[0,30],[5,10],[15,20]]
#   Output: False
#   Explanation: Meeting [5,10] overlaps with [0,30] (starts at 5 which is before 30).
#
# Example 2:
#   Input: intervals = [[7,10],[2,4]]
#   Output: True
#   Explanation: No meetings overlap. [2,4] ends before [7,10] starts.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 0 <= intervals.length <= 10^4
# - intervals[i].length == 2
# - 0 <= start_i < end_i <= 10^6
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Example 1: intervals = [[0,30],[5,10],[15,20]]
#
#   0    5   10   15   20   25   30
#   |====|====|====|====|====|====|   Meeting 1: [0, 30]
#        |====|                       Meeting 2: [5, 10]  -- OVERLAPS with Meeting 1
#                   |====|            Meeting 3: [15, 20] -- OVERLAPS with Meeting 1
#
# Example 2: intervals = [[7,10],[2,4]]
#
#   0  2  4  6  7  8  10
#      |==|                           Meeting 1: [2, 4]
#            |==|==|                  Meeting 2: [7, 10]  -- No overlap
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

def can_attend_meetings_brute_force(intervals: List[List[int]]) -> bool:
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

def can_attend_meetings(intervals: List[List[int]]) -> bool:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([[0, 30], [5, 10], [15, 20]],),
            "expected": False
        },
        {
            "args": ([[7, 10], [2, 4]],),
            "expected": True
        },
        {
            "args": ([],),
            "expected": True
        },
        {
            "args": ([[1, 5]],),
            "expected": True
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = can_attend_meetings_brute_force(*args)
        result2 = can_attend_meetings(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
