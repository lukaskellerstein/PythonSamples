
# ============================================================
# PROBLEM: Longest Substring Without Repeating Characters (LeetCode 3)
# ============================================================
# Difficulty: Medium
# Pattern: Sliding Window (Variable Size)
#
# Given a string s, find the length of the longest substring without
# repeating characters. A substring is a contiguous non-empty sequence
# of characters within a string.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: s = "abcabcbb"
#   Output: 3
#   Explanation: The longest substring is "abc", with length 3.
#
# Example 2:
#   Input: s = "bbbbb"
#   Output: 1
#   Explanation: The longest substring is "b", with length 1.
#
# Example 3:
#   Input: s = "pwwkew"
#   Output: 3
#   Explanation: The longest substring is "wke", with length 3.
#               Note that "pwke" is a subsequence, not a substring.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 0 <= s.length <= 5 * 10^4
# - s consists of English letters, digits, symbols, and spaces
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# s = "abcabcbb"
#
# left=0, right=0: [a]bcabcbb       -> seen={a}     -> len=1
# left=0, right=1: [ab]cabcbb       -> seen={a,b}   -> len=2
# left=0, right=2: [abc]abcbb       -> seen={a,b,c} -> len=3
# left=0, right=3: [abca]bcbb       -> 'a' repeated!
# left=1, right=3:  a[bca]bcbb      -> seen={b,c,a} -> len=3
# left=1, right=4:  a[bcab]cbb      -> 'b' repeated!
# left=2, right=4:  ab[cab]cbb      -> seen={c,a,b} -> len=3
# ...
# Maximum length = 3
#


# ============================================================
# PART 1 — BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def length_of_longest_substring_brute_force(s: str) -> int:
    pass


# ============================================================
# PART 2 — OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def length_of_longest_substring(s: str) -> int:
    pass


# ============================================================
# PART 3 — TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
