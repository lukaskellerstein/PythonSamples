from typing import List


# ============================================================
# PROBLEM: Daily Temperatures (LeetCode 739)
# ============================================================
# Difficulty: Medium
# Pattern: Monotonic Stack (Decreasing Stack / Next Greater Element)
#
# Given an array of integers temperatures representing daily temperatures,
# return an array answer such that answer[i] is the number of days you
# have to wait after the ith day to get a warmer temperature. If there is
# no future day with a warmer temperature, keep answer[i] == 0.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
#   Output: [1, 1, 4, 2, 1, 1, 0, 0]
#   Explanation:
#     Day 0 (73): next warmer is day 1 (74) -> wait 1 day
#     Day 2 (75): next warmer is day 6 (76) -> wait 4 days
#     Day 6 (76): no warmer day ahead -> 0
#     Day 7 (73): no warmer day ahead -> 0
#
# Example 2:
#   Input: temperatures = [30, 40, 50, 60]
#   Output: [1, 1, 1, 0]
#
# Example 3:
#   Input: temperatures = [30, 60, 90]
#   Output: [1, 1, 0]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= temperatures.length <= 10^5
# - 30 <= temperatures[i] <= 100
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
#                  0   1   2   3   4   5   6   7   (indices)
#
# Monotonic decreasing stack (stores indices):
#   i=0 (73): stack=[0]
#   i=1 (74): 74>73, pop 0 -> ans[0]=1-0=1, stack=[1]
#   i=2 (75): 75>74, pop 1 -> ans[1]=2-1=1, stack=[2]
#   i=3 (71): 71<75, push -> stack=[2,3]
#   i=4 (69): 69<71, push -> stack=[2,3,4]
#   i=5 (72): 72>69, pop 4 -> ans[4]=5-4=1
#             72>71, pop 3 -> ans[3]=5-3=2, stack=[2,5]
#   i=6 (76): 76>72, pop 5 -> ans[5]=6-5=1
#             76>75, pop 2 -> ans[2]=6-2=4, stack=[6]
#   i=7 (73): 73<76, push -> stack=[6,7]
#   End: remaining indices get 0 -> ans[6]=0, ans[7]=0
#
# Result: [1, 1, 4, 2, 1, 1, 0, 0]
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


def daily_temperatures_brute_force(temperatures: List[int]) -> List[int]:
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


def daily_temperatures(temperatures: List[int]) -> List[int]:
    pass


# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([73, 74, 75, 71, 69, 72, 76, 73],),
            "expected": [1, 1, 4, 2, 1, 1, 0, 0],
        },
        {
            "args": ([30, 40, 50, 60],),
            "expected": [1, 1, 1, 0],
        },
        {
            "args": ([30, 60, 90],),
            "expected": [1, 1, 0],
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = daily_temperatures_brute_force(*args)
        result2 = daily_temperatures(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
