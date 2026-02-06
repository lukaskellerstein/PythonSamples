
# -----------------------
# Word Search (LeetCode 79)
# -----------------------

# Difficulty: Medium (very common at Google)

# Problem: Given an m x n grid of characters board and a string word, return
# true if word exists in the grid. The word can be constructed from letters of
# sequentially adjacent cells (horizontally or vertically). The same cell may
# not be used more than once.

# -----------------------

# For the given board and word "ABCCED", check if the word exists.
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"

# ----------------------------------------------------
# Backtracking solution (in-place visited marking)
#
# time complexity = O(m * n * 3^L) - start from each cell, branch 3 ways
#                   (not 4 because we won't revisit the cell we came from),
#                   L = length of word
# space complexity = O(L) - recursion depth equals word length
# ----------------------------------------------------


def exist(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, idx):
        # All characters matched
        if idx == len(word):
            return True

        # Out of bounds or character mismatch
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if board[r][c] != word[idx]:
            return False

        # Choose — mark cell as visited by replacing with '#'
        tmp = board[r][c]
        board[r][c] = "#"

        # Explore all 4 directions
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if backtrack(r + dr, c + dc, idx + 1):
                board[r][c] = tmp  # restore before returning
                return True

        # Undo (backtrack) — restore original character
        board[r][c] = tmp
        return False

    # Try starting from every cell
    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0):
                return True
    return False


# Example
print(exist(board, word))  # True


# Reset board for brute force example
board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

# ----------------------------------------------------
# Brute Force solution (explicit visited set)
#
# time complexity = O(m * n * 3^L) - same branching, but uses extra set
# space complexity = O(m * n) - visited set can hold all cells in worst case
# ----------------------------------------------------


def exist_brute_force(board, word):
    rows, cols = len(board), len(board[0])

    def backtrack(r, c, idx, visited):
        if idx == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return False
        if (r, c) in visited or board[r][c] != word[idx]:
            return False

        visited.add((r, c))

        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if backtrack(r + dr, c + dc, idx + 1, visited):
                visited.remove((r, c))
                return True

        visited.remove((r, c))
        return False

    for r in range(rows):
        for c in range(cols):
            if backtrack(r, c, 0, set()):
                return True
    return False


# Example
print(exist_brute_force(board, word))  # True
