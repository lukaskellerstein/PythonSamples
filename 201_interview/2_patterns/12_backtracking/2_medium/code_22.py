
# ============================================================
# PROBLEM: Generate Parentheses (LeetCode 22)
# ============================================================
# Difficulty: Medium
# Pattern: Backtracking
#
# Given n pairs of parentheses, write a function to generate all
# combinations of well-formed parentheses. A well-formed string has
# matching opening and closing parentheses in the correct order.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: n = 3
#   Output: ["((()))","(()())","(())()","()(())","()()()"]
#   Explanation: All 5 valid combinations of 3 pairs of parentheses.
#
# Example 2:
#   Input: n = 1
#   Output: ["()"]
#
# Example 3:
#   Input: n = 2
#   Output: ["(())","()()"]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= n <= 8
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Decision tree for n=2:
#
#                    ""
#                   /
#                 "("
#                /    \
#            "(("      "()"
#            /           \
#         "(()"         "()(
#          /               \
#       "(())"           "()()"
#
# At each step we can:
#   - Add '(' if open_count < n
#   - Add ')' if close_count < open_count
#

from typing import List


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Generate all, then filter)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def generate_parenthesis_brute_force(n: int) -> List[str]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Backtracking with pruning)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def generate_parenthesis(n: int) -> List[str]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
