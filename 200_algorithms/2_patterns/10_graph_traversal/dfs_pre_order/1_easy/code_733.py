
# -----------------------
# Flood Fill (LeetCode 733)
# -----------------------

# Difficulty: Easy

# Problem: An image is represented by an m x n integer grid where image[i][j]
# represents the pixel value. You are given three integers sr, sc, and color.
# Perform a flood fill on the image starting from the pixel image[sr][sc].
# To perform a flood fill, consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color). Replace the color of all of the aforementioned
# pixels with color.

# -----------------------
# VISUALIZATION
# -----------------------
#
# image = [[1,1,1],       After flood fill (sr=1, sc=1, color=2):
#          [1,1,0],  -->  [[2,2,2],
#          [1,0,1]]        [2,2,0],
#                          [2,0,1]]
#
# DFS from (1,1):
#   Visit (1,1) val=1, color->2
#     Visit (0,1) val=1, color->2
#       Visit (0,0) val=1, color->2
#         neighbors all out of bounds or different color -> backtrack
#       Visit (0,2) val=1, color->2
#         neighbors all visited or different color -> backtrack
#     Visit (1,0) val=1, color->2
#       Visit (2,0) val=1, color->2
#         neighbors all visited or different color -> backtrack
#     Visit (1,2) val=0 -> skip (different color)
#     Visit (2,1) val=0 -> skip (different color)
#
# -----------------------

from typing import List


# ----------------------------------------------------
# DFS Recursive solution (Optimal)
#
# time complexity = O(m * n) - visit every pixel at most once
# space complexity = O(m * n) - recursion stack in worst case
# ----------------------------------------------------

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    original_color = image[sr][sc]

    if original_color == color:
        return image

    rows, cols = len(image), len(image[0])

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original_color:
            return

        image[r][c] = color

        dfs(r + 1, c)  # down
        dfs(r - 1, c)  # up
        dfs(r, c + 1)  # right
        dfs(r, c - 1)  # left

    dfs(sr, sc)
    return image


# Example
image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(flood_fill(image1, 1, 1, 2))  # [[2,2,2],[2,2,0],[2,0,1]]


# ----------------------------------------------------
# DFS Iterative (Stack-based) solution
#
# time complexity = O(m * n) - visit every pixel at most once
# space complexity = O(m * n) - explicit stack
# ----------------------------------------------------

def flood_fill_iterative(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    original_color = image[sr][sc]

    if original_color == color:
        return image

    rows, cols = len(image), len(image[0])
    stack = [(sr, sc)]
    image[sr][sc] = color

    while stack:
        r, c = stack.pop()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                image[nr][nc] = color
                stack.append((nr, nc))

    return image


# Example
image2 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(flood_fill_iterative(image2, 1, 1, 2))  # [[2,2,2],[2,2,0],[2,0,1]]


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),  # same color
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 2, [[2, 2, 2], [2, 2, 2]]),  # fill all
    ]

    print("\nFlood Fill (DFS) Results:")
    print("-" * 50)

    for image, sr, sc, color, expected in test_cases:
        import copy
        img1 = copy.deepcopy(image)
        img2 = copy.deepcopy(image)
        result1 = flood_fill(img1, sr, sc, color)
        result2 = flood_fill_iterative(img2, sr, sc, color)
        print(f"Input:     {image}")
        print(f"Recursive: {result1}")
        print(f"Iterative: {result2}")
        print(f"Expected:  {expected}")
        print(f"Match:     {result1 == expected and result2 == expected}")
        print("-" * 50)
