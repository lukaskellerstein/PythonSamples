
# -----------------------
# Three Sum (LeetCode 15) — Very Common
# -----------------------

# Dificulty: Medium

# Problem: Given an array of integers, find all unique triplets that sum to a target value.

# -----------------------

# For given array [-1, 0, 1, 2, -1, -4] find all unique triplets that sum to 0.
nums = [-1, 0, 1, 2, -1, -4]
target = 0

# ----------------------------------------------------
# Two Pointers solution
#
# time complexity = O(n²) - sorting O(n log n) + nested loops O(n²)
# space complexity = O(1) - excluding output array
# ----------------------------------------------------

def three_sum(nums, target):

    # Sort the array !!
    nums.sort()

    result = []

    # first pointer
    for i in range(len(nums) - 2):

        # # Skip duplicates for the first element
        # if i > 0 and nums[i] == nums[i - 1]:
        #     continue

        # second pointer
        left = i + 1
        # third pointer
        right = len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                # total == target !!!!!!!!!!
                result.append([nums[i], nums[left], nums[right]])

                # # Skip duplicates for second and third elements
                # while left < right and nums[left] == nums[left + 1]:
                #     left += 1
                # while left < right and nums[right] == nums[right - 1]:
                #     right -= 1

                left += 1
                right -= 1

    return result


# Example
print(three_sum(nums.copy(), target))  # [[-1, -1, 2], [-1, 0, 1]]


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n³) - three nested loops
# space complexity = O(n) - for storing seen triplets to avoid duplicates
# ----------------------------------------------------

def three_sum_brute_force(nums, target):

    n = len(nums)
    result = []
    seen = set()

    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target:
                    # Sort triplet to handle duplicates
                    triplet = tuple(sorted([nums[i], nums[j], nums[k]]))
                    if triplet not in seen:
                        seen.add(triplet)
                        result.append(list(triplet))

    return result


# Example
print(three_sum_brute_force(nums.copy(), target))  # [[-1, -1, 2], [-1, 0, 1]]
