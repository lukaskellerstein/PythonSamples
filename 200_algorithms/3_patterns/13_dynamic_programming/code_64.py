
# -----------------------
# Minimum Path Sum (LeetCode 64)
# -----------------------

# Difficulty: Medium
# Sub-pattern: Grid / 2D DP

# Problem: Given a m x n grid filled with non-negative numbers, find a path
# from top left to bottom right, which minimizes the sum of all numbers
# along its path. You can only move either down or right at any point.

# -----------------------

# For the grid below, minimum path sum = 7 (1→3→1→1→1).
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1],
]

# ----------------------------------------------------
# Bottom-Up DP solution (in-place)
#
# time complexity = O(m * n) - visit each cell once
# space complexity = O(1) - modify grid in-place
# ----------------------------------------------------


def min_path_sum(grid):
    rows, cols = len(grid), len(grid[0])

    # Fill first row (can only come from left)
    for j in range(1, cols):
        grid[0][j] += grid[0][j - 1]

    # Fill first column (can only come from above)
    for i in range(1, rows):
        grid[i][0] += grid[i - 1][0]

    # Fill rest: dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
    for i in range(1, rows):
        for j in range(1, cols):
            grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

    return grid[rows - 1][cols - 1]


# Example (note: modifies grid in-place, so copy for reuse)
import copy

grid_copy = copy.deepcopy(grid)
print(min_path_sum(grid_copy))  # 7


# ----------------------------------------------------
# Bottom-Up DP solution (separate dp array)
#
# time complexity = O(m * n) - visit each cell once
# space complexity = O(n) - single row
# ----------------------------------------------------


def min_path_sum_dp(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [float("inf")] * (cols + 1)
    dp[1] = 0  # seed for grid[0][0]

    for i in range(rows):
        for j in range(cols):
            dp[j + 1] = grid[i][j] + min(dp[j], dp[j + 1])

    return dp[cols]


# Example
print(min_path_sum_dp(grid))  # 7


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^(m+n)) - binary tree of recursive calls
# space complexity = O(m + n) - recursion stack depth
# ----------------------------------------------------


def min_path_sum_brute(grid):
    rows, cols = len(grid), len(grid[0])

    def dp(i, j):
        if i == 0 and j == 0:
            return grid[0][0]
        if i < 0 or j < 0:
            return float("inf")
        return grid[i][j] + min(dp(i - 1, j), dp(i, j - 1))

    return dp(rows - 1, cols - 1)


# Example
print(min_path_sum_brute(grid))  # 7
