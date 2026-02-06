
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
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def is_palindrome_brute_force(s: str) -> bool:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Two Pointers)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def is_palindrome(s: str) -> bool:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    test_cases = [
        ("racecar", True),
        ("hello", False),
        ("madam", True),
        ("python", False),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("", True),
    ]

    pass
