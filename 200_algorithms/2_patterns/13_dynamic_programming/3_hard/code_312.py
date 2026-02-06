
# -----------------------
# Burst Balloons (LeetCode 312)
# -----------------------

# Difficulty: Hard
# Sub-pattern: Interval DP

# Problem: You are given n balloons, indexed from 0 to n-1. Each balloon is
# painted with a number on it represented by array nums. You are asked to
# burst all the balloons. If you burst balloon i you will get
# nums[i-1] * nums[i] * nums[i+1] coins. If i-1 or i+1 goes out of bounds,
# treat it as if there is a balloon with a 1 painted on it. Return the
# maximum coins you can collect by bursting the balloons wisely.

# -----------------------

# For nums=[3,1,5,8], max coins = 167.
# Burst order: 1→5→3→8 gives 3*1*5 + 3*5*8 + 1*3*8 + 1*8*1 = 15+120+24+8 = 167.
nums = [3, 1, 5, 8]

# ----------------------------------------------------
# Bottom-Up Interval DP solution
#
# Key insight: Instead of thinking which balloon to burst FIRST,
# think which balloon to burst LAST in each interval.
#
# time complexity = O(n^3) - three nested loops
# space complexity = O(n^2) - 2D dp table
# ----------------------------------------------------


def max_coins(nums):
    # Add boundary balloons with value 1
    balloons = [1] + nums + [1]
    n = len(balloons)

    # dp[i][j] = max coins from bursting all balloons between i and j (exclusive)
    dp = [[0] * n for _ in range(n)]

    # Iterate over interval length
    for length in range(2, n):
        for left in range(0, n - length):
            right = left + length
            for k in range(left + 1, right):
                # k is the LAST balloon to burst in (left, right)
                coins = (
                    balloons[left] * balloons[k] * balloons[right]
                    + dp[left][k]
                    + dp[k][right]
                )
                dp[left][right] = max(dp[left][right], coins)

    return dp[0][n - 1]


# Example
print(max_coins(nums))  # 167


# ----------------------------------------------------
# Top-Down (Memoization) solution
#
# time complexity = O(n^3) - n^2 subproblems, each O(n) work
# space complexity = O(n^2) - memo table + recursion stack
# ----------------------------------------------------


def max_coins_memo(nums):
    balloons = [1] + nums + [1]
    n = len(balloons)
    memo = {}

    def dp(left, right):
        if right - left < 2:
            return 0
        if (left, right) in memo:
            return memo[(left, right)]

        result = 0
        for k in range(left + 1, right):
            coins = (
                balloons[left] * balloons[k] * balloons[right]
                + dp(left, k)
                + dp(k, right)
            )
            result = max(result, coins)

        memo[(left, right)] = result
        return result

    return dp(0, n - 1)


# Example
print(max_coins_memo(nums))  # 167


# ----------------------------------------------------
# Brute Force (Permutation) solution
#
# time complexity = O(n! * n) - try all burst orders
# space complexity = O(n) - recursion stack
# ----------------------------------------------------


def max_coins_brute(nums):
    def dp(remaining):
        if not remaining:
            return 0

        result = 0
        for i in range(len(remaining)):
            # Coins from bursting remaining[i]
            left = remaining[i - 1] if i > 0 else 1
            right = remaining[i + 1] if i < len(remaining) - 1 else 1
            coins = left * remaining[i] * right

            # Burst it and recurse on the rest
            new_remaining = remaining[:i] + remaining[i + 1 :]
            result = max(result, coins + dp(new_remaining))

        return result

    return dp(nums)


# Example
print(max_coins_brute(nums))  # 167
