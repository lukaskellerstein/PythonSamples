
# -----------------------
# Sliding Window Maximum (LeetCode 239)
# -----------------------

# Difficulty: Hard

# Problem: You are given an array of integers nums, and there is a sliding window
# of size k which is moving from the left to the right of the array. You can only
# see the k numbers in the window. Each time the sliding window moves right by one
# position, return the max element in the window.

# -----------------------

# For given array [1,3,-1,-3,5,3,6,7] and k=3, return max of each window.
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

# ----------------------------------------------------
# Sliding Window with Monotonic Deque solution
#
# time complexity = O(n) - each element added/removed from deque at most once
# space complexity = O(k) - deque stores at most k elements
# ----------------------------------------------------

from collections import deque


def max_sliding_window(nums, k):
    if not nums:
        return []

    result = []
    # Deque stores indices, maintains decreasing order of values
    dq = deque()

    for i in range(len(nums)):
        # Remove indices outside the current window
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove smaller elements from the back (they can't be max)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        # Add current index
        dq.append(i)

        # Add to result once we have a full window
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result


# Example
print(max_sliding_window(nums, k))  # [3, 3, 5, 5, 6, 7]


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n * k) - for each window, find max in k elements
# space complexity = O(1) - excluding output array
# ----------------------------------------------------


def max_sliding_window_brute_force(nums, k):
    if not nums:
        return []

    result = []
    n = len(nums)

    # Check each window of size k
    for i in range(n - k + 1):
        # Find max in current window
        window_max = nums[i]
        for j in range(i, i + k):
            window_max = max(window_max, nums[j])
        result.append(window_max)

    return result


# Example
print(max_sliding_window_brute_force(nums, k))  # [3, 3, 5, 5, 6, 7]
