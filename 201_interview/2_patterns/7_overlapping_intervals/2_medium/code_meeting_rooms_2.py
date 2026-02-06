from typing import List

# ============================================================
# PROBLEM: Meeting Rooms II (LeetCode 253)
# ============================================================
# Difficulty: Medium
# Pattern: Overlapping Intervals
#
# Given an array of meeting time intervals where intervals[i] = [start_i, end_i],
# return the minimum number of conference rooms required to schedule all meetings
# without conflicts.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: intervals = [[0,30],[5,10],[15,20]]
#   Output: 2
#   Explanation: Meeting [0,30] runs the entire time. [5,10] overlaps with it,
#                so we need 2 rooms. [15,20] also overlaps with [0,30] but
#                [5,10] has ended, so 2 rooms still suffice.
#
# Example 2:
#   Input: intervals = [[7,10],[2,4]]
#   Output: 1
#   Explanation: The two meetings don't overlap, so 1 room is enough.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= intervals.length <= 10^4
# - 0 <= start_i < end_i <= 10^6
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Example 1: intervals = [[0,30],[5,10],[15,20]]
#
# Timeline:
#   0    5   10   15   20   25   30
#   |=========================|====|   Room 1: Meeting [0,30]
#        |====|                       Room 2: Meeting [5,10]
#                   |====|            Room 2: Meeting [15,20] (reuses room after [5,10] ends)
#
# Rooms needed at each point:
#   Time 0-5:   1 room  (only [0,30])
#   Time 5-10:  2 rooms ([0,30] + [5,10])
#   Time 10-15: 1 room  (only [0,30])
#   Time 15-20: 2 rooms ([0,30] + [15,20])
#   Time 20-30: 1 room  (only [0,30])
#
#   Maximum concurrent meetings = 2 => Answer: 2
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

def min_meeting_rooms_brute_force(intervals: List[List[int]]) -> int:
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

def min_meeting_rooms(intervals: List[List[int]]) -> int:
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
            "expected": 2
        },
        {
            "args": ([[7, 10], [2, 4]],),
            "expected": 1
        },
        {
            "args": ([[1, 5], [2, 6], [3, 7]],),
            "expected": 3
        },
        {
            "args": ([],),
            "expected": 0
        },
        {
            "args": ([[1, 5], [5, 10], [10, 15]],),
            "expected": 1
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = min_meeting_rooms_brute_force(*args)
        result2 = min_meeting_rooms(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
