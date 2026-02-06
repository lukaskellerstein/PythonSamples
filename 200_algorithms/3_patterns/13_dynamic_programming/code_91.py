
# -----------------------
# Decode Ways (LeetCode 91)
# -----------------------

# Difficulty: Medium
# Sub-pattern: 1D DP (Linear)

# Problem: A message containing letters from A-Z can be encoded into numbers
# using the mapping: 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26".
# Given a string s containing only digits, return the number of ways to
# decode it. The answer is guaranteed to fit in a 32-bit integer.

# -----------------------

# For s="226", there are 3 ways: "BZ" (2,26), "VF" (22,6), "BBF" (2,2,6).
s = "226"

# ----------------------------------------------------
# Bottom-Up DP solution (space-optimized)
#
# time complexity = O(n) - single pass
# space complexity = O(1) - two variables
# ----------------------------------------------------


def num_decodings(s):
    if not s or s[0] == "0":
        return 0

    # dp[i] = number of ways to decode s[0:i]
    # Recurrence:
    #   if s[i] != '0': dp[i] += dp[i-1] (single digit)
    #   if 10 <= int(s[i-1:i+1]) <= 26: dp[i] += dp[i-2] (two digits)
    prev2 = 1  # dp[i-2], empty string = 1 way
    prev1 = 1  # dp[i-1], first char (already checked != '0')

    for i in range(1, len(s)):
        curr = 0

        # Single digit decode
        if s[i] != "0":
            curr += prev1

        # Two digit decode
        two_digit = int(s[i - 1 : i + 1])
        if 10 <= two_digit <= 26:
            curr += prev2

        prev2 = prev1
        prev1 = curr

    return prev1


# Example
print(num_decodings(s))  # 3


# ----------------------------------------------------
# Top-Down (Memoization) solution
#
# time complexity = O(n) - each position solved once
# space complexity = O(n) - memo dict + recursion stack
# ----------------------------------------------------


def num_decodings_memo(s):
    memo = {}

    def dp(i):
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0
        if i in memo:
            return memo[i]

        # Take one digit
        result = dp(i + 1)

        # Take two digits
        if i + 1 < len(s) and int(s[i : i + 2]) <= 26:
            result += dp(i + 2)

        memo[i] = result
        return result

    return dp(0)


# Example
print(num_decodings_memo(s))  # 3


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^n) - binary branching at each position
# space complexity = O(n) - recursion stack
# ----------------------------------------------------


def num_decodings_brute(s):
    def dp(i):
        if i == len(s):
            return 1
        if s[i] == "0":
            return 0

        result = dp(i + 1)
        if i + 1 < len(s) and int(s[i : i + 2]) <= 26:
            result += dp(i + 2)

        return result

    return dp(0)


# Example
print(num_decodings_brute(s))  # 3
