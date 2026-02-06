
# -----------------------
# Find the Duplicate Number (LeetCode 287)
# -----------------------

# Difficulty: Medium

# Problem: Given an array of integers nums containing n + 1 integers where each
# integer is in the range [1, n] inclusive, there is only one repeated number.
# Return this repeated number. You must solve it without modifying the array
# and using only constant extra space.

# -----------------------

# For given array [1, 3, 4, 2, 2], find the duplicate number.
# Follow the chain: 0 → 1 → 3 → 2 → 4 → 2 → 4 → 2 ...
#                                 ↑              |
#                                 └──────────────┘
# Duplicate (2) = cycle entrance
nums = [1, 3, 4, 2, 2]

# ----------------------------------------------------
# Floyd's Cycle Detection (Tortoise and Hare) solution
#
# time complexity = O(n) - linear traversal
# space complexity = O(1) - only two pointers
# ----------------------------------------------------


def find_duplicate(nums):
    # Treat array as linked list: index → nums[index]
    slow = nums[0]
    fast = nums[0]

    # Phase 1: Find meeting point inside the cycle
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Phase 2: Find cycle entrance (the duplicate)
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


# Example
print(find_duplicate(nums))  # 2
print(find_duplicate([3, 1, 3, 4, 2]))  # 3


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n^2) - compare each pair
# space complexity = O(1) - no extra space
# ----------------------------------------------------


def find_duplicate_brute_force(nums):
    n = len(nums)

    # Compare each element with every other element
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return nums[i]

    return -1


# Example
print(find_duplicate_brute_force(nums))  # 2


# ----------------------------------------------------
# Sorting solution (modifies array - not allowed by problem)
#
# time complexity = O(n log n) - sorting
# space complexity = O(1) or O(n) - depending on sort implementation
# ----------------------------------------------------


def find_duplicate_sorting(nums):
    nums_sorted = sorted(nums)

    # Adjacent duplicates after sorting
    for i in range(1, len(nums_sorted)):
        if nums_sorted[i] == nums_sorted[i - 1]:
            return nums_sorted[i]

    return -1


# Example
print(find_duplicate_sorting(nums))  # 2
