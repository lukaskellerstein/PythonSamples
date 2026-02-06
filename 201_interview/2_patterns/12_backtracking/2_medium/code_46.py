
# ============================================================
# PROBLEM: Permutations (LeetCode 46)
# ============================================================
# Difficulty: Medium
# Pattern: Backtracking
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order. Each permutation
# must use every element exactly once.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1,2,3]
#   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#   Explanation: All 6 permutations of three distinct elements.
#
# Example 2:
#   Input: nums = [0,1]
#   Output: [[0,1],[1,0]]
#
# Example 3:
#   Input: nums = [1]
#   Output: [[1]]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= nums.length <= 6
# - -10 <= nums[i] <= 10
# - All the integers of nums are unique
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Decision tree for [1, 2, 3]:
#
#                       []
#                /       |       \
#             [1]       [2]      [3]
#            /   \     /   \    /   \
#         [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
#          |     |     |     |     |      |
#       [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
#
# Backtracking pattern: Choose -> Explore -> Undo
#

from typing import List


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Shrinking remaining list)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def permute_brute_force(nums: List[int]) -> List[List[int]]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Backtracking with used set)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def permute(nums: List[int]) -> List[List[int]]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
