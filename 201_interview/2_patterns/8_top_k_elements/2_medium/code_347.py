from typing import List

# ============================================================
# PROBLEM: Top K Frequent Elements (LeetCode 347)
# ============================================================
# Difficulty: Medium
# Pattern: Top K Elements
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order. It is guaranteed that
# the answer is unique.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1,1,1,2,2,3], k = 2
#   Output: [1,2]
#   Explanation: Element 1 appears 3 times, element 2 appears 2 times,
#                element 3 appears 1 time. The 2 most frequent are [1, 2].
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
# - k is in the range [1, the number of unique elements in the array]
# - It is guaranteed that the answer is unique
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums = [1,1,1,2,2,3], k = 2
#
# Step 1: Count frequencies
#   {1: 3, 2: 2, 3: 1}
#
# Step 2: Min-heap of size k=2 (by frequency)
#   Process (3, 1): heap = [(3, 1)]
#   Process (2, 2): heap = [(2, 2), (3, 1)]
#   Process (1, 3): heap = [(2, 2), (3, 1)], push (1,3) -> pop min (1,3)
#                   heap = [(2, 2), (3, 1)]
#
#   Result: [2, 1] (or [1, 2] -- any order is valid)
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def top_k_frequent_brute_force(nums: List[int], k: int) -> List[int]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def top_k_frequent(nums: List[int], k: int) -> List[int]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1
    result = top_k_frequent_brute_force([1, 1, 1, 2, 2, 3], 2)
    assert sorted(result) == [1, 2]

    result = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(result) == [1, 2]

    # Test case 2: Single element
    assert top_k_frequent([1], 1) == [1]

    # Test case 3: All same frequency, k equals number of unique elements
    result = top_k_frequent([1, 2, 3], 3)
    assert sorted(result) == [1, 2, 3]

    # Test case 4: Negative numbers
    result = top_k_frequent([-1, -1, -2, -2, -2, 3], 2)
    assert sorted(result) == [-2, -1]

    print("All test cases passed!")
