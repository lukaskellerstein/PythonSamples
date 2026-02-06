
# -----------------------
# N-Queens (LeetCode 51)
# -----------------------

# Difficulty: Hard (Google favorite)

# Problem: The n-queens puzzle is the problem of placing n queens on an n x n
# chessboard such that no two queens attack each other. Given an integer n,
# return all distinct solutions. Each solution contains a distinct board
# configuration where 'Q' and '.' indicate a queen and an empty space.

# -----------------------

# For n=4, place 4 queens on a 4x4 board so no two attack each other.
n = 4

# ----------------------------------------------------
# Backtracking solution (with constraint sets)
#
# time complexity = O(n!) - at most n choices for row 0, n-1 for row 1, etc.
# space complexity = O(n^2) - board + O(n) for the three constraint sets
# ----------------------------------------------------


def solve_n_queens(n):
    res = []
    board = [["." for _ in range(n)] for _ in range(n)]

    # Constraint sets for O(1) conflict checking
    cols = set()       # columns with a queen
    diag1 = set()      # "\" diagonals identified by (row - col)
    diag2 = set()      # "/" diagonals identified by (row + col)

    def backtrack(row):
        if row == n:
            # All queens placed — record the board
            res.append(["".join(r) for r in board])
            return

        for col in range(n):
            # Pruning: skip if column or either diagonal is attacked
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue

            # Choose — place queen
            board[row][col] = "Q"
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            # Explore next row
            backtrack(row + 1)

            # Undo (backtrack) — remove queen
            board[row][col] = "."
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

    backtrack(0)
    return res


# Example
for solution in solve_n_queens(n):
    for row in solution:
        print(row)
    print()
# .Q..    ..Q.
# ...Q    Q...
# Q...    ...Q
# ..Q.    .Q..


# ----------------------------------------------------
# Brute Force solution (check all placements)
#
# time complexity = O(n^n) - try every column for every row without set pruning
# space complexity = O(n^2) - board
# ----------------------------------------------------


def solve_n_queens_brute_force(n):
    res = []

    def is_safe(board, row, col):
        # Check column above
        for r in range(row):
            if board[r][col] == "Q":
                return False
        # Check upper-left diagonal
        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r -= 1
            c -= 1
        # Check upper-right diagonal
        r, c = row - 1, col + 1
        while r >= 0 and c < n:
            if board[r][c] == "Q":
                return False
            r -= 1
            c += 1
        return True

    def backtrack(board, row):
        if row == n:
            res.append(["".join(r) for r in board])
            return
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = "Q"
                backtrack(board, row + 1)
                board[row][col] = "."

    backtrack([["." for _ in range(n)] for _ in range(n)], 0)
    return res


# Example
print(f"Number of solutions: {len(solve_n_queens_brute_force(n))}")  # 2
