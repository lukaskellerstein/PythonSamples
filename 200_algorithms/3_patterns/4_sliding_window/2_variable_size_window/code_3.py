
# -----------------------
# Longest Substring Without Repeating Characters (LeetCode 3)
# -----------------------

# Difficulty: Medium

# Problem: Given a string s, find the length of the longest substring
# without repeating characters.

# Note: This is the definitive variable-size window problem.
# Common at Google, Meta, and Amazon. Often used as a warm-up.

# -----------------------

# For given string "abcabcbb", find the longest substring without repeating chars.
s = "abcabcbb"

# ----------------------------------------------------
# Sliding Window solution
#
# time complexity = O(n) - each character visited at most twice
# space complexity = O(min(n, m)) - where m is the charset size (26 for lowercase)
# ----------------------------------------------------

def length_of_longest_substring(s):
    char_index = {}  # stores last seen index of each character
    max_length = 0
    left = 0

    for right in range(len(s)):
        # If character already in window, move left pointer
        if s[right] in char_index and char_index[s[right]] >= left:
            left = char_index[s[right]] + 1

        # Update last seen index
        char_index[s[right]] = right

        # Update max length
        max_length = max(max_length, right - left + 1)

    return max_length


# Example
print(length_of_longest_substring(s))  # 3 -> "abc"


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n³) - check all substrings O(n²), each check O(n)
# space complexity = O(min(n, m)) - for the set
# ----------------------------------------------------

def length_of_longest_substring_brute_force(s):
    n = len(s)
    max_length = 0

    # Check all possible substrings
    for i in range(n):
        for j in range(i, n):
            # Check if substring s[i:j+1] has all unique characters
            if has_unique_chars(s, i, j):
                max_length = max(max_length, j - i + 1)

    return max_length


def has_unique_chars(s, start, end):
    seen = set()
    for i in range(start, end + 1):
        if s[i] in seen:
            return False
        seen.add(s[i])
    return True


# Example
print(length_of_longest_substring_brute_force(s))  # 3 -> "abc"


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        "abcabcbb",  # 3 -> "abc"
        "bbbbb",     # 1 -> "b"
        "pwwkew",    # 3 -> "wke"
        "",          # 0
        "a",         # 1
        "abcdef",    # 6 -> entire string
    ]

    print("\nLongest Substring Without Repeating Characters:")
    print("-" * 50)
    print(f"{'String':<15} {'Sliding Window':<15} {'Brute Force':<15}")
    print("-" * 50)
    for test in test_cases:
        result1 = length_of_longest_substring(test)
        result2 = length_of_longest_substring_brute_force(test)
        print(f"'{test}'".ljust(15) + f"{result1}".ljust(15) + f"{result2}".ljust(15))
