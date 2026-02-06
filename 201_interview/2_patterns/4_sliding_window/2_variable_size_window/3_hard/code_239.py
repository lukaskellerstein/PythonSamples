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
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====


def max_sliding_window_brute_force(nums: List[int], k: int) -> List[int]:
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


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    pass


# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([1, 3, -1, -3, 5, 3, 6, 7], 3),
            "expected": [3, 3, 5, 5, 6, 7],
        },
        {
            "args": ([1], 1),
            "expected": [1],
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = max_sliding_window_brute_force(*args)
        result2 = max_sliding_window(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
