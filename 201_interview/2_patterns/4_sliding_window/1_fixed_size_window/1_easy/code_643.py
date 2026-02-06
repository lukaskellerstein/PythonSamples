from typing import List


# ============================================================
# PROBLEM: Maximum Average Subarray I (LeetCode 643)
# ============================================================
# Difficulty: Easy
# Pattern: Sliding Window (Fixed Size)
#
# Given an integer array nums and an integer k, find the contiguous
# subarray of length k that has the maximum average value, and return
# this value. You must find a subarray of exactly length k.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1, 12, -5, -6, 50, 3], k = 4
#   Output: 12.75
#   Explanation: Maximum average is (12 + (-5) + (-6) + 50) / 4 = 12.75
#
# Example 2:
#   Input: nums = [5], k = 1
#   Output: 5.0
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - n == nums.length
# - 1 <= k <= n <= 10^5
# - -10^4 <= nums[i] <= 10^4
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums = [1, 12, -5, -6, 50, 3],  k = 4
#
# Window 1: [1, 12, -5, -6]  -> sum =  2,  avg = 0.50
# Window 2: [12, -5, -6, 50] -> sum = 51,  avg = 12.75  <-- max
# Window 3: [-5, -6, 50,  3] -> sum = 42,  avg = 10.50
#
# Sliding: remove leftmost, add rightmost each step.
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


def find_max_average_brute_force(nums: List[int], k: int) -> float:
    pass


# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====


def find_max_average(nums: List[int], k: int) -> float:
    pass


# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([1, 12, -5, -6, 50, 3], 4),
            "expected": 12.75,
        },
        {
            "args": ([5], 1),
            "expected": 5.0,
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = find_max_average_brute_force(*args)
        result2 = find_max_average(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
