
# -----------------------
# Edit Distance / Levenshtein Distance (LeetCode 72)
# -----------------------

# Difficulty: Medium
# Sub-pattern: String DP (Two-String)

# Problem: Given two strings word1 and word2, return the minimum number of
# operations required to convert word1 to word2. You have three operations:
# Insert a character, Delete a character, Replace a character.

# -----------------------

# For word1="horse" and word2="ros", the minimum is 3 operations:
# horse → rorse (replace 'h' with 'r')
# rorse → rose (remove 'r')
# rose → ros (remove 'e')
word1 = "horse"
word2 = "ros"

# ----------------------------------------------------
# Bottom-Up DP solution (space-optimized)
#
# time complexity = O(m * n) - fill the table
# space complexity = O(n) - single row
# ----------------------------------------------------


def min_distance(word1, word2):
    m, n = len(word1), len(word2)

    # dp[j] = edit distance for word1[0:i] → word2[0:j]
    dp = list(range(n + 1))

    for i in range(1, m + 1):
        prev = dp[0]  # dp[i-1][j-1]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = 1 + min(prev, dp[j], dp[j - 1])
                # prev    = replace (dp[i-1][j-1])
                # dp[j]   = delete  (dp[i-1][j])
                # dp[j-1] = insert  (dp[i][j-1])
            prev = temp

    return dp[n]


# Example
print(min_distance(word1, word2))  # 3


# ----------------------------------------------------
# Full 2D DP solution
#
# time complexity = O(m * n) - fill the table
# space complexity = O(m * n) - 2D dp table
# ----------------------------------------------------


def min_distance_2d(word1, word2):
    m, n = len(word1), len(word2)
    # dp[i][j] = min ops to convert word1[0:i] to word2[0:j]
    # Recurrence:
    #   if chars match: dp[i][j] = dp[i-1][j-1]
    #   else: dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])
    #                          (replace,         delete,      insert)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Base cases: transforming empty string
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j - 1],  # replace
                    dp[i - 1][j],  # delete
                    dp[i][j - 1],  # insert
                )

    return dp[m][n]


# Example
print(min_distance_2d(word1, word2))  # 3


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(3^(m+n)) - three choices at each step
# space complexity = O(m + n) - recursion stack depth
# ----------------------------------------------------


def min_distance_brute(word1, word2):
    def dp(i, j):
        if i == 0:
            return j
        if j == 0:
            return i
        if word1[i - 1] == word2[j - 1]:
            return dp(i - 1, j - 1)
        return 1 + min(
            dp(i - 1, j - 1),  # replace
            dp(i - 1, j),  # delete
            dp(i, j - 1),  # insert
        )

    return dp(len(word1), len(word2))


# Example
print(min_distance_brute(word1, word2))  # 3
