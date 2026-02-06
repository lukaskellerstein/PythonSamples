
# -----------------------
# Sum of Subarray Minimums (LeetCode 907)
# -----------------------

# Difficulty: Medium
# Sub-pattern: Monotonic Stack + Contribution Counting

# Problem: Given an array of integers arr, find the sum of min(b) for every
# (contiguous) subarray b of arr. Since the answer may be large, return
# the answer modulo 10^9 + 7.

# -----------------------

# For arr=[3,1,2,4] → 17
# Subarrays and their minimums:
# [3]=3, [1]=1, [2]=2, [4]=4, [3,1]=1, [1,2]=1, [2,4]=2,
# [3,1,2]=1, [1,2,4]=1, [3,1,2,4]=1 → sum = 17
arr = [3, 1, 2, 4]

# ----------------------------------------------------
# Monotonic Stack — Contribution Counting solution
#
# Key insight: Instead of checking every subarray, for each element
# compute HOW MANY subarrays it is the minimum of.
#
# For arr[i], find:
#   - PLE (Previous Less Element) distance: number of elements to the left
#     until we hit a strictly smaller element → left[i]
#   - NLE (Next Less-or-Equal Element) distance: number of elements to the
#     right until we hit a smaller-or-equal element → right[i]
#
# arr[i] is the minimum of left[i] * right[i] subarrays.
# Contribution of arr[i] = arr[i] * left[i] * right[i].
#
# Note: We use strict < on left and <= on right (or vice versa) to avoid
# double-counting duplicates.
#
# time complexity = O(n) - two stack passes
# space complexity = O(n) - left/right arrays + stacks
# ----------------------------------------------------

MOD = 10**9 + 7


def sum_subarray_mins(arr):
    n = len(arr)
    left = [0] * n  # distance to previous less element
    right = [0] * n  # distance to next less-or-equal element

    # Find Previous Less Element (strictly less) distances
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        # Distance from i to its PLE (or to the left boundary)
        left[i] = i - stack[-1] if stack else i + 1
        stack.append(i)

    # Find Next Less-or-Equal Element distances
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        # Distance from i to its NLE (or to the right boundary)
        right[i] = stack[-1] - i if stack else n - i
        stack.append(i)

    # Sum contributions
    result = 0
    for i in range(n):
        result = (result + arr[i] * left[i] * right[i]) % MOD

    return result


# Example
print(sum_subarray_mins(arr))  # 17


# ----------------------------------------------------
# Single-Pass Monotonic Stack solution
#
# Process contributions while popping from the stack — when an element
# is popped, we know both its left and right boundaries.
#
# time complexity = O(n) - each element pushed and popped once
# space complexity = O(n) - stack
# ----------------------------------------------------


def sum_subarray_mins_single_pass(arr):
    n = len(arr)
    stack = []  # stores indices, values are in increasing order
    result = 0

    for i in range(n + 1):
        # Use -inf as sentinel to flush remaining elements
        curr = arr[i] if i < n else -1

        while stack and curr <= arr[stack[-1]]:
            mid = stack.pop()
            left_boundary = stack[-1] if stack else -1
            right_boundary = i

            # Number of subarrays where arr[mid] is the minimum
            left_count = mid - left_boundary
            right_count = right_boundary - mid

            result = (result + arr[mid] * left_count * right_count) % MOD

        stack.append(i)

    return result


# Example
print(sum_subarray_mins_single_pass(arr))  # 17


# ----------------------------------------------------
# Brute Force solution
#
# Check every subarray and find its minimum.
#
# time complexity = O(n^2) - enumerate all subarrays
# space complexity = O(1)
# ----------------------------------------------------


def sum_subarray_mins_brute(arr):
    n = len(arr)
    result = 0

    for i in range(n):
        curr_min = arr[i]
        for j in range(i, n):
            curr_min = min(curr_min, arr[j])
            result += curr_min

    return result % MOD


# Example
print(sum_subarray_mins_brute(arr))  # 17
