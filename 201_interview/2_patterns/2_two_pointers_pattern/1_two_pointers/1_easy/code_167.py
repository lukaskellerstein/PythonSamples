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

# ===== YOUR ANSWER =====
# Approach: Two for-loops - outer and inner, compare all numbers, remove duplicated indexes
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Two Pointers)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: two pointers in one loop
# Time Complexity: O(n)
# Space Complexity: O(1)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def two_sum(nums: List[int], target: int) -> List[int]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([1, 3, 4, 5, 6, 7, 10, 11], 9),
            "expected": [1, 4]
        },
        {
            "args": ([2, 7, 11, 15], 9),
            "expected": [0, 1]
        },
        {
            "args": ([2, 3, 4], 6),
            "expected": [0, 2]
        },
        {
            "args": ([-1, 0], -1),
            "expected": [0, 1]
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = two_sum_brute_force(*args)
        result2 = two_sum(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
