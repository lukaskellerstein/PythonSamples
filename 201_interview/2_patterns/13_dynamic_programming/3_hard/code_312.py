
# ============================================================
# PROBLEM: Burst Balloons (LeetCode 312)
# ============================================================
# Difficulty: Hard
# Pattern: Dynamic Programming (Interval DP)
#
# You are given n balloons indexed from 0 to n-1. Each balloon is
# painted with a number represented by array nums. You burst all
# balloons. When you burst balloon i, you get nums[i-1] * nums[i] *
# nums[i+1] coins. If i-1 or i+1 goes out of bounds, treat it as
# having a balloon with value 1. Return the maximum coins you can
# collect by bursting the balloons wisely.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [3,1,5,8]
#   Output: 167
#   Explanation: Burst order 1->5->3->8 gives:
#     nums = [3,1,5,8] -> burst 1: 3*1*5 = 15
#     nums = [3,5,8]   -> burst 5: 3*5*8 = 120
#     nums = [3,8]     -> burst 3: 1*3*8 = 24
#     nums = [8]       -> burst 8: 1*8*1 = 8
#     Total: 15 + 120 + 24 + 8 = 167
#
# Example 2:
#   Input: nums = [1,5]
#   Output: 10
#   Explanation: Burst 1 first (1*1*5=5), then 5 (1*5*1=5). Total=10.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - n == nums.length
# - 1 <= n <= 300
# - 0 <= nums[i] <= 100
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Key insight: Think about which balloon to burst LAST in each interval,
# not which to burst first.
#
# nums = [3, 1, 5, 8]  ->  balloons = [1, 3, 1, 5, 8, 1]  (add boundary 1s)
#
# dp[i][j] = max coins from bursting all balloons between i and j (exclusive)
#
# For interval (0, 5) with balloons = [1, 3, 1, 5, 8, 1]:
#   Try k=1 (burst 3 last): 1*3*1 + dp[0][1] + dp[1][5]
#   Try k=2 (burst 1 last): 1*1*1 + dp[0][2] + dp[2][5]
#   Try k=3 (burst 5 last): 1*5*1 + dp[0][3] + dp[3][5]
#   Try k=4 (burst 8 last): 1*8*1 + dp[0][4] + dp[4][5]
#
# Answer: dp[0][5] = 167
#

from typing import List


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Try all burst orders)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def max_coins_brute_force(nums: List[int]) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Interval DP)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def max_coins(nums: List[int]) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {"args": ([3,1,5,8],), "expected": 167},
        {"args": ([1,5],), "expected": 10},
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = max_coins_brute_force(*args)
        result2 = max_coins(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
