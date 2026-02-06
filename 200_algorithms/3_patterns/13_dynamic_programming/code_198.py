
# -----------------------
# House Robber (LeetCode 198)
# -----------------------

# Difficulty: Medium
# Sub-pattern: 1D DP (Linear)

# Problem: You are a robber planning to rob houses along a street. Each house
# has a certain amount of money stashed. Adjacent houses have security systems
# connected — if two adjacent houses are broken into on the same night, the
# police will be contacted. Given an integer array nums representing the amount
# of money of each house, return the maximum amount of money you can rob
# tonight without alerting the police.

# -----------------------

# For houses [2,7,9,3,1], the max is 12 (rob houses 0, 2, 4 → 2+9+1=12).
nums = [2, 7, 9, 3, 1]

# ----------------------------------------------------
# Bottom-Up DP solution (space-optimized)
#
# time complexity = O(n) - single pass
# space complexity = O(1) - only two variables
# ----------------------------------------------------


def rob(nums):
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    # dp[i] = max money robbing from house 0..i
    # Recurrence: dp[i] = max(dp[i-1], dp[i-2] + nums[i])
    #   - skip house i → take dp[i-1]
    #   - rob house i  → take dp[i-2] + nums[i]
    prev2 = 0
    prev1 = 0

    for num in nums:
        curr = max(prev1, prev2 + num)
        prev2 = prev1
        prev1 = curr

    return prev1


# Example
print(rob(nums))  # 12


# ----------------------------------------------------
# Top-Down (Memoization) solution
#
# time complexity = O(n) - each subproblem solved once
# space complexity = O(n) - recursion stack + memo dict
# ----------------------------------------------------


def rob_memo(nums):
    memo = {}

    def dp(i):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(dp(i - 1), dp(i - 2) + nums[i])
        return memo[i]

    return dp(len(nums) - 1)


# Example
print(rob_memo(nums))  # 12


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^n) - at each house decide to rob or skip
# space complexity = O(n) - recursion stack depth
# ----------------------------------------------------


def rob_brute(nums):
    def dp(i):
        if i < 0:
            return 0
        return max(dp(i - 1), dp(i - 2) + nums[i])

    return dp(len(nums) - 1)


# Example
print(rob_brute(nums))  # 12
