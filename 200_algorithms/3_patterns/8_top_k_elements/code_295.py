
# -----------------------
# Find Median from Data Stream (LeetCode 295)
# -----------------------

# Difficulty: Hard

# Problem: The median is the middle value in an ordered integer list. If the size
# of the list is even, the median is the average of the two middle values.
#
# Implement the MedianFinder class:
# - MedianFinder() initializes the MedianFinder object.
# - void addNum(int num) adds the integer num to the data structure.
# - double findMedian() returns the median of all elements so far.

# -----------------------

# Example:
# addNum(1), addNum(2), findMedian() -> 1.5
# addNum(3), findMedian() -> 2.0

# ----------------------------------------------------
# Two Heaps solution (Optimal)
#
# time complexity = O(log n) for addNum, O(1) for findMedian
# space complexity = O(n) - storing all elements in heaps
#
# Idea: Use a max-heap for the lower half and min-heap for the upper half.
# The median is either the top of max-heap or average of both tops.
# ----------------------------------------------------

import heapq


class MedianFinder:
    def __init__(self):
        # Max heap for lower half (store negatives since Python has min-heap)
        self.lower = []  # max-heap (inverted)
        # Min heap for upper half
        self.upper = []  # min-heap

    def addNum(self, num: int) -> None:
        # Always add to lower (max-heap) first
        heapq.heappush(self.lower, -num)

        # Balance: largest of lower should be <= smallest of upper
        if self.lower and self.upper and (-self.lower[0] > self.upper[0]):
            val = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)

        # Maintain size property: lower can have at most 1 more element than upper
        if len(self.lower) > len(self.upper) + 1:
            val = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, val)

        if len(self.upper) > len(self.lower):
            val = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -val)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        return (-self.lower[0] + self.upper[0]) / 2.0


# Example
mf = MedianFinder()
mf.addNum(1)
mf.addNum(2)
print(mf.findMedian())  # 1.5
mf.addNum(3)
print(mf.findMedian())  # 2.0

# More comprehensive test
mf2 = MedianFinder()
for num in [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0]:
    mf2.addNum(num)
print(mf2.findMedian())  # 3.0 (sorted: [0,0,0,1,2,3,5,6,6,6,10])


# ----------------------------------------------------
# Brute Force solution (Sorted List)
#
# time complexity = O(n) for addNum (insertion), O(1) for findMedian
# space complexity = O(n) - storing all elements
# ----------------------------------------------------


class MedianFinderBruteForce:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        # Insert in sorted order using binary search for position
        # But insertion itself is O(n) due to shifting
        left, right = 0, len(self.nums)
        while left < right:
            mid = (left + right) // 2
            if self.nums[mid] < num:
                left = mid + 1
            else:
                right = mid
        self.nums.insert(left, num)

    def findMedian(self) -> float:
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0


# Example
mf_bf = MedianFinderBruteForce()
mf_bf.addNum(1)
mf_bf.addNum(2)
print(mf_bf.findMedian())  # 1.5
mf_bf.addNum(3)
print(mf_bf.findMedian())  # 2.0


# ----------------------------------------------------
# Naive Brute Force solution (Sort on every findMedian)
#
# time complexity = O(1) for addNum, O(n log n) for findMedian
# space complexity = O(n) - storing all elements
# ----------------------------------------------------


class MedianFinderNaive:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        if n % 2 == 1:
            return self.nums[n // 2]
        return (self.nums[n // 2 - 1] + self.nums[n // 2]) / 2.0


# Example
mf_naive = MedianFinderNaive()
mf_naive.addNum(1)
mf_naive.addNum(2)
print(mf_naive.findMedian())  # 1.5
mf_naive.addNum(3)
print(mf_naive.findMedian())  # 2.0
