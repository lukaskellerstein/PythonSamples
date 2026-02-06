
# -----------------------
# Number of Islands (LeetCode 200)
# -----------------------

# Difficulty: Medium

# Problem: Given an m x n 2D binary grid which represents a map of '1's (land)
# and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands
# horizontally or vertically. You may assume all four edges of the grid are
# surrounded by water.

# -----------------------

# Example:
#   1 1 0 0 0
#   1 1 0 0 0
#   0 0 1 0 0
#   0 0 0 1 1
#
# Output: 3 (three separate islands)

from collections import deque


grid1 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

grid2 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]


# ----------------------------------------------------
# BFS solution (Optimal)
#
# time complexity = O(m * n) - visit each cell once
# space complexity = O(min(m, n)) - queue size in worst case
#
# Idea: Iterate through grid. When we find a '1', increment island count
# and use BFS to mark all connected land cells as visited.
# ----------------------------------------------------


def num_islands_bfs(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        grid[r][c] = "0"  # Mark as visited

        while queue:
            row, col = queue.popleft()

            # Check all 4 directions
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                    grid[nr][nc] = "0"  # Mark as visited
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                bfs(r, c)

    return islands


# Make copies since we modify the grid
print(num_islands_bfs([row[:] for row in grid1]))  # 3
print(num_islands_bfs([row[:] for row in grid2]))  # 1


# ----------------------------------------------------
# Union-Find solution (Optimal Alternative)
#
# time complexity = O(m * n * α(m * n)) ≈ O(m * n) with path compression
# space complexity = O(m * n) - parent array
#
# Idea: Use Union-Find to group connected land cells. Count unique roots.
# ----------------------------------------------------


def num_islands_union_find(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])

    # Initialize Union-Find
    parent = list(range(rows * cols))
    rank = [0] * (rows * cols)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return
        # Union by rank
        if rank[px] < rank[py]:
            px, py = py, px
        parent[py] = px
        if rank[px] == rank[py]:
            rank[px] += 1

    def get_id(r, c):
        return r * cols + c

    # Union adjacent land cells
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                # Check right and down neighbors only (to avoid double counting)
                if c + 1 < cols and grid[r][c + 1] == "1":
                    union(get_id(r, c), get_id(r, c + 1))
                if r + 1 < rows and grid[r + 1][c] == "1":
                    union(get_id(r, c), get_id(r + 1, c))

    # Count unique roots for land cells
    unique_roots = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                unique_roots.add(find(get_id(r, c)))

    return len(unique_roots)


print(num_islands_union_find([row[:] for row in grid1]))  # 3
print(num_islands_union_find([row[:] for row in grid2]))  # 1


# ----------------------------------------------------
# Brute Force solution (with visited set)
#
# time complexity = O(m * n) - same as optimal
# space complexity = O(m * n) - explicit visited set
#
# Idea: Same BFS but uses explicit visited set instead of modifying grid.
# Less efficient due to set operations but doesn't mutate input.
# ----------------------------------------------------


def num_islands_brute_force(grid):
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    islands = 0

    def bfs(r, c):
        queue = deque([(r, c)])
        visited.add((r, c))

        while queue:
            row, col = queue.popleft()

            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = row + dr, col + dc

                if (0 <= nr < rows and 0 <= nc < cols and
                        grid[nr][nc] == "1" and (nr, nc) not in visited):
                    visited.add((nr, nc))
                    queue.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visited:
                islands += 1
                bfs(r, c)

    return islands


print(num_islands_brute_force([row[:] for row in grid1]))  # 3
print(num_islands_brute_force([row[:] for row in grid2]))  # 1
