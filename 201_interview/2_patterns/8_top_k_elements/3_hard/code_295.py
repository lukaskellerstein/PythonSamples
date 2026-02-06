


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

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???) for addNum, O(???) for findMedian
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

class MedianFinderBruteForce:

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???) for addNum, O(???) for findMedian
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

class MedianFinder:

    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    # Test case 1: Basic usage
    test_operations = [
        {"op": "addNum", "val": 1, "expected": None},
        {"op": "addNum", "val": 2, "expected": None},
        {"op": "findMedian", "val": None, "expected": 1.5},
        {"op": "addNum", "val": 3, "expected": None},
        {"op": "findMedian", "val": None, "expected": 2.0},
    ]

    mf_bf = MedianFinderBruteForce()
    mf = MedianFinder()

    for test in test_operations:
        op = test["op"]
        val = test["val"]
        expected = test["expected"]

        if op == "addNum":
            mf_bf.addNum(val)
            mf.addNum(val)
            print(f"addNum({val}) ✓")
        elif op == "findMedian":
            result1 = mf_bf.findMedian()
            result2 = mf.findMedian()
            assert result1 == expected, f"Brute force failed: findMedian() got {result1}, expected {expected}"
            assert result2 == expected, f"Optimal failed: findMedian() got {result2}, expected {expected}"
            print(f"findMedian(), expected={expected}, brute_force={result1}, optimal={result2} ✓")

    # Test case 2: Larger stream
    mf2_bf = MedianFinderBruteForce()
    mf2 = MedianFinder()
    for num in [6, 10, 2, 6, 5, 0, 6, 3, 1, 0, 0]:
        mf2_bf.addNum(num)
        mf2.addNum(num)
    result1 = mf2_bf.findMedian()
    result2 = mf2.findMedian()
    assert result1 == 3.0, f"Brute force failed: got {result1}, expected 3.0"
    assert result2 == 3.0, f"Optimal failed: got {result2}, expected 3.0"
    print(f"Larger stream: expected=3.0, brute_force={result1}, optimal={result2} ✓")

    # Test case 3: Single element
    mf3_bf = MedianFinderBruteForce()
    mf3 = MedianFinder()
    mf3_bf.addNum(5)
    mf3.addNum(5)
    assert mf3_bf.findMedian() == 5.0
    assert mf3.findMedian() == 5.0
    print(f"Single element: expected=5.0 ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
