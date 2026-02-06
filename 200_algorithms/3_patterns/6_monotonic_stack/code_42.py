
# -----------------------
# Trapping Rain Water (LeetCode 42)
# -----------------------

# Difficulty: Hard
# Sub-pattern: Monotonic Decreasing Stack / Two Pointers

# Problem: Given n non-negative integers representing an elevation map where
# the width of each bar is 1, compute how much water it can trap after raining.

# -----------------------

# For height [0,1,0,2,1,0,1,3,2,1,2,1] → 6 units of trapped water.
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# ----------------------------------------------------
# Monotonic Stack solution (horizontal layer-by-layer)
#
# Maintain a decreasing stack. When current bar is taller than the top,
# we found a "valley" — pop the bottom of the valley and compute the
# water trapped in this horizontal layer between the new top and current.
#
# time complexity = O(n) - each bar pushed and popped at most once
# space complexity = O(n) - stack
# ----------------------------------------------------


def trap_stack(height):
    stack = []  # stores indices, heights are in decreasing order
    water = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            bottom = stack.pop()
            if not stack:
                break
            # Width between left wall (stack[-1]) and right wall (i)
            width = i - stack[-1] - 1
            # Height is bounded by the shorter wall minus the bottom
            bounded_height = min(height[stack[-1]], height[i]) - height[bottom]
            water += width * bounded_height
        stack.append(i)

    return water


# Example
print(trap_stack(height))  # 6


# ----------------------------------------------------
# Two Pointers solution
#
# Maintain left and right pointers with their respective max heights.
# Water at each position = min(left_max, right_max) - height[i].
#
# time complexity = O(n) - single pass with two pointers
# space complexity = O(1) - only pointer variables
# ----------------------------------------------------


def trap_two_pointers(height):
    left, right = 0, len(height) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1

    return water


# Example
print(trap_two_pointers(height))  # 6


# ----------------------------------------------------
# DP (Precomputed Max) solution
#
# For each bar, precompute the max height to its left and right.
# Water at position i = min(left_max[i], right_max[i]) - height[i].
#
# time complexity = O(n) - three passes
# space complexity = O(n) - two extra arrays
# ----------------------------------------------------


def trap_dp(height):
    n = len(height)
    if n < 3:
        return 0

    left_max = [0] * n
    right_max = [0] * n

    left_max[0] = height[0]
    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])

    right_max[n - 1] = height[n - 1]
    for i in range(n - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], height[i])

    water = 0
    for i in range(n):
        water += min(left_max[i], right_max[i]) - height[i]

    return water


# Example
print(trap_dp(height))  # 6


# ----------------------------------------------------
# Brute Force solution
#
# For each bar, scan left and right to find the max heights.
#
# time complexity = O(n^2) - for each bar scan both directions
# space complexity = O(1)
# ----------------------------------------------------


def trap_brute(height):
    n = len(height)
    water = 0

    for i in range(n):
        left_max = max(height[: i + 1])
        right_max = max(height[i:])
        water += min(left_max, right_max) - height[i]

    return water


# Example
print(trap_brute(height))  # 6
