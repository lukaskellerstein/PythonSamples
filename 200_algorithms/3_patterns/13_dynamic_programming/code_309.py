
# -----------------------
# Best Time to Buy and Sell Stock with Cooldown (LeetCode 309)
# -----------------------

# Difficulty: Medium
# Sub-pattern: Decision-Making / State Machine DP

# Problem: You are given an array prices where prices[i] is the price of a
# given stock on the ith day. Find the maximum profit you can achieve.
# You may complete as many transactions as you like with the following
# restrictions: After you sell your stock, you cannot buy stock on the
# next day (i.e., cooldown one day).

# -----------------------

# For prices=[1,2,3,0,2], max profit = 3 (buy@1, sell@3, cooldown, buy@0, sell@2).
prices = [1, 2, 3, 0, 2]

# ----------------------------------------------------
# State Machine DP solution
#
# States: hold (have stock), sold (just sold), rest (cooldown/idle)
#
# time complexity = O(n) - single pass
# space complexity = O(1) - three variables
# ----------------------------------------------------


def max_profit(prices):
    if len(prices) < 2:
        return 0

    # State transitions:
    # hold = max(hold, rest - price)  → keep holding OR buy after rest
    # sold = hold + price             → sell what we hold
    # rest = max(rest, sold)          → stay resting OR transition from sold
    hold = float("-inf")
    sold = 0
    rest = 0

    for price in prices:
        prev_hold = hold
        hold = max(hold, rest - price)
        rest = max(rest, sold)
        sold = prev_hold + price

    return max(sold, rest)


# Example
print(max_profit(prices))  # 3


# ----------------------------------------------------
# Bottom-Up DP solution (2D table)
#
# time complexity = O(n) - single pass
# space complexity = O(n) - dp arrays
# ----------------------------------------------------


def max_profit_dp(prices):
    n = len(prices)
    if n < 2:
        return 0

    # hold[i] = max profit on day i if holding stock
    # sold[i] = max profit on day i if just sold
    # rest[i] = max profit on day i if in cooldown/idle
    hold = [0] * n
    sold = [0] * n
    rest = [0] * n

    hold[0] = -prices[0]

    for i in range(1, n):
        hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
        sold[i] = hold[i - 1] + prices[i]
        rest[i] = max(rest[i - 1], sold[i - 1])

    return max(sold[n - 1], rest[n - 1])


# Example
print(max_profit_dp(prices))  # 3


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(3^n) - three choices at each day
# space complexity = O(n) - recursion stack depth
# ----------------------------------------------------


def max_profit_brute(prices):
    def dp(i, holding):
        if i >= len(prices):
            return 0
        if holding:
            # sell or hold
            return max(
                prices[i] + dp(i + 2, False),  # sell + cooldown
                dp(i + 1, True),  # hold
            )
        else:
            # buy or skip
            return max(
                -prices[i] + dp(i + 1, True),  # buy
                dp(i + 1, False),  # skip
            )

    return dp(0, False)


# Example
print(max_profit_brute(prices))  # 3
