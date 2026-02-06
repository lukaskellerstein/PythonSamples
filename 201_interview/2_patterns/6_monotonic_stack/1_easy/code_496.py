from typing import List


# ============================================================
# PROBLEM: Next Greater Element I (LeetCode 496)
# ============================================================
# Difficulty: Easy
# Pattern: Monotonic Stack
#
# You are given two distinct 0-indexed integer arrays nums1 and nums2,
# where nums1 is a subset of nums2. For each element in nums1, find the
# first element in nums2 that is greater than it and appears to its right
# in nums2. If no such element exists, the answer for that element is -1.
# Return an array of results corresponding to each element of nums1.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
#   Output: [-1, 3, -1]
#   Explanation:
#     4 is at index 2 in nums2; no greater element to the right -> -1
#     1 is at index 0 in nums2; next greater to the right is 3 -> 3
#     2 is at index 3 in nums2; no greater element to the right -> -1
#
# Example 2:
#   Input: nums1 = [2, 4], nums2 = [1, 2, 3, 4]
#   Output: [3, -1]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= nums1.length <= nums2.length <= 1000
# - 0 <= nums1[i], nums2[i] <= 10^4
# - All integers in nums1 and nums2 are unique
# - All integers of nums1 also appear in nums2
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
#
# Process nums2 with monotonic stack (left to right):
#   i=0 (val=1): stack=[1]
#   i=1 (val=3): 3 > 1, pop 1 -> next_greater[1]=3, stack=[3]
#   i=2 (val=4): 4 > 3, pop 3 -> next_greater[3]=4, stack=[4]
#   i=3 (val=2): 2 < 4, push -> stack=[4, 2]
#   End: remaining in stack have no next greater -> next_greater[4]=-1, next_greater[2]=-1
#
# Lookup for nums1: [4->-1, 1->3, 2->-1] = [-1, 3, -1]
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


def next_greater_element_brute_force(
    nums1: List[int], nums2: List[int]
) -> List[int]:
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


def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    pass


# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([4, 1, 2], [1, 3, 4, 2]),
            "expected": [-1, 3, -1],
        },
        {
            "args": ([2, 4], [1, 2, 3, 4]),
            "expected": [3, -1],
        },
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = next_greater_element_brute_force(*args)
        result2 = next_greater_element(*args)

        assert result1 == expected, f"Brute force failed for {args}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {args}: got {result2}, expected {expected}"

        print(f"args={args}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
