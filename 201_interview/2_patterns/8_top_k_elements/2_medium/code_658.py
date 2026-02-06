from typing import List

# ============================================================
# PROBLEM: Find K Closest Elements (LeetCode 658)
# ============================================================
# Difficulty: Medium
# Pattern: Top K Elements
#
# Given a sorted integer array arr, two integers k and x, return the k closest
# integers to x in the array. The result should also be sorted in ascending order.
#
# An integer a is closer to x than an integer b if:
#   - |a - x| < |b - x|, or
#   - |a - x| == |b - x| and a < b (prefer the smaller element on tie)
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: arr = [1,2,3,4,5], k = 4, x = 3
#   Output: [1,2,3,4]
#   Explanation: Distances from 3: [2,1,0,1,2]. The 4 closest are [1,2,3,4].
#
# Example 2:
#   Input: arr = [1,1,2,3,4,5], k = 4, x = -1
#   Output: [1,1,2,3]
#   Explanation: Distances from -1: [2,2,3,4,5,6]. The 4 closest are [1,1,2,3].
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - 1 <= k <= arr.length
# - 1 <= arr.length <= 10^4
# - arr is sorted in ascending order
# - -10^4 <= arr[i], x <= 10^4
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# arr = [1, 2, 3, 4, 5], k = 4, x = 3
#
# Number line with distances to x=3:
#
#   1     2     3     4     5
#   |-----|-----|-----|-----|
#   d=2   d=1   d=0   d=1   d=2
#
# We need to find a window of size k=4:
#   Window [1,2,3,4]: total distances = 2+1+0+1 = 4
#   Window [2,3,4,5]: total distances = 1+0+1+2 = 4
#   Tie: prefer the window starting with the smaller element -> [1,2,3,4]
#
# Binary search approach: search for left boundary of the window
#   left=0, right=len(arr)-k = 1
#   mid=0: compare |arr[0]-x| vs |arr[0+k]-x| => |1-3|=2 vs |5-3|=2
#          2 <= 2 => right = 0 => window starts at index 0 => [1,2,3,4]
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def find_closest_elements_brute_force(arr: List[int], k: int, x: int) -> List[int]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def find_closest_elements(arr: List[int], k: int, x: int) -> List[int]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1
    assert find_closest_elements_brute_force([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]
    assert find_closest_elements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]

    # Test case 2: Target outside array range (negative)
    assert find_closest_elements_brute_force([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3]
    assert find_closest_elements([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3]

    # Test case 3: Target outside array range (left side)
    assert find_closest_elements([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]
    assert find_closest_elements_brute_force([1, 2, 3, 4, 5], 4, -1) == [1, 2, 3, 4]

    # Test case 4: k equals array length
    assert find_closest_elements([1, 2, 3], 3, 2) == [1, 2, 3]

    print("All test cases passed!")
