
# -----------------------
# Climbing Stairs (LeetCode 70)
# -----------------------

# Difficulty: Easy
# Sub-pattern: 1D DP (Linear)

# Problem: You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways
# can you climb to the top?

# -----------------------

# For n=5, there are 8 distinct ways to climb to the top.
n = 5

# ----------------------------------------------------
# Bottom-Up DP solution
#
# time complexity = O(n) - single pass through steps
# space complexity = O(1) - only two variables
# ----------------------------------------------------


def climb_stairs(n):
    if n <= 2:
        return n

    # dp[i] = number of ways to reach step i
    # Recurrence: dp[i] = dp[i-1] + dp[i-2]
    # (arrive from one step below OR two steps below)
    # Space-optimized: only keep last two values
    prev2 = 1  # dp[0] — 1 way to reach step 1
    prev1 = 2  # dp[1] — 2 ways to reach step 2

    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr

    return prev1


# Example
print(climb_stairs(n))  # 8


# ----------------------------------------------------
# Top-Down (Memoization) solution
#
# time complexity = O(n) - each subproblem solved once
# space complexity = O(n) - recursion stack + memo dict
# ----------------------------------------------------


def climb_stairs_memo(n):
    memo = {}

    def dp(i):
        if i <= 2:
            return i
        if i in memo:
            return memo[i]
        memo[i] = dp(i - 1) + dp(i - 2)
        return memo[i]

    return dp(n)


# Example
print(climb_stairs_memo(n))  # 8


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^n) - binary tree of recursive calls
# space complexity = O(n) - recursion stack depth
# ----------------------------------------------------


def climb_stairs_brute(n):
    if n <= 2:
        return n
    return climb_stairs_brute(n - 1) + climb_stairs_brute(n - 2)


# Example
print(climb_stairs_brute(n))  # 8
