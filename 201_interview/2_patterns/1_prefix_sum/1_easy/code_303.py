from typing import List


# ============================================================
# PROBLEM: Range Sum Query - Immutable (LeetCode 303)
# ============================================================
# Difficulty: Easy
# Pattern: Prefix Sum
#
# Given an integer array nums, implement a class that handles
# multiple queries to calculate the sum of elements between
# indices left and right (inclusive). The array does not change
# between queries.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#          query: sumRange(2, 6)
#   Output: 25
#   Explanation: 3 + 4 + 5 + 6 + 7 = 25
#
# Example 2:
#   Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#          query: sumRange(0, 0)
#   Output: 1
#   Explanation: Only element at index 0.
#
# Example 3:
#   Input: nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#          query: sumRange(0, 9)
#   Output: 55
#   Explanation: Sum of all elements 1 through 10.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= nums.length <= 10^4
# - -10^5 <= nums[i] <= 10^5
# - 0 <= left <= right < nums.length
# - At most 10^4 calls will be made to sumRange
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums:         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# index:         0  1  2  3  4  5  6  7  8   9
#
# prefix_sum: [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55]
# index:       0  1  2  3   4   5   6   7   8   9  10
#
# sumRange(2, 6) = prefix_sum[7] - prefix_sum[2] = 28 - 3 = 25
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: Use range(left, right+1, 1) and sum += nums[i]
# Time Complexity: O(1) init, O(n) per query
# Space Complexity: O(n)
# ===== END ANSWER =====

# ===== YOUR CODE =====

class NumArrayBruteForce:

    def __init__(self, nums: List[int]):
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Prefix Sum)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: Precalculate a sum of values and use them to calculate the query sum
# Time Complexity: O(n) init, O(1) per query
# Space Complexity: O(n)
# ===== END ANSWER =====

# ===== YOUR CODE =====

class NumArray:

    def __init__(self, nums: List[int]):
        pass

    def sumRange(self, left: int, right: int) -> int:
        pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    test_cases = [
        {
            "args": (0, 0),
            "expected": 1
        },
        {
            "args": (0, 9),
            "expected": 55
        },
        {
            "args": (2, 6),
            "expected": 25
        },
        {
            "args": (5, 8),
            "expected": 30
        },
    ]

    bf = NumArrayBruteForce(test_nums)
    opt = NumArray(test_nums)

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = bf.sumRange(*args)
        result2 = opt.sumRange(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
