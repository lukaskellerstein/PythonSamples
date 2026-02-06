
# ============================================================
# PROBLEM: Coin Change (LeetCode 322)
# ============================================================
# Difficulty: Medium
# Pattern: Dynamic Programming (Unbounded Knapsack)
#
# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of
# money. Return the fewest number of coins needed to make up that
# amount. If that amount cannot be made up by any combination of the
# coins, return -1. You may assume infinite supply of each coin type.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: coins = [1,5,11], amount = 15
#   Output: 3
#   Explanation: 15 = 5 + 5 + 5. Note: greedy (11+1+1+1+1 = 5 coins)
#                fails here, which is why DP is necessary.
#
# Example 2:
#   Input: coins = [2], amount = 3
#   Output: -1
#   Explanation: Cannot make amount 3 with only coin of value 2.
#
# Example 3:
#   Input: coins = [1], amount = 0
#   Output: 0
#   Explanation: Amount 0 requires 0 coins.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= coins.length <= 12
# - 1 <= coins[i] <= 2^31 - 1
# - 0 <= amount <= 10^4
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# coins = [1, 5, 11], amount = 15
#
# DP table: dp[i] = minimum coins to make amount i
#
# Amount:  0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
# dp:      0   1   2   3   4   1   2   3   4   5   2   1   2   3   4   3
#                               ^                       ^               ^
#                            5=5(1)                  11=11(1)      15=5+5+5(3)
#
# Recurrence: dp[i] = min(dp[i - coin] + 1) for each coin where coin <= i
#

from typing import List


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Recursion without memoization)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def coin_change_brute_force(coins: List[int], amount: int) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Bottom-Up DP)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def coin_change(coins: List[int], amount: int) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {"args": ([1,5,11], 15), "expected": 3},
        {"args": ([2], 3), "expected": -1},
        {"args": ([1], 0), "expected": 0},
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = coin_change_brute_force(*args)
        result2 = coin_change(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
