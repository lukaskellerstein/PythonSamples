
# -----------------------
# Valid Palindrome (LeetCode 125)
# -----------------------

# Dificulty: Easy

# Problem: Given a string, determine if it is a palindrome.
# A palindrome reads the same forward and backward.

# -----------------------

# For given string "racecar", check if it is a palindrome.
s = "racecar"

# ----------------------------------------------------
# Two Pointers solution
#
# time complexity = O(n) - single pass, comparing from both ends
# space complexity = O(1) - only using two pointers
# ----------------------------------------------------


def is_palindrome(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        if arr[left] != arr[right]:
            return False
        else:
            left += 1
            right -= 1

    return True


# Example
print(is_palindrome(s))  # True


# ----------------------------------------------------
# Brute Force solution (reverse and compare)
#
# time complexity = O(n) - reversing string takes O(n)
# space complexity = O(n) - creating reversed copy of string
# ----------------------------------------------------

def is_palindrome_brute_force(s):
    # Reverse the string and compare
    reversed_s = s[::-1]
    return s == reversed_s


# Example
print(is_palindrome_brute_force(s))  # True


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        "racecar",   # True - classic palindrome
        "hello",     # False
        "madam",     # True
        "python",    # False
        "a",         # True - single char
        "aa",        # True
        "ab",        # False
        ""           # True - empty string
    ]

    print("\nPalindrome Test Results:")
    print("-" * 40)
    print(f"{'String':<15} {'Two Pointers':<15} {'Brute Force':<15}")
    print("-" * 40)
    for test in test_cases:
        result1 = is_palindrome(test)
        result2 = is_palindrome_brute_force(test)
        print(f"'{test}'".ljust(15) + f"{result1}".ljust(15) + f"{result2}".ljust(15))
