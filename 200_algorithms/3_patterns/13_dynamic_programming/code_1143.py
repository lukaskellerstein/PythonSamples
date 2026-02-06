
# -----------------------
# Longest Common Subsequence (LeetCode 1143)
# -----------------------

# Difficulty: Medium
# Sub-pattern: String DP (Two-String)

# Problem: Given two strings text1 and text2, return the length of their
# longest common subsequence. A subsequence is a sequence that can be derived
# from the string by deleting some (or no) characters without changing the
# relative order of the remaining characters.

# -----------------------

# For text1="abcde" and text2="ace", the LCS is "ace" → length 3.
text1 = "abcde"
text2 = "ace"

# ----------------------------------------------------
# Bottom-Up DP solution (space-optimized)
#
# time complexity = O(m * n) - fill the table
# space complexity = O(min(m, n)) - single row
# ----------------------------------------------------


def longest_common_subsequence(text1, text2):
    # Ensure text2 is the shorter string for space optimization
    if len(text1) < len(text2):
        text1, text2 = text2, text1

    m, n = len(text1), len(text2)
    # dp[j] = LCS length for text1[0:i] and text2[0:j]
    dp = [0] * (n + 1)

    for i in range(1, m + 1):
        prev = 0  # dp[i-1][j-1]
        for j in range(1, n + 1):
            temp = dp[j]
            if text1[i - 1] == text2[j - 1]:
                dp[j] = prev + 1
            else:
                dp[j] = max(dp[j], dp[j - 1])
            prev = temp

    return dp[n]


# Example
print(longest_common_subsequence(text1, text2))  # 3


# ----------------------------------------------------
# Full 2D DP solution
#
# time complexity = O(m * n) - fill the table
# space complexity = O(m * n) - 2D dp table
# ----------------------------------------------------


def longest_common_subsequence_2d(text1, text2):
    m, n = len(text1), len(text2)
    # dp[i][j] = LCS length for text1[0:i] and text2[0:j]
    # Recurrence:
    #   if text1[i-1] == text2[j-1]: dp[i][j] = dp[i-1][j-1] + 1
    #   else: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Example
print(longest_common_subsequence_2d(text1, text2))  # 3


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^(m+n)) - explore all combinations
# space complexity = O(m + n) - recursion stack depth
# ----------------------------------------------------


def longest_common_subsequence_brute(text1, text2):
    def dp(i, j):
        if i == 0 or j == 0:
            return 0
        if text1[i - 1] == text2[j - 1]:
            return 1 + dp(i - 1, j - 1)
        return max(dp(i - 1, j), dp(i, j - 1))

    return dp(len(text1), len(text2))


# Example
print(longest_common_subsequence_brute(text1, text2))  # 3
