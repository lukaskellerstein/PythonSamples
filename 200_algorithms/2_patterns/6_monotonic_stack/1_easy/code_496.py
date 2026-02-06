
# -----------------------
# Next Greater Element I (LeetCode 496)
# -----------------------

# Difficulty: Easy

# Problem: You are given two distinct 0-indexed integer arrays nums1 and nums2,
# where nums1 is a subset of nums2. For each 0 <= i < nums1.length, find the
# index j such that nums1[i] == nums2[j] and determine the next greater element
# of nums2[j] in nums2. If there is no next greater element, the answer is -1.
# Return an array ans of length nums1.length such that ans[i] is the next
# greater element as described above.

# -----------------------
# VISUALIZATION
# -----------------------
#
# nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]
#
# Process nums2 right to left with monotonic stack:
#   i=3 (val=2): stack=[]       -> next_greater[2]=-1, push 2, stack=[2]
#   i=2 (val=4): pop 2 (2<4),   stack=[] -> next_greater[4]=-1, push 4, stack=[4]
#   i=1 (val=3): peek 4 (4>3),  stack=[4] -> next_greater[3]=4, push 3, stack=[3,4]
#   i=0 (val=1): peek 3 (3>1),  stack=[3,4] -> next_greater[1]=3, push 1, stack=[1,3,4]
#
# Result for nums1=[4,1,2]: [-1, 3, -1]
#
# -----------------------

from typing import List


# ----------------------------------------------------
# Monotonic Stack solution (Optimal)
#
# time complexity = O(n + m) - n = len(nums2), m = len(nums1)
# space complexity = O(n) - hashmap + stack
# ----------------------------------------------------

def next_greater_element(nums1: List[int], nums2: List[int]) -> List[int]:
    # Build a map: for each element in nums2, what's the next greater element?
    next_greater = {}
    stack = []  # monotonic decreasing stack

    for num in nums2:
        # Pop elements smaller than current — current is their next greater
        while stack and stack[-1] < num:
            val = stack.pop()
            next_greater[val] = num
        stack.append(num)

    return [next_greater.get(num, -1) for num in nums1]


# Example
print(next_greater_element([4, 1, 2], [1, 3, 4, 2]))  # [-1, 3, -1]


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(m * n) - for each element in nums1, scan nums2
# space complexity = O(1) - no extra space beyond output
# ----------------------------------------------------

def next_greater_element_brute_force(nums1: List[int], nums2: List[int]) -> List[int]:
    result = []

    for num in nums1:
        # Find num in nums2
        found = False
        greater = -1
        for val in nums2:
            if val == num:
                found = True
            elif found and val > num:
                greater = val
                break
        result.append(greater)

    return result


# Example
print(next_greater_element_brute_force([4, 1, 2], [1, 3, 4, 2]))  # [-1, 3, -1]


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ([1], [1], [-1]),
        ([1, 3, 5], [1, 2, 3, 4, 5], [2, 4, -1]),
    ]

    print("\nNext Greater Element I Results:")
    print("-" * 60)
    print(f"{'nums1':<15} {'nums2':<20} {'Optimal':<15} {'Brute':<15}")
    print("-" * 60)

    for nums1, nums2, expected in test_cases:
        result1 = next_greater_element(nums1, nums2)
        result2 = next_greater_element_brute_force(nums1, nums2)
        print(f"{str(nums1):<15} {str(nums2):<20} {str(result1):<15} {str(result2):<15}")
