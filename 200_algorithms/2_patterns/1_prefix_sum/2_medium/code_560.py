
# -----------------------
# Subarray Sum Equals K (LeetCode 560)
# -----------------------

# Difficulty: Medium

# Problem: Given an array of integers nums and an integer k, return the total
# number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.

# -----------------------
# VISUALIZATION
# -----------------------
#
# Input: nums = [3, 4, 7, 2, -3, 1, 4, 2], k = 7
# Output: 4
#
# Subarrays that sum to 7:
#   [3, 4]           → 3 + 4 = 7 ✓
#   [7]              → 7 = 7 ✓
#   [7, 2, -3, 1]    → 7 + 2 - 3 + 1 = 7 ✓
#   [1, 4, 2]        → 1 + 4 + 2 = 7 ✓
#
# -----------------------

# For given array, count subarrays that sum to k
nums = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7

# ----------------------------------------------------
# Prefix Sum + HashMap solution
#
# time complexity = O(n) - single pass
# space complexity = O(n) - hashmap storing prefix sums
#
# Key insight: If prefix_sum[j] - prefix_sum[i] = k,
# then subarray from i+1 to j sums to k.
# So we look for (current_prefix - k) in our seen prefix sums.
# ----------------------------------------------------

# def subarray_sum(nums, k):
#     count = 0
#     prefix_sum = 0
#     seen = {0: 1}  # prefix_sum → count of occurrences

#     for num in nums:
#         prefix_sum += num

#         # If (prefix_sum - k) exists, we found valid subarrays
#         target = prefix_sum - k
#         if target in seen:
#             count += seen[target]

#         # Record current prefix sum
#         seen[prefix_sum] = seen.get(prefix_sum, 0) + 1

#     return count


# ????
def subarray_sum(nums, k):

    cumulativeSum = []
    cumulativeSum.append(0)

    for num in nums:
        cumulativeSum.append(cumulativeSum[-1]+num)

    #    [3, 4, 7,  2,  -3,  1,  4,  2]  <- original nums
    # [0, 3, 7, 14, 16, 13, 14, 18, 20] <- cumulativeSum

    count = 0
    seen = {0: 1} # prefix_sum → how many times we've seen it

    for cs in cumulativeSum:
        target = cs - k

        # if we've seen this target before, those are all valid subarrays
        if target in seen:
            count += seen[target]

        # record current prefix sum
        seen[cs] = seen.get(cs, 0) + 1

    return count


# Example
print(subarray_sum(nums, k))  # 4


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n²) - check all subarrays
# space complexity = O(1) - no extra space
# ----------------------------------------------------

def subarray_sum_brute_force(nums, k):
    n = len(nums)
    count = 0

    # Check all possible subarrays
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            if current_sum == k:
                count += 1

    return count


# Example
print(subarray_sum_brute_force(nums, k))  # 4


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        ([3, 4, 7, 2, -3, 1, 4, 2], 7),  # 4
        ([1, 1, 1], 2),                   # 2 -> [1,1] at index 0-1 and 1-2
        ([1, 2, 3], 3),                   # 2 -> [1,2] and [3]
        ([1], 1),                         # 1
        ([1, -1, 0], 0),                  # 3 -> [1,-1], [-1,0,1-1? no], [0], [1,-1,0]
    ]

    print("\nSubarray Sum Equals K Results:")
    print("-" * 55)
    print(f"{'Array':<25} {'k':<5} {'Prefix':<10} {'Brute':<10}")
    print("-" * 55)
    for arr, target in test_cases:
        result1 = subarray_sum(arr, target)
        result2 = subarray_sum_brute_force(arr, target)
        arr_str = str(arr) if len(str(arr)) < 23 else str(arr)[:20] + "..."
        print(f"{arr_str:<25} {target:<5} {result1:<10} {result2:<10}")
