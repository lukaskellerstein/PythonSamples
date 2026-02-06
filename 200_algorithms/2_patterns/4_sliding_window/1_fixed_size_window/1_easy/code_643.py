
# -----------------------
# Maximum Average Subarray I (LeetCode 643)
# -----------------------

# Difficulty: Easy

# Problem: Given an integer array nums and an integer k, find the contiguous
# subarray of length k that has the maximum average value, and return this value.

# -----------------------

# For given array [1, 12, -5, -6, 50, 3] and k=4, find max average of subarray of length k.
nums = [1, 12, -5, -6, 50, 3]
k = 4

# ----------------------------------------------------
# Sliding Window solution
#
# time complexity = O(n) - single pass through the array
# space complexity = O(1) - only using variables
# ----------------------------------------------------

def find_max_average(nums, k):
    # Calculate sum of first window
    window_sum = sum(nums[:k])
    max_sum = window_sum

    # Slide the window: add next element, remove first element
    for i in range(k, len(nums)):
        window_sum = window_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum / k


# Example
print(find_max_average(nums, k))  # 12.75 -> (12 + -5 + -6 + 50) / 4


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n * k) - for each position, sum k elements
# space complexity = O(1) - only using variables
# ----------------------------------------------------

def find_max_average_brute_force(nums, k):
    n = len(nums)
    max_avg = float('-inf')

    # Check each possible window of size k
    for i in range(n - k + 1):
        # Calculate sum of current window
        window_sum = 0
        for j in range(i, i + k):
            window_sum += nums[j]

        # Update max average
        avg = window_sum / k
        max_avg = max(max_avg, avg)

    return max_avg


# Example
print(find_max_average_brute_force(nums, k))  # 12.75
