
# ---------------------------
# Google Favorite
# ---------------------------

# -----------------------
# Trapping Rain Water (LeetCode 42)
# -----------------------

# Dificulty: Hard

# Problem: Given an array of non-negative integers representing an elevation map
# where each bar has width 1, compute how much water it can trap after raining.

# -----------------------
# VISUALIZATION
# -----------------------
#
# Input:  [0,1,0,2,1,0,1,3,2,1,2,1]
#          0 1 2 3 4 5 6 7 8 9 ...  <- index
#
# Legend: █ = ground (elevation)
#         ~ = trapped water
#
#     3 |               █
#     2 |       █ ~ ~ ~ █ █ ~ █
#     1 |   █ ~ █ █ ~ █ █ █ █ █ █
#       +-------------------------
#         0 1 2 3 4 5 6 7 8 9 10 11  <- index
#         0 1 0 2 1 0 1 3 2 1 2  1   <- height
#         0 0 1 0 1 2 1 0 0 1 0  0   <- water at each position
#                                    -----
#                          Total:    6
#
# Water is trapped at:
#   - index 2: between bars at 1 and 3, holds 1 unit
#   - index 4: between bars at 3 and 7, holds 1 unit
#   - index 5: between bars at 3 and 7, holds 2 units
#   - index 6: between bars at 3 and 7, holds 1 unit
#   - index 9: between bars at 8 and 10, holds 1 unit
#
# -----------------------

# For given elevation map, compute trapped water
heightArr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

# ----------------------------------------------------
# Two Pointers solution
#
# time complexity = O(n) - single pass through the array
# space complexity = O(1) - only using pointers and variables
# ----------------------------------------------------


def water_trap(heightArr):
    if not heightArr:
        return 0

    left_index = 0
    right_index = len(heightArr) - 1

    left_max_height = heightArr[left_index]
    right_max_height = heightArr[right_index]

    water = 0

    while left_index < right_index:
        if left_max_height < right_max_height:
            left_index += 1
            left_max_height = max(left_max_height, heightArr[left_index])
            water += left_max_height - heightArr[left_index]
        else:
            right_index -= 1
            right_max_height = max(right_max_height, heightArr[right_index])
            water += right_max_height - heightArr[right_index]
        
    return water


# Example
print(water_trap(heightArr))  # 6


# ----------------------------------------------------
# Brute Force solution
#
# time complexity = O(n²) - for each element, scan left and right
# space complexity = O(1) - only using variables
# ----------------------------------------------------

def trap_brute_force(height):
    if not height:
        return 0

    n = len(height)
    water = 0

    # For each element, find the water it can trap
    for i in range(n):
        # Find maximum height to the left
        left_max = 0
        for j in range(i + 1):
            left_max = max(left_max, height[j])

        # Find maximum height to the right
        right_max = 0
        for j in range(i, n):
            right_max = max(right_max, height[j])

        # Water at current position = min(left_max, right_max) - height[i]
        water += min(left_max, right_max) - height[i]

    return water


# Example
print(trap_brute_force(heightArr))  # 6
