
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
# BFS from (1,1): queue = [(1,1)]
#   Process (1,1) val=1, color->2, add neighbors with val=1
#   -> queue = [(0,1), (1,0)]
#   Process (0,1) val=1, color->2, add neighbors
#   -> queue = [(1,0), (0,0), (0,2)]
#   ... continue until queue empty
#
# -----------------------

from typing import List
from collections import deque


# ----------------------------------------------------
# BFS solution (Optimal)
#
# time complexity = O(m * n) - visit every pixel at most once
# space complexity = O(m * n) - queue can hold all pixels
# ----------------------------------------------------

def flood_fill(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    original_color = image[sr][sc]

    if original_color == color:
        return image

    rows, cols = len(image), len(image[0])
    queue = deque([(sr, sc)])
    image[sr][sc] = color

    while queue:
        r, c = queue.popleft()

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and image[nr][nc] == original_color:
                image[nr][nc] = color
                queue.append((nr, nc))

    return image


# Example
image1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(flood_fill(image1, 1, 1, 2))  # [[2,2,2],[2,2,0],[2,0,1]]


# ----------------------------------------------------
# Brute Force solution (Repeated scans)
#
# time complexity = O((m * n)^2) - worst case many passes
# space complexity = O(m * n) - visited set
# ----------------------------------------------------

def flood_fill_brute_force(image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
    original_color = image[sr][sc]

    if original_color == color:
        return image

    rows, cols = len(image), len(image[0])
    visited = set()

    # Mark starting pixel
    image[sr][sc] = color
    visited.add((sr, sc))

    # Keep scanning until no more changes
    changed = True
    while changed:
        changed = False
        for r in range(rows):
            for c in range(cols):
                if image[r][c] == original_color:
                    # Check if any neighbor is already colored
                    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + dr, c + dc
                        if (nr, nc) in visited:
                            image[r][c] = color
                            visited.add((r, c))
                            changed = True
                            break

    return image


# Example
image2 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(flood_fill_brute_force(image2, 1, 1, 2))  # [[2,2,2],[2,2,0],[2,0,1]]


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]]),  # same color
        ([[0, 0, 0], [0, 0, 0]], 0, 0, 2, [[2, 2, 2], [2, 2, 2]]),  # fill all
    ]

    print("\nFlood Fill (BFS) Results:")
    print("-" * 50)

    for image, sr, sc, color, expected in test_cases:
        import copy
        img1 = copy.deepcopy(image)
        img2 = copy.deepcopy(image)
        result1 = flood_fill(img1, sr, sc, color)
        result2 = flood_fill_brute_force(img2, sr, sc, color)
        print(f"Input:    {image}")
        print(f"BFS:      {result1}")
        print(f"Brute:    {result2}")
        print(f"Expected: {expected}")
        print(f"Match:    {result1 == expected and result2 == expected}")
        print("-" * 50)
