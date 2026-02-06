
# -----------------------
# Unique Paths (LeetCode 62)
# -----------------------

# Difficulty: Medium
# Sub-pattern: Grid / 2D DP

# Problem: There is a robot on an m x n grid. The robot is initially located
# at the top-left corner (grid[0][0]). The robot tries to move to the
# bottom-right corner (grid[m-1][n-1]). The robot can only move either
# down or right at any point in time. Given the two integers m and n,
# return the number of possible unique paths.

# -----------------------

# For a 3x7 grid, there are 28 unique paths.
m = 3
n = 7

# ----------------------------------------------------
# Bottom-Up DP solution (space-optimized)
#
# time complexity = O(m * n) - fill the grid
# space complexity = O(n) - single row
# ----------------------------------------------------


def unique_paths(m, n):
    # dp[j] = number of ways to reach column j in current row
    # Recurrence: dp[i][j] = dp[i-1][j] + dp[i][j-1]
    #   (come from above or from the left)
    # Space-optimized: dp[j] += dp[j-1] (above is already in dp[j])
    dp = [1] * n

    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]

    return dp[n - 1]


# Example
print(unique_paths(m, n))  # 28


# ----------------------------------------------------
# Full 2D DP solution
#
# time complexity = O(m * n) - fill the grid
# space complexity = O(m * n) - 2D dp table
# ----------------------------------------------------


def unique_paths_2d(m, n):
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


# Example
print(unique_paths_2d(m, n))  # 28


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^(m+n)) - binary tree of recursive calls
# space complexity = O(m + n) - recursion stack depth
# ----------------------------------------------------


def unique_paths_brute(m, n):
    def dp(i, j):
        if i == 0 or j == 0:
            return 1
        return dp(i - 1, j) + dp(i, j - 1)

    return dp(m - 1, n - 1)


# Example
print(unique_paths_brute(m, n))  # 28
