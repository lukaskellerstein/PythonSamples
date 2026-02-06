
# -----------------------
# Two Sum II - Input Array Is Sorted (LeetCode 167)
# -----------------------

# Difficulty: Easy

# Problem: Given a sorted array, find two numbers that add up to a target sum.

# -----------------------

# For given sorted array [1, 3, 4, 5, 6, 7, 10, 11] find two number that sums as 9.
nums = [1, 3, 4, 5, 6, 7, 10, 11]
target = 9

# ----------------------------------------------------
# Two Pointers solution
#
# time complexity = O(n)
# space complexity = O(1)
# ----------------------------------------------------

def two_sum(nums, target):

    left_pointer = 0
    right_pointer = len(nums) - 1

    while left_pointer < right_pointer:

        currentSum = nums[left_pointer] + nums[right_pointer]

        if currentSum == target:
            return [left_pointer, right_pointer]
        elif currentSum < target:
            # move left pointer to the bigger value in array => right
            left_pointer += 1
        elif currentSum > target:
            # move right pointer to the smaller value in array => left
            right_pointer -= 1

    return []

# Example
print(two_sum(nums, target))  # [1, 4] → indices of 3 and 6
# ignores the [2, 3] -> 4 and 5


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n^2)
# space complexity = O(1)
# ----------------------------------------------------

def two_sum_brute_force(nums, target):

    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]

    return []


# Example
print(two_sum_brute_force(nums, target))  # [1, 4] → indices of 3 and 6
