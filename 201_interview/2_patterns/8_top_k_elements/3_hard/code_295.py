

# ============================================================
# PROBLEM: Find Median from Data Stream (LeetCode 295)
# ============================================================
# Difficulty: Hard
# Pattern: Top K Elements
#
# The median is the middle value in an ordered integer list. If the size of the
# list is even, the median is the average of the two middle values.
#
# Implement the MedianFinder class:
#   - MedianFinder() initializes the MedianFinder object.
#   - void addNum(int num) adds the integer num from the data stream to the
#     data structure.
#   - double findMedian() returns the median of all elements so far. Answers
#     within 10^-5 of the actual answer will be accepted.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input:
#     MedianFinder()
#     addNum(1)
#     addNum(2)
#     findMedian() -> 1.5
#     addNum(3)
#     findMedian() -> 2.0
#   Explanation:
#     After addNum(1): list = [1], median = 1
#     After addNum(2): list = [1, 2], median = (1+2)/2 = 1.5
#     After addNum(3): list = [1, 2, 3], median = 2.0
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - -10^5 <= num <= 10^5
# - There will be at least one element before calling findMedian
# - At most 5 * 10^4 calls will be made to addNum and findMedian
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Two-Heap approach: Max-heap (lower half) + Min-heap (upper half)
#
# After addNum(1):
#   lower (max-heap): [1]     upper (min-heap): []
#   Median = top of lower = 1
#
# After addNum(2):
#   lower (max-heap): [1]     upper (min-heap): [2]
#   Median = (1 + 2) / 2 = 1.5
#
# After addNum(3):
#   lower (max-heap): [2, 1]  upper (min-heap): [3]
#   Median = top of lower = 2.0
#
# Invariants:
#   - All elements in lower <= all elements in upper
#   - |len(lower) - len(upper)| <= 1
#   - lower has same size or 1 more element than upper
#
#          lower (max-heap)     |    upper (min-heap)
#          ─────────────────    |    ─────────────────
#   small values ... max_lower  |  min_upper ... large values
#                          ^    |    ^
#                     median comes from these tops
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???) for addNum, O(???) for findMedian
# Space Complexity: O(???)


class MedianFinderBruteForce:

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???) for addNum, O(???) for findMedian
# Space Complexity: O(???)


class MedianFinder:

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1: Basic usage (optimal)
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0

    # Test case 2: Basic usage (brute force)
    mf_bf = MedianFinderBruteForce()
    mf_bf.addNum(1)
    mf_bf.addNum(2)
    assert mf_bf.findMedian() == 1.5
    mf_bf.addNum(3)
    assert mf_bf.findMedian() == 2.0

    # Test case 3: Larger stream
    mf2 = MedianFinder()
    for num in [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0]:
        mf2.addNum(num)
    assert mf2.findMedian() == 3.0  # sorted: [0,0,0,1,2,3,5,6,6,6,10]

    # Test case 4: Single element
    mf3 = MedianFinder()
    mf3.addNum(5)
    assert mf3.findMedian() == 5.0

    # Test case 5: Two elements
    mf4 = MedianFinder()
    mf4.addNum(1)
    mf4.addNum(2)
    assert mf4.findMedian() == 1.5

    print("All test cases passed!")
