
# ============================================================
# PROBLEM: Word Search (LeetCode 79)
# ============================================================
# Difficulty: Medium
# Pattern: Backtracking
#
# Given an m x n grid of characters board and a string word, return
# true if the word exists in the grid. The word can be constructed from
# letters of sequentially adjacent cells (horizontally or vertically
# neighboring). The same letter cell may not be used more than once.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
#   Output: true
#   Explanation: Path: (0,0)A -> (0,1)B -> (0,2)C -> (1,2)C -> (2,2)E -> (2,1)D
#
# Example 2:
#   Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
#   Output: true
#   Explanation: Path: (1,3)S -> (2,3)E -> (2,2)E
#
# Example 3:
#   Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
#   Output: false
#   Explanation: Cannot reuse cell (0,1)B after visiting it.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - m == board.length
# - n == board[i].length
# - 1 <= m, n <= 6
# - 1 <= word.length <= 15
# - board and word consist of only lowercase and uppercase English letters
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Board:
#   +---+---+---+---+
#   | A | B | C | E |
#   +---+---+---+---+
#   | S | F | C | S |
#   +---+---+---+---+
#   | A | D | E | E |
#   +---+---+---+---+
#
# Finding "ABCCED":
#   [A] [B] [C]  E       A -> B -> C -> C -> E -> D
#    S   F  [C]  S       Path traces through adjacent cells
#    A  [D] [E]  E       Each cell used at most once
#
# Backtracking: mark cell visited, explore 4 neighbors,
# then unmark (restore) the cell when backtracking.
#

from typing import List


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Explicit visited set)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def exist_brute_force(board: List[List[str]], word: str) -> bool:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (In-place visited marking)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def exist(board: List[List[str]], word: str) -> bool:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

    test_cases = [
        {
            "args": ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"),
            "expected": True
        },
        {
            "args": ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"),
            "expected": True
        },
        {
            "args": ([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"),
            "expected": False
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = exist_brute_force(*args)
        result2 = exist(*args)

        assert result1 == expected, f"Brute force failed for word='{args[1]}': got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for word='{args[1]}': got {result2}, expected {expected}"

        print(f"word='{args[1]}', expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
