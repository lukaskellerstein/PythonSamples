from typing import List


# ============================================================
# PROBLEM: 3Sum (LeetCode 15)
# ============================================================
# Difficulty: Medium
# Pattern: Three Pointers (Sort + Two Pointers)
#
# Given an integer array nums, return all the unique triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and
# j != k, and nums[i] + nums[j] + nums[k] == target. The
# solution set must not contain duplicate triplets.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [-1, 0, 1, 2, -1, -4], target = 0
#   Output: [[-1, -1, 2], [-1, 0, 1]]
#   Explanation: nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0
#                nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0
#                The distinct triplets are [-1, 0, 1] and [-1, -1, 2].
#
# Example 2:
#   Input: nums = [0, 1, 1], target = 0
#   Output: []
#   Explanation: No triplet sums to 0.
#
# Example 3:
#   Input: nums = [0, 0, 0], target = 0
#   Output: [[0, 0, 0]]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 3 <= nums.length <= 3000
# - -10^5 <= nums[i] <= 10^5
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums = [-1, 0, 1, 2, -1, -4], target = 0
#
# Step 1: Sort the array -> [-4, -1, -1, 0, 1, 2]
#
# Step 2: Fix first element, use two pointers for the rest:
#
#   i=0 (-4): left=1(-1), right=5(2)
#     -4 + (-1) + 2 = -3 < 0 -> move left
#     -4 + (-1) + 2 = -3 < 0 -> move left
#     ... no triplet found
#
#   i=1 (-1): left=2(-1), right=5(2)
#     -1 + (-1) + 2 = 0 = target -> FOUND [-1, -1, 2]
#     left=3(0), right=4(1)
#     -1 + 0 + 1 = 0 = target -> FOUND [-1, 0, 1]
#
#   i=2 (-1): skip (duplicate of i=1)
#   ...
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def three_sum_brute_force(nums: List[int], target: int) -> List[List[int]]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Sort + Two Pointers)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def three_sum(nums: List[int], target: int) -> List[List[int]]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([-1, 0, 1, 2, -1, -4], 0),
            "expected": [[-1, -1, 2], [-1, 0, 1]]
        },
        {
            "args": ([0, 1, 1], 0),
            "expected": []
        },
        {
            "args": ([0, 0, 0], 0),
            "expected": [[0, 0, 0]]
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = three_sum_brute_force(*args)
        result2 = three_sum(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
