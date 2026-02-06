
# ============================================================
# PROBLEM: Flood Fill (LeetCode 733)
# ============================================================
# Difficulty: Easy
# Pattern: Graph Traversal - BFS
#
# An image is represented by an m x n integer grid where image[i][j]
# represents the pixel value. You are given three integers sr, sc, and
# color. Perform a flood fill starting from pixel image[sr][sc].
# Replace the color of the starting pixel and all 4-directionally
# connected pixels that share the same original color with the new color.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2
#   Output: [[2,2,2],[2,2,0],[2,0,1]]
#   Explanation: From pixel (1,1), all connected pixels with value 1
#                are changed to 2. Pixels (2,2) and (1,2),(2,1) are not
#                connected to (1,1) through same-color pixels.
#
# Example 2:
#   Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, color = 0
#   Output: [[0,0,0],[0,0,0]]
#   Explanation: Starting pixel already has the target color, no change.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - m == image.length
# - n == image[i].length
# - 1 <= m, n <= 50
# - 0 <= image[i][j], color < 2^16
# - 0 <= sr < m
# - 0 <= sc < n
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Before:              After (sr=1, sc=1, color=2):
#   [1, 1, 1]            [2, 2, 2]
#   [1, 1, 0]    --->    [2, 2, 0]
#   [1, 0, 1]            [2, 0, 1]
#
# BFS traversal from (1,1):
#   Queue: [(1,1)]
#   Process (1,1) -> color=2, enqueue neighbors (0,1),(1,0)
#   Queue: [(0,1),(1,0)]
#   Process (0,1) -> color=2, enqueue (0,0),(0,2)
#   Process (1,0) -> color=2, enqueue (2,0)
#   ... continue until queue is empty
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

def flood_fill_brute_force(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
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

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
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
            "args": ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2),
            "expected": [[2,2,2],[2,2,0],[2,0,1]]
        },
        {
            "args": ([[0,0,0],[0,0,0]], 0, 0, 0),
            "expected": [[0,0,0],[0,0,0]]
        },
    ]

    for test in test_cases:
        image, sr, sc, color = test["args"]
        expected = test["expected"]

        result1 = flood_fill_brute_force(copy.deepcopy(image), sr, sc, color)
        result2 = flood_fill(copy.deepcopy(image), sr, sc, color)

        assert result1 == expected, f"Brute force failed: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed: got {result2}, expected {expected}"

        print(f"args=({image}, {sr}, {sc}, {color}), expected={expected} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
