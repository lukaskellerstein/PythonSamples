
# -----------------------
# Range Sum Query - Immutable (LeetCode 303)
# -----------------------

# Difficulty: Easy

# Problem: Given an integer array nums, handle multiple queries of the following type:
# Calculate the sum of the elements of nums between indices left and right inclusive.

# -----------------------

# For given array [1,2,3,4,5,6,7,8,9,10] sum elements between index 2 and 6
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from typing import List

# ----------------------------------------------------
# Prefix Sum solution (Iterative)
#
# time complexity = O(n) init, O(1) per query
# space complexity = O(n) - storing prefix sums
# ----------------------------------------------------

class NumArray:

    def __init__(self, nums: List[int]):
        self.original = nums

        self.cumulative = [0]
        for num in nums:
            self.cumulative.append(self.cumulative[-1]+num)


    def sumRange(self, left: int, right: int) -> int:

        leftSum = self.cumulative[left]
        rightSum = self.cumulative[right+1]

        return rightSum - leftSum


# Example
arr = NumArray(nums)
print(arr.sumRange(2, 6))  # 25 -> 3+4+5+6+7


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(1) init, O(n) per query
# space complexity = O(1) - no extra space
# ----------------------------------------------------

class NumArrayBruteForce:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        total = 0
        for i in range(left, right + 1):
            total += self.nums[i]
        return total


# Example
arr_bf = NumArrayBruteForce(nums)
print(arr_bf.sumRange(2, 6))  # 25 -> 3+4+5+6+7


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    test_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    arr_prefix = NumArray(test_nums)
    arr_brute = NumArrayBruteForce(test_nums)

    test_queries = [
        (0, 0),   # 1
        (0, 9),   # 55 (sum of 1-10)
        (2, 6),   # 25 (3+4+5+6+7)
        (5, 8),   # 30 (6+7+8+9)
    ]

    print("\nRange Sum Query Results:")
    print("-" * 50)
    print(f"{'Query':<15} {'Prefix Sum':<15} {'Brute Force':<15}")
    print("-" * 50)
    for left, right in test_queries:
        result1 = arr_prefix.sumRange(left, right)
        result2 = arr_brute.sumRange(left, right)
        print(f"[{left}, {right}]".ljust(15) + f"{result1}".ljust(15) + f"{result2}".ljust(15))
