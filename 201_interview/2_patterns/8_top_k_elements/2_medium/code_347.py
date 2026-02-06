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

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def top_k_frequent_brute_force(nums: List[int], k: int) -> List[int]:
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

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([1, 1, 1, 2, 2, 3], 2),
            "expected": [1, 2]
        },
        {
            "args": ([1], 1),
            "expected": [1]
        },
        {
            "args": ([1, 2, 3], 3),
            "expected": [1, 2, 3]
        },
        {
            "args": ([-1, -1, -2, -2, -2, 3], 2),
            "expected": [-2, -1]
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = sorted(top_k_frequent_brute_force(*args))
        result2 = sorted(top_k_frequent(*args))

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
