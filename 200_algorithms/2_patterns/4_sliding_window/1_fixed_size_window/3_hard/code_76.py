
# -----------------------
# Minimum Window Substring (LeetCode 76)
# -----------------------

# Difficulty: Hard

# Problem: Given two strings s and t, return the minimum window substring of s
# such that every character in t (including duplicates) is included in the window.
# If there is no such substring, return the empty string "".

# -----------------------

# For given strings s = "ADOBECODEBANC" and t = "ABC", find minimum window containing all chars of t.
s = "ADOBECODEBANC"
t = "ABC"

# ----------------------------------------------------
# Sliding Window solution
#
# time complexity = O(n + m) - where n = len(s), m = len(t)
# space complexity = O(m) - for the frequency maps
# ----------------------------------------------------

from collections import Counter


def min_window(s, t):
    if not t or not s:
        return ""

    # Count characters needed from t
    t_count = Counter(t)
    required = len(t_count)

    # Left and right pointers for the window
    left = 0
    # Track how many unique characters we have with required frequency
    formed = 0
    # Window character counts
    window_counts = {}

    # Result: (window length, left, right)
    result = (float("inf"), None, None)

    for right in range(len(s)):
        # Add character from the right
        char = s[right]
        window_counts[char] = window_counts.get(char, 0) + 1

        # Check if current character's frequency matches required frequency
        if char in t_count and window_counts[char] == t_count[char]:
            formed += 1

        # Try to shrink the window until it's no longer valid
        while left <= right and formed == required:
            char = s[left]

            # Update result if this window is smaller
            if right - left + 1 < result[0]:
                result = (right - left + 1, left, right)

            # Remove character from left of window
            window_counts[char] -= 1
            if char in t_count and window_counts[char] < t_count[char]:
                formed -= 1

            left += 1

    return "" if result[0] == float("inf") else s[result[1] : result[2] + 1]


# Example
print(min_window(s, t))  # "BANC"


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n^2 * m) - check all substrings and verify each
# space complexity = O(m) - for the frequency map
# ----------------------------------------------------


def min_window_brute_force(s, t):
    if not t or not s:
        return ""

    t_count = Counter(t)
    min_len = float("inf")
    min_window = ""

    # Check all possible substrings
    for i in range(len(s)):
        for j in range(i + len(t), len(s) + 1):
            substring = s[i:j]

            # Check if substring contains all characters of t
            if is_valid(substring, t_count):
                if len(substring) < min_len:
                    min_len = len(substring)
                    min_window = substring

    return min_window


def is_valid(substring, t_count):
    s_count = Counter(substring)
    for char, count in t_count.items():
        if s_count.get(char, 0) < count:
            return False
    return True


# Example
print(min_window_brute_force(s, t))  # "BANC"
