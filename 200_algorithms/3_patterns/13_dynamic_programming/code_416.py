
# -----------------------
# Partition Equal Subset Sum (LeetCode 416)
# -----------------------

# Difficulty: Medium
# Sub-pattern: Knapsack Variants (0/1 Knapsack)

# Problem: Given an integer array nums, return true if you can partition the
# array into two subsets such that the sum of the elements in both subsets
# is equal.

# -----------------------

# For nums=[1,5,11,5], total=22, target=11 → [1,5,5] and [11] → True.
nums = [1, 5, 11, 5]

# ----------------------------------------------------
# Bottom-Up DP solution (1D boolean array)
#
# time complexity = O(n * target) - n=len(nums), target=sum/2
# space complexity = O(target) - dp set or array
# ----------------------------------------------------


def can_partition(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    # dp[j] = True if we can form sum j using a subset of nums
    dp = [False] * (target + 1)
    dp[0] = True

    for num in nums:
        # Traverse right-to-left so each num is used at most once (0/1 knapsack)
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]

    return dp[target]


# Example
print(can_partition(nums))  # True


# ----------------------------------------------------
# Set-based DP solution
#
# time complexity = O(n * target) - at most target sums tracked
# space complexity = O(target) - set of reachable sums
# ----------------------------------------------------


def can_partition_set(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2
    reachable = {0}

    for num in nums:
        new_reachable = set()
        for s in reachable:
            if s + num == target:
                return True
            if s + num < target:
                new_reachable.add(s + num)
        reachable |= new_reachable

    return target in reachable


# Example
print(can_partition_set(nums))  # True


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^n) - include/exclude each element
# space complexity = O(n) - recursion stack depth
# ----------------------------------------------------


def can_partition_brute(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False

    target = total // 2

    def dp(i, remaining):
        if remaining == 0:
            return True
        if i < 0 or remaining < 0:
            return False
        # Include nums[i] or exclude it
        return dp(i - 1, remaining - nums[i]) or dp(i - 1, remaining)

    return dp(len(nums) - 1, target)


# Example
print(can_partition_brute(nums))  # True
