
# ============================================================
# PROBLEM: N-Queens (LeetCode 51)
# ============================================================
# Difficulty: Hard
# Pattern: Backtracking
#
# The n-queens puzzle is the problem of placing n queens on an n x n
# chessboard such that no two queens attack each other (no two queens
# share the same row, column, or diagonal). Given an integer n, return
# all distinct solutions. Each solution is a board configuration where
# 'Q' indicates a queen and '.' indicates an empty space.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: n = 4
#   Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
#   Explanation: There are exactly 2 distinct solutions for the 4-queens puzzle.
#
# Example 2:
#   Input: n = 1
#   Output: [["Q"]]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= n <= 9
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Solution 1 (n=4):        Solution 2 (n=4):
#   . Q . .                  . . Q .
#   . . . Q                  Q . . .
#   Q . . .                  . . . Q
#   . . Q .                  . Q . .
#
# Queen placement constraints:
#   - One queen per row (iterate row by row)
#   - One queen per column (track in cols set)
#   - One queen per "\" diagonal (track row - col in diag1 set)
#   - One queen per "/" diagonal (track row + col in diag2 set)
#
# Backtracking: For each row, try every column. If no conflict,
# place queen, recurse to next row, then remove queen.
#

from typing import List


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Check all placements explicitly)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def solve_n_queens_brute_force(n: int) -> List[List[str]]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Backtracking with constraint sets)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def solve_n_queens(n: int) -> List[List[str]]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": (4,),
            "expected": [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
        },
        {
            "args": (1,),
            "expected": [["Q"]]
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = sorted(test["expected"])

        result1 = sorted(solve_n_queens_brute_force(*args))
        result2 = sorted(solve_n_queens(*args))

        assert result1 == expected, f"Brute force failed for n={args[0]}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for n={args[0]}: got {result2}, expected {expected}"

        print(f"n={args[0]}, num_solutions={len(expected)} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
