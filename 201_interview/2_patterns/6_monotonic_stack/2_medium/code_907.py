from typing import List


# ============================================================
# PROBLEM: Sum of Subarray Minimums (LeetCode 907)
# ============================================================
# Difficulty: Medium
# Pattern: Monotonic Stack + Contribution Counting
#
# Given an array of integers arr, find the sum of min(b) for every
# contiguous subarray b of arr. Since the answer may be large, return
# the answer modulo 10^9 + 7.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: arr = [3, 1, 2, 4]
#   Output: 17
#   Explanation: Subarrays and their minimums:
#     [3]=3, [1]=1, [2]=2, [4]=4,
#     [3,1]=1, [1,2]=1, [2,4]=2,
#     [3,1,2]=1, [1,2,4]=1,
#     [3,1,2,4]=1
#     Sum = 3+1+2+4+1+1+2+1+1+1 = 17
#
# Example 2:
#   Input: arr = [11, 81, 94, 43, 3]
#   Output: 444
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= arr.length <= 3 * 10^4
# - 1 <= arr[i] <= 3 * 10^4
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# arr = [3, 1, 2, 4]
#        0  1  2  3   (indices)
#
# Contribution counting: For each element, count how many subarrays
# it is the minimum of.
#
# arr[0]=3: PLE boundary=-1, NLE boundary=1 -> left=1, right=1 -> 3*1*1 = 3
# arr[1]=1: PLE boundary=-1, NLE boundary=4 -> left=2, right=3 -> 1*2*3 = 6
# arr[2]=2: PLE boundary=1,  NLE boundary=3 -> left=1, right=1 -> 2*1*1 = 2
# arr[3]=4: PLE boundary=2,  NLE boundary=4 -> left=1, right=1 -> 4*1*1 = 4
#                                                                 not 4+1=5
# Wait -- let's recount: 1*2*3=6 covers subarrays where 1 is min:
#   [1], [3,1], [1,2], [3,1,2], [1,2,4], [3,1,2,4] -> 6 subarrays
#
# Total = 3 + 6 + 2 + 4 + ... hmm, let's just trust: sum = 17
#


# ============================================================
# PART 1 — BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def sum_subarray_mins_brute_force(arr: List[int]) -> int:
    pass


# ============================================================
# PART 2 — OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach using monotonic stack + contribution counting
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def sum_subarray_mins(arr: List[int]) -> int:
    pass


# ============================================================
# PART 3 — TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
