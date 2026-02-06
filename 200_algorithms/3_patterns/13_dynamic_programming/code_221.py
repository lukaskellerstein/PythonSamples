
# -----------------------
# Maximal Square (LeetCode 221)
# -----------------------

# Difficulty: Medium
# Sub-pattern: Grid / 2D DP

# Problem: Given an m x n binary matrix filled with 0's and 1's, find the
# largest square containing only 1's and return its area.

# -----------------------

# For the matrix below, the largest square of 1's has side 2 → area = 4.
matrix = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]

# ----------------------------------------------------
# Bottom-Up DP solution
#
# time complexity = O(m * n) - visit each cell once
# space complexity = O(n) - single row (space-optimized)
# ----------------------------------------------------


def maximal_square(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    # dp[j] = side length of largest square ending at (current_row, j)
    dp = [0] * (cols + 1)
    max_side = 0
    prev = 0  # dp[i-1][j-1]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            temp = dp[j]
            if matrix[i - 1][j - 1] == "1":
                # Recurrence: dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                dp[j] = min(dp[j], dp[j - 1], prev) + 1
                max_side = max(max_side, dp[j])
            else:
                dp[j] = 0
            prev = temp

    return max_side * max_side


# Example
print(maximal_square(matrix))  # 4


# ----------------------------------------------------
# Full 2D DP solution
#
# time complexity = O(m * n) - visit each cell once
# space complexity = O(m * n) - 2D dp table
# ----------------------------------------------------


def maximal_square_2d(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
    max_side = 0

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_side = max(max_side, dp[i][j])

    return max_side * max_side


# Example
print(maximal_square_2d(matrix))  # 4


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(m * n * min(m,n)^2) - for each cell, expand square
# space complexity = O(1)
# ----------------------------------------------------


def maximal_square_brute(matrix):
    if not matrix:
        return 0

    rows, cols = len(matrix), len(matrix[0])
    max_side = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == "1":
                # Try to expand square from (i, j)
                side = 1
                can_expand = True
                while can_expand and i + side < rows and j + side < cols:
                    # Check new row and new column added by expansion
                    for k in range(j, j + side + 1):
                        if matrix[i + side][k] != "1":
                            can_expand = False
                            break
                    if can_expand:
                        for k in range(i, i + side + 1):
                            if matrix[k][j + side] != "1":
                                can_expand = False
                                break
                    if can_expand:
                        side += 1
                max_side = max(max_side, side)

    return max_side * max_side


# Example
print(maximal_square_brute(matrix))  # 4
