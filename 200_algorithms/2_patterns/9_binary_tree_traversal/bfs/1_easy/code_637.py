
# -----------------------
# Average of Levels in Binary Tree (LeetCode 637)
# -----------------------

# Difficulty: Easy

# Problem: Given the root of a binary tree, return the average value of the
# nodes on each level in the form of an array. Answers within 10^-5 of the
# actual answer will be accepted.

# -----------------------
# VISUALIZATION
# -----------------------
#
#       3
#      / \
#     9   20
#        /  \
#       15   7
#
# Level 0: [3]       -> avg = 3.0
# Level 1: [9, 20]   -> avg = 14.5
# Level 2: [15, 7]   -> avg = 11.0
#
# Output: [3.0, 14.5, 11.0]
#
# -----------------------

from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build test tree:       3
#                       / \
#                      9   20
#                         /  \
#                        15   7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


# ----------------------------------------------------
# BFS Level-Order solution (Optimal)
#
# time complexity = O(n) - visit every node once
# space complexity = O(w) - w = max width of tree (queue size)
# ----------------------------------------------------

def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level_sum = 0

        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level_sum / level_size)

    return result


# Example
print(average_of_levels(root))  # [3.0, 14.5, 11.0]


# ----------------------------------------------------
# Brute Force solution (DFS + level tracking)
#
# time complexity = O(n) - visit every node once
# space complexity = O(n) - storing sums and counts for each level
# ----------------------------------------------------

def average_of_levels_brute_force(root: Optional[TreeNode]) -> List[float]:
    if not root:
        return []

    level_sums = {}   # level -> sum of values
    level_counts = {} # level -> count of nodes

    def dfs(node, level):
        if not node:
            return

        level_sums[level] = level_sums.get(level, 0) + node.val
        level_counts[level] = level_counts.get(level, 0) + 1

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)

    result = []
    for level in range(len(level_sums)):
        result.append(level_sums[level] / level_counts[level])

    return result


# Example
print(average_of_levels_brute_force(root))  # [3.0, 14.5, 11.0]


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    # Test case 2: single node
    root2 = TreeNode(1)

    # Test case 3: all left
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)

    test_cases = [
        (root, [3.0, 14.5, 11.0]),
        (root2, [1.0]),
        (root3, [1.0, 2.0, 3.0]),
    ]

    print("\nAverage of Levels Results:")
    print("-" * 50)
    for tree_root, expected in test_cases:
        result1 = average_of_levels(tree_root)
        result2 = average_of_levels_brute_force(tree_root)
        print(f"BFS:   {result1}")
        print(f"DFS:   {result2}")
        print(f"Match: {result1 == result2}")
        print("-" * 50)
