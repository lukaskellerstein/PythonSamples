
# ============================================================
# PROBLEM: Number of Islands (LeetCode 200)
# ============================================================
# Difficulty: Medium
# Pattern: Graph Traversal - BFS
#
# Given an m x n 2D binary grid which represents a map of '1's (land)
# and '0's (water), return the number of islands. An island is surrounded
# by water and is formed by connecting adjacent lands horizontally or
# vertically. You may assume all four edges of the grid are surrounded
# by water.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: grid = [
#     ["1","1","1","1","0"],
#     ["1","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]
#   Output: 1
#   Explanation: All the '1's are connected, forming one island.
#
# Example 2:
#   Input: grid = [
#     ["1","1","0","0","0"],
#     ["1","1","0","0","0"],
#     ["0","0","1","0","0"],
#     ["0","0","0","1","1"]
#   ]
#   Output: 3
#   Explanation: Three separate groups of connected '1's.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - m == grid.length
# - n == grid[i].length
# - 1 <= m, n <= 300
# - grid[i][j] is '0' or '1'
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Grid (Example 2):
#   1 1 0 0 0       Island 1: cells (0,0),(0,1),(1,0),(1,1)
#   1 1 0 0 0       Island 2: cell  (2,2)
#   0 0 1 0 0       Island 3: cells (3,3),(3,4)
#   0 0 0 1 1
#
# BFS approach:
#   Scan grid left-to-right, top-to-bottom.
#   When a '1' is found, increment island count and BFS to mark
#   all connected '1's as visited (change to '0').
#

from typing import List
from collections import deque


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def num_islands_brute_force(grid: List[List[str]]) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (BFS)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def num_islands(grid: List[List[str]]) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    import copy

    test_cases = [
        {
            "args": ([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],),
            "expected": 1
        },
        {
            "args": ([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]],),
            "expected": 3
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = num_islands_brute_force(copy.deepcopy(args[0]))
        result2 = num_islands(copy.deepcopy(args[0]))

        assert result1 == expected, f"Brute force failed: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed: got {result2}, expected {expected}"

        print(f"expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
