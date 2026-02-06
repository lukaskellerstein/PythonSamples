
# -----------------------
# Longest Increasing Subsequence (LeetCode 300)
# -----------------------

# Difficulty: Medium
# Sub-pattern: 1D DP (Linear)

# Problem: Given an integer array nums, return the length of the longest
# strictly increasing subsequence. A subsequence is derived from the array
# by deleting some or no elements without changing the order of the
# remaining elements.

# -----------------------

# For array [10,9,2,5,3,7,101,18], the LIS is [2,3,7,101] → length 4.
nums = [10, 9, 2, 5, 3, 7, 101, 18]

# ----------------------------------------------------
# Binary Search + Patience Sorting solution
#
# time complexity = O(n log n) - binary search for each element
# space complexity = O(n) - tails array
# ----------------------------------------------------

import bisect


def length_of_lis(nums):
    # tails[i] = smallest tail element for increasing subsequence of length i+1
    tails = []

    for num in nums:
        pos = bisect.bisect_left(tails, num)
        if pos == len(tails):
            tails.append(num)
        else:
            tails[pos] = num

    return len(tails)


# Example
print(length_of_lis(nums))  # 4


# ----------------------------------------------------
# Bottom-Up DP solution
#
# time complexity = O(n^2) - for each element check all previous
# space complexity = O(n) - dp array
# ----------------------------------------------------


def length_of_lis_dp(nums):
    if not nums:
        return 0

    n = len(nums)
    # dp[i] = length of LIS ending at index i
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# Example
print(length_of_lis_dp(nums))  # 4


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^n) - include/exclude each element
# space complexity = O(n) - recursion stack depth
# ----------------------------------------------------


def length_of_lis_brute(nums):
    def dp(i, prev):
        if i == len(nums):
            return 0
        # Option 1: skip current element
        skip = dp(i + 1, prev)
        # Option 2: take current element (if it's larger than previous)
        take = 0
        if prev < nums[i]:
            take = 1 + dp(i + 1, nums[i])
        return max(skip, take)

    return dp(0, float("-inf"))


# Example
print(length_of_lis_brute(nums))  # 4
