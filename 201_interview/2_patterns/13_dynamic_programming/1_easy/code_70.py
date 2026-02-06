
# ============================================================
# PROBLEM: Climbing Stairs (LeetCode 70)
# ============================================================
# Difficulty: Easy
# Pattern: Dynamic Programming (1D Linear)
#
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct
# ways can you climb to the top?
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: n = 2
#   Output: 2
#   Explanation: (1+1) or (2). Two distinct ways.
#
# Example 2:
#   Input: n = 3
#   Output: 3
#   Explanation: (1+1+1), (1+2), (2+1). Three distinct ways.
#
# Example 3:
#   Input: n = 5
#   Output: 8
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= n <= 45
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Recurrence: dp[i] = dp[i-1] + dp[i-2]
# (reach step i from one step below OR two steps below)
#
# Step:    1   2   3   4   5
# Ways:    1   2   3   5   8
#
# DP table for n=5:
#   dp[1] = 1
#   dp[2] = 2
#   dp[3] = dp[2] + dp[1] = 2 + 1 = 3
#   dp[4] = dp[3] + dp[2] = 3 + 2 = 5
#   dp[5] = dp[4] + dp[3] = 5 + 3 = 8
#
# This is essentially the Fibonacci sequence.
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Pure recursion)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def climb_stairs_brute_force(n: int) -> int:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Bottom-Up DP, space-optimized)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def climb_stairs(n: int) -> int:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
