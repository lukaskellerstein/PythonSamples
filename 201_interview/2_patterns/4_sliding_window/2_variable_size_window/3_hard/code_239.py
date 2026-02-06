from typing import List
from collections import deque


# ============================================================
# PROBLEM: Sliding Window Maximum (LeetCode 239)
# ============================================================
# Difficulty: Hard
# Pattern: Sliding Window + Monotonic Deque
#
# You are given an array of integers nums and a sliding window of size k
# which moves from the very left of the array to the very right. You can
# only see the k numbers in the window. Each time the sliding window moves
# right by one position, return the maximum element in the window.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
#   Output: [3,3,5,5,6,7]
#   Explanation:
#     Window position              Max
#     ---------------             -----
#     [1  3  -1] -3  5  3  6  7    3
#      1 [3  -1  -3] 5  3  6  7    3
#      1  3 [-1  -3  5] 3  6  7    5
#      1  3  -1 [-3  5  3] 6  7    5
#      1  3  -1  -3 [5  3  6] 7    6
#      1  3  -1  -3  5 [3  6  7]   7
#
# Example 2:
#   Input: nums = [1], k = 1
#   Output: [1]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
# - 1 <= k <= nums.length
#


# ============================================================
# PART 1 — BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def max_sliding_window_brute_force(nums: List[int], k: int) -> List[int]:
    pass


# ============================================================
# PART 2 — OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    pass


# ============================================================
# PART 3 — TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
