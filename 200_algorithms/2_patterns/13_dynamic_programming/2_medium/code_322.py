
# -----------------------
# Coin Change (LeetCode 322)
# -----------------------

# Difficulty: Medium
# Sub-pattern: Knapsack Variants (Unbounded Knapsack)

# Problem: You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up, return -1.
# You may assume that you have an infinite number of each kind of coin.

# -----------------------

# For coins=[1,5,11] and amount=15, the minimum is 3 coins (5+5+5).
# Note: greedy (11+1+1+1+1=5 coins) fails here — DP is necessary.
coins = [1, 5, 11]
amount = 15

# ----------------------------------------------------
# Bottom-Up DP solution
#
# time complexity = O(amount * len(coins)) - for each amount try each coin
# space complexity = O(amount) - dp array
# ----------------------------------------------------


def coin_change(coins, amount):
    # dp[i] = minimum coins needed to make amount i
    # Recurrence: dp[i] = min(dp[i - coin] + 1) for each coin
    dp = [float("inf")] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] != float("inf"):
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float("inf") else -1


# Example
print(coin_change(coins, amount))  # 3


# ----------------------------------------------------
# Top-Down (Memoization) solution
#
# time complexity = O(amount * len(coins)) - each subproblem solved once
# space complexity = O(amount) - memo dict + recursion stack
# ----------------------------------------------------


def coin_change_memo(coins, amount):
    memo = {}

    def dp(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float("inf")
        if remaining in memo:
            return memo[remaining]

        result = float("inf")
        for coin in coins:
            result = min(result, dp(remaining - coin) + 1)

        memo[remaining] = result
        return result

    ans = dp(amount)
    return ans if ans != float("inf") else -1


# Example
print(coin_change_memo(coins, amount))  # 3


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(amount^len(coins)) - exponential branching
# space complexity = O(amount) - recursion stack depth
# ----------------------------------------------------


def coin_change_brute(coins, amount):
    def dp(remaining):
        if remaining == 0:
            return 0
        if remaining < 0:
            return float("inf")

        result = float("inf")
        for coin in coins:
            result = min(result, dp(remaining - coin) + 1)
        return result

    ans = dp(amount)
    return ans if ans != float("inf") else -1


# Example
print(coin_change_brute(coins, amount))  # 3
