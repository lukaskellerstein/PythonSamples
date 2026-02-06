
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

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def generate_parenthesis_brute_force(n: int) -> List[str]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Backtracking with pruning)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def generate_parenthesis(n: int) -> List[str]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": (3,),
            "expected": ["((()))","(()())","(())()","()(())","()()()"]
        },
        {
            "args": (1,),
            "expected": ["()"]
        },
        {
            "args": (2,),
            "expected": ["(())","()()"]
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = sorted(test["expected"])

        result1 = sorted(generate_parenthesis_brute_force(*args))
        result2 = sorted(generate_parenthesis(*args))

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
