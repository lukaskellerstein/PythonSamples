
# ============================================================
# PROBLEM: Valid Palindrome (LeetCode 125)
# ============================================================
# Difficulty: Easy
# Pattern: Two Pointers
#
# Given a string s, determine if it is a palindrome. A palindrome
# is a string that reads the same forward and backward. Consider
# only alphanumeric characters and ignore cases for this problem.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: s = "racecar"
#   Output: True
#   Explanation: "racecar" reversed is "racecar" -- same string.
#
# Example 2:
#   Input: s = "hello"
#   Output: False
#   Explanation: "hello" reversed is "olleh" -- not the same.
#
# Example 3:
#   Input: s = "madam"
#   Output: True
#
# Example 4:
#   Input: s = "a"
#   Output: True
#   Explanation: Single character is always a palindrome.
#
# Example 5:
#   Input: s = ""
#   Output: True
#   Explanation: Empty string is considered a palindrome.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 0 <= s.length <= 2 * 10^5
# - s consists only of printable ASCII characters
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# s = "racecar"
#
#  r  a  c  e  c  a  r
#  ^                 ^     left=0, right=6: 'r'=='r' -> match
#     ^           ^        left=1, right=5: 'a'=='a' -> match
#        ^     ^           left=2, right=4: 'c'=='c' -> match
#           ^              left=3, right=3: pointers crossed -> palindrome!
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Reverse and Compare)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def is_palindrome_brute_force(s: str) -> bool:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Two Pointers)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def is_palindrome(s: str) -> bool:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ("racecar",),
            "expected": True
        },
        {
            "args": ("hello",),
            "expected": False
        },
        {
            "args": ("madam",),
            "expected": True
        },
        {
            "args": ("python",),
            "expected": False
        },
        {
            "args": ("a",),
            "expected": True
        },
        {
            "args": ("aa",),
            "expected": True
        },
        {
            "args": ("ab",),
            "expected": False
        },
        {
            "args": ("",),
            "expected": True
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = is_palindrome_brute_force(*args)
        result2 = is_palindrome(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
