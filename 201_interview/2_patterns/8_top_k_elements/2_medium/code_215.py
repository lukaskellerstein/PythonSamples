from typing import List

# ============================================================
# PROBLEM: Kth Largest Element in an Array (LeetCode 215)
# ============================================================
# Difficulty: Medium
# Pattern: Top K Elements
#
# Given an integer array nums and an integer k, return the kth largest element
# in the array. Note that it is the kth largest element in the sorted order,
# not the kth distinct element. You must solve it without sorting the entire array
# for the optimal solution.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [3,2,1,5,6,4], k = 2
#   Output: 5
#   Explanation: Sorted descending = [6,5,4,3,2,1]. The 2nd largest is 5.
#
# Example 2:
#   Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
#   Output: 4
#   Explanation: Sorted descending = [6,5,5,4,3,3,2,2,1]. The 4th largest is 4.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= k <= nums.length <= 10^5
# - -10^4 <= nums[i] <= 10^4
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums = [3, 2, 1, 5, 6, 4], k = 2
#
# Min-heap approach (size k=2):
#   Process 3: heap = [3]
#   Process 2: heap = [2, 3]
#   Process 1: heap = [2, 3], 1 < 2 (heap min) -> skip (or push+pop)
#   Process 5: push -> [2,3,5], pop min -> heap = [3, 5]
#   Process 6: push -> [3,5,6], pop min -> heap = [5, 6]
#   Process 4: push -> [4,5,6], pop min -> heap = [5, 6]
#
#   Answer = heap[0] = 5 (the kth largest)
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

def find_kth_largest_brute_force(nums: List[int], k: int) -> int:
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

def find_kth_largest(nums: List[int], k: int) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([3, 2, 1, 5, 6, 4], 2),
            "expected": 5
        },
        {
            "args": ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4),
            "expected": 4
        },
        {
            "args": ([1], 1),
            "expected": 1
        },
        {
            "args": ([7, 7, 7, 7], 2),
            "expected": 7
        },
        {
            "args": ([-1, -2, -3, -4], 1),
            "expected": -1
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = find_kth_largest_brute_force(*args)
        result2 = find_kth_largest(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
