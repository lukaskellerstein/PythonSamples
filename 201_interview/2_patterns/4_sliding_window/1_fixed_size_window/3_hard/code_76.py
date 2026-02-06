from collections import Counter


# ============================================================
# PROBLEM: Minimum Window Substring (LeetCode 76)
# ============================================================
# Difficulty: Hard
# Pattern: Sliding Window (Variable Size / Shrinkable Window)
#
# Given two strings s and t of lengths m and n respectively, return
# the minimum window substring of s such that every character in t
# (including duplicates) is included in the window. If there is no
# such substring, return the empty string "".
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: s = "ADOBECODEBANC", t = "ABC"
#   Output: "BANC"
#   Explanation: "BANC" is the smallest substring containing 'A', 'B', and 'C'.
#
# Example 2:
#   Input: s = "a", t = "a"
#   Output: "a"
#   Explanation: The entire string s is the minimum window.
#
# Example 3:
#   Input: s = "a", t = "aa"
#   Output: ""
#   Explanation: Both 'a's from t must be included, which is impossible.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - m == s.length, n == t.length
# - 1 <= m, n <= 10^5
# - s and t consist of uppercase and lowercase English letters
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# s = "ADOBECODEBANC", t = "ABC"
#
# Expand right until all chars of t are covered:
#   [ADOBEC]ODEBANC   -> contains A, B, C -> record "ADOBEC" (len 6)
# Shrink left while still valid:
#   A[DOBEC]ODEBANC   -> missing A -> expand right again
#   ...
#   ADOBECODE[BANC]   -> contains A, B, C -> record "BANC" (len 4)
#
# Answer: "BANC"
#


# ============================================================
# PART 1 — BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def min_window_brute_force(s: str, t: str) -> str:
    pass


# ============================================================
# PART 2 — OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def min_window(s: str, t: str) -> str:
    pass


# ============================================================
# PART 3 — TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
