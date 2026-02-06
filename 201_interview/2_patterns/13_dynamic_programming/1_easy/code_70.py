
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

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def climb_stairs_brute_force(n: int) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Bottom-Up DP, space-optimized)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def climb_stairs(n: int) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {"args": (2,), "expected": 2},
        {"args": (3,), "expected": 3},
        {"args": (5,), "expected": 8},
        {"args": (1,), "expected": 1},
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = climb_stairs_brute_force(*args)
        result2 = climb_stairs(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
