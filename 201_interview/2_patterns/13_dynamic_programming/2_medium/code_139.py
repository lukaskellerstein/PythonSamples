
# ============================================================
# PROBLEM: Word Break (LeetCode 139)
# ============================================================
# Difficulty: Medium
# Pattern: Dynamic Programming (1D Linear)
#
# Given a string s and a dictionary of strings wordDict, return true
# if s can be segmented into a space-separated sequence of one or more
# dictionary words. The same word in the dictionary may be reused
# multiple times in the segmentation.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: s = "leetcode", wordDict = ["leet","code"]
#   Output: true
#   Explanation: "leetcode" can be segmented as "leet code".
#
# Example 2:
#   Input: s = "applepenapple", wordDict = ["apple","pen"]
#   Output: true
#   Explanation: "applepenapple" = "apple" + "pen" + "apple".
#
# Example 3:
#   Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
#   Output: false
#   Explanation: No valid segmentation exists.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= s.length <= 300
# - 1 <= wordDict.length <= 1000
# - 1 <= wordDict[i].length <= 20
# - s and wordDict[i] consist of only lowercase English letters
# - All the strings of wordDict are unique
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# s = "leetcode", wordDict = ["leet", "code"]
#
# DP table: dp[i] = can s[0:i] be segmented?
#
# Index:  0     1     2     3     4     5     6     7     8
# Char:   ""    l     e     e     t     c     o     d     e
# dp:     T     F     F     F     T     F     F     F     T
#                                 ^                       ^
#                              "leet"                  "code"
#                             dp[0]=T                 dp[4]=T
#
# dp[0] = True  (empty string)
# dp[4] = True  (s[0:4] = "leet" is in dict, and dp[0] = True)
# dp[8] = True  (s[4:8] = "code" is in dict, and dp[4] = True)
#

from typing import List


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Recursion without memoization)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def word_break_brute_force(s: str, wordDict: List[str]) -> bool:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Bottom-Up DP)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def word_break(s: str, wordDict: List[str]) -> bool:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {"args": ("leetcode", ["leet","code"]), "expected": True},
        {"args": ("applepenapple", ["apple","pen"]), "expected": True},
        {"args": ("catsandog", ["cats","dog","sand","and","cat"]), "expected": False},
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = word_break_brute_force(*args)
        result2 = word_break(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
