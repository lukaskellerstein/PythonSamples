from typing import List


# ============================================================
# PROBLEM: Two Sum II - Input Array Is Sorted (LeetCode 167)
# ============================================================
# Difficulty: Easy
# Pattern: Two Pointers
#
# Given a 1-indexed array of integers that is already sorted in
# non-decreasing order, find two numbers such that they add up
# to a specific target number. Return the indices of the two
# numbers (0-indexed in this implementation).
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1, 3, 4, 5, 6, 7, 10, 11], target = 9
#   Output: [1, 4]
#   Explanation: nums[1] + nums[4] = 3 + 6 = 9
#
# Example 2:
#   Input: nums = [2, 7, 11, 15], target = 9
#   Output: [0, 1]
#   Explanation: nums[0] + nums[1] = 2 + 7 = 9
#
# Example 3:
#   Input: nums = [2, 3, 4], target = 6
#   Output: [0, 2]
#   Explanation: nums[0] + nums[2] = 2 + 4 = 6
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 2 <= nums.length <= 3 * 10^4
# - -1000 <= nums[i] <= 1000
# - nums is sorted in non-decreasing order
# - -1000 <= target <= 1000
# - Exactly one solution exists
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums = [1, 3, 4, 5, 6, 7, 10, 11], target = 9
#
# Step 1: left=0(1), right=7(11) -> sum=12 > 9 -> move right
# Step 2: left=0(1), right=6(10) -> sum=11 > 9 -> move right
# Step 3: left=0(1), right=5(7)  -> sum=8  < 9 -> move left
# Step 4: left=1(3), right=5(7)  -> sum=10 > 9 -> move right
# Step 5: left=1(3), right=4(6)  -> sum=9  = 9 -> FOUND [1, 4]
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Two Pointers)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def two_sum(nums: List[int], target: int) -> List[int]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    test_cases = [
        ([1, 3, 4, 5, 6, 7, 10, 11], 9),   # Expected: [1, 4]
        ([2, 7, 11, 15], 9),                 # Expected: [0, 1]
        ([2, 3, 4], 6),                      # Expected: [0, 2]
        ([-1, 0], -1),                       # Expected: [0, 1]
    ]

    pass
