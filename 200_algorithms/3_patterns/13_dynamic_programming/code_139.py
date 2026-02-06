
# -----------------------
# Word Break (LeetCode 139)
# -----------------------

# Difficulty: Medium
# Sub-pattern: 1D DP (Linear)

# Problem: Given a string s and a dictionary of strings wordDict, return true
# if s can be segmented into a space-separated sequence of one or more
# dictionary words. The same word in the dictionary may be reused multiple
# times in the segmentation.

# -----------------------

# For s="leetcode" and wordDict=["leet","code"], return True
# because "leetcode" can be segmented as "leet code".
s = "leetcode"
wordDict = ["leet", "code"]

# ----------------------------------------------------
# Bottom-Up DP solution
#
# time complexity = O(n^2 * m) - n=len(s), m=avg word length for slicing
# space complexity = O(n) - dp array
# ----------------------------------------------------


def word_break(s, wordDict):
    word_set = set(wordDict)
    n = len(s)

    # dp[i] = True if s[0:i] can be segmented into dictionary words
    dp = [False] * (n + 1)
    dp[0] = True  # empty string is always valid

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break

    return dp[n]


# Example
print(word_break(s, wordDict))  # True


# ----------------------------------------------------
# Top-Down (Memoization) solution
#
# time complexity = O(n^2 * m) - n subproblems, each checks up to n splits
# space complexity = O(n) - memo dict + recursion stack
# ----------------------------------------------------


def word_break_memo(s, wordDict):
    word_set = set(wordDict)
    memo = {}

    def dp(start):
        if start == len(s):
            return True
        if start in memo:
            return memo[start]

        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and dp(end):
                memo[start] = True
                return True

        memo[start] = False
        return False

    return dp(0)


# Example
print(word_break_memo(s, wordDict))  # True


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^n) - try every possible split
# space complexity = O(n) - recursion stack depth
# ----------------------------------------------------


def word_break_brute(s, wordDict):
    word_set = set(wordDict)

    def dp(start):
        if start == len(s):
            return True
        for end in range(start + 1, len(s) + 1):
            if s[start:end] in word_set and dp(end):
                return True
        return False

    return dp(0)


# Example
print(word_break_brute(s, wordDict))  # True
