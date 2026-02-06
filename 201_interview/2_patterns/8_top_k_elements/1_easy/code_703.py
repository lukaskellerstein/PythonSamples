from typing import List

# ============================================================
# PROBLEM: Kth Largest Element in a Stream (LeetCode 703)
# ============================================================
# Difficulty: Easy
# Pattern: Top K Elements
#
# Design a class to find the kth largest element in a stream. Note that it is
# the kth largest element in the sorted order, not the kth distinct element.
#
# Implement the KthLargest class:
#   - KthLargest(int k, int[] nums) initializes the object with the integer k
#     and the stream of integers nums.
#   - int add(int val) appends the integer val to the stream and returns the
#     element representing the kth largest element in the stream.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input:
#     KthLargest(3, [4, 5, 8, 2])
#     add(3)  -> 4
#     add(5)  -> 5
#     add(10) -> 5
#     add(9)  -> 8
#     add(4)  -> 8
#   Explanation:
#     After init, stream = [4,5,8,2]. Top 3 largest = [4,5,8], 3rd largest = 4.
#     add(3):  stream=[2,3,4,5,8],   3rd largest = 4
#     add(5):  stream=[2,3,4,5,5,8], 3rd largest = 5
#     add(10): stream=[2,3,4,5,5,8,10], 3rd largest = 5
#     add(9):  stream=[2,3,4,5,5,8,9,10], 3rd largest = 8
#     add(4):  stream=[2,3,4,4,5,5,8,9,10], 3rd largest = 8
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= k <= 10^4
# - 0 <= nums.length <= 10^4
# - -10^4 <= nums[i] <= 10^4
# - -10^4 <= val <= 10^4
# - At most 10^4 calls will be made to add
# - It is guaranteed that there will be at least k elements when you search for the kth element
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# k = 3, nums = [4, 5, 8, 2]
#
# Min-heap of size k=3 keeps the 3 largest elements:
#
#   Init:  heap = [4, 5, 8]  (2 is removed as smallest)
#          kth largest (heap top) = 4
#
#   add(3):  3 < 4 (heap min) -> don't add -> heap = [4, 5, 8]  -> return 4
#   add(5):  push 5 -> [4,5,5,8] -> pop min -> heap = [5, 5, 8] -> return 5
#   add(10): push 10 -> [5,5,8,10] -> pop min -> heap = [5,8,10] -> return 5
#   add(9):  push 9 -> [5,8,9,10] -> pop min -> heap = [8,9,10]  -> return 8
#   add(4):  4 < 8 (heap min) -> don't add -> heap = [8, 9, 10]  -> return 8
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???) for __init__, O(???) for add
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

class KthLargestBruteForce:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???) for __init__, O(???) for add
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        pass

    def add(self, val: int) -> int:
        pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    # Test case 1: k=3
    test_cases_1 = [
        {"add": 3, "expected": 4},
        {"add": 5, "expected": 5},
        {"add": 10, "expected": 5},
        {"add": 9, "expected": 8},
        {"add": 4, "expected": 8},
    ]

    kl_bf = KthLargestBruteForce(3, [4, 5, 8, 2])
    kl = KthLargest(3, [4, 5, 8, 2])

    for test in test_cases_1:
        val = test["add"]
        expected = test["expected"]

        result1 = kl_bf.add(val)
        result2 = kl.add(val)

        assert result1 == expected, f"Brute force failed: add({val}), got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed: add({val}), got {result2}, expected {expected}"

        print(f"add({val}), expected={expected}, brute_force={result1}, optimal={result2} ✓")

    # Test case 2: k=1, empty init
    test_cases_2 = [
        {"add": -3, "expected": -3},
        {"add": -2, "expected": -2},
        {"add": -4, "expected": -2},
        {"add": 0, "expected": 0},
        {"add": 4, "expected": 4},
    ]

    kl_bf2 = KthLargestBruteForce(1, [])
    kl2 = KthLargest(1, [])

    for test in test_cases_2:
        val = test["add"]
        expected = test["expected"]

        result1 = kl_bf2.add(val)
        result2 = kl2.add(val)

        assert result1 == expected, f"Brute force failed: add({val}), got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed: add({val}), got {result2}, expected {expected}"

        print(f"add({val}), expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
