
# ============================================================
# PROBLEM: Permutations (LeetCode 46)
# ============================================================
# Difficulty: Medium
# Pattern: Backtracking
#
# Given an array nums of distinct integers, return all the possible
# permutations. You can return the answer in any order. Each permutation
# must use every element exactly once.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums = [1,2,3]
#   Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#   Explanation: All 6 permutations of three distinct elements.
#
# Example 2:
#   Input: nums = [0,1]
#   Output: [[0,1],[1,0]]
#
# Example 3:
#   Input: nums = [1]
#   Output: [[1]]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= nums.length <= 6
# - -10 <= nums[i] <= 10
# - All the integers of nums are unique
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Decision tree for [1, 2, 3]:
#
#                       []
#                /       |       \
#             [1]       [2]      [3]
#            /   \     /   \    /   \
#         [1,2] [1,3] [2,1] [2,3] [3,1] [3,2]
#          |     |     |     |     |      |
#       [1,2,3] [1,3,2] [2,1,3] [2,3,1] [3,1,2] [3,2,1]
#
# Backtracking pattern: Choose -> Explore -> Undo
#

from typing import List


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Shrinking remaining list)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def permute_brute_force(nums: List[int]) -> List[List[int]]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Backtracking with used set)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def permute(nums: List[int]) -> List[List[int]]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([1,2,3],),
            "expected": [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        },
        {
            "args": ([0,1],),
            "expected": [[0,1],[1,0]]
        },
        {
            "args": ([1],),
            "expected": [[1]]
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = sorted(test["expected"])

        result1 = sorted(permute_brute_force(*args))
        result2 = sorted(permute(*args))

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
