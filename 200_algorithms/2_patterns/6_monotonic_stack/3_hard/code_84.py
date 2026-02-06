
# -----------------------
# Largest Rectangle in Histogram (LeetCode 84)
# -----------------------

# Difficulty: Hard
# Sub-pattern: Monotonic Increasing Stack

# Problem: Given an array of integers heights representing the histogram's
# bar height where the width of each bar is 1, return the area of the
# largest rectangle in the histogram.

# -----------------------

# For heights [2,1,5,6,2,3] → 10
# The largest rectangle is formed by bars at index 2 and 3 (heights 5,6)
# with width 2 → area = 5 * 2 = 10.
heights = [2, 1, 5, 6, 2, 3]

# ----------------------------------------------------
# Monotonic Increasing Stack solution
#
# Maintain an increasing stack of indices. When we encounter a bar shorter
# than the top, we pop and calculate the area using the popped bar as the
# height. The width extends from the new stack top+1 to current index-1.
#
# time complexity = O(n) - each bar pushed and popped at most once
# space complexity = O(n) - stack
# ----------------------------------------------------


def largest_rectangle_area(heights):
    stack = []  # stores indices, heights at these indices are increasing
    max_area = 0
    n = len(heights)

    for i in range(n + 1):
        # Use height 0 as a sentinel to flush remaining bars at the end
        curr_height = heights[i] if i < n else 0

        while stack and curr_height < heights[stack[-1]]:
            height = heights[stack.pop()]
            # Width: if stack is empty, bar extends from index 0 to i-1
            # otherwise from stack[-1]+1 to i-1
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area


# Example
print(largest_rectangle_area(heights))  # 10


# ----------------------------------------------------
# Explicit Left/Right Boundaries solution
#
# For each bar, find the nearest smaller bar on the left (PLE) and
# on the right (NLE) using two monotonic stack passes.
#
# time complexity = O(n) - two passes
# space complexity = O(n) - left/right boundary arrays + stack
# ----------------------------------------------------


def largest_rectangle_area_two_pass(heights):
    n = len(heights)
    left = [0] * n  # index of previous less element (-1 if none)
    right = [0] * n  # index of next less element (n if none)

    # Find previous less element for each bar
    stack = []
    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    # Find next less element for each bar
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    # For each bar, area = height * (right[i] - left[i] - 1)
    max_area = 0
    for i in range(n):
        area = heights[i] * (right[i] - left[i] - 1)
        max_area = max(max_area, area)

    return max_area


# Example
print(largest_rectangle_area_two_pass(heights))  # 10


# ----------------------------------------------------
# Brute Force solution
#
# For every pair (i, j), find the min height and compute area.
#
# time complexity = O(n^2) - check every pair of bars
# space complexity = O(1)
# ----------------------------------------------------


def largest_rectangle_area_brute(heights):
    max_area = 0
    n = len(heights)

    for i in range(n):
        min_height = heights[i]
        for j in range(i, n):
            min_height = min(min_height, heights[j])
            area = min_height * (j - i + 1)
            max_area = max(max_area, area)

    return max_area


# Example
print(largest_rectangle_area_brute(heights))  # 10
