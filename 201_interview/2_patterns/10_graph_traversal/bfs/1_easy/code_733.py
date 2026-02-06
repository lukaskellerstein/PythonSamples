
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
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def flood_fill_brute_force(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (BFS)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
