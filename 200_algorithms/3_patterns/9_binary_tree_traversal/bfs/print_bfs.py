
# -----------------------
# Binary Tree Level Order Traversal (LeetCode 102)
# -----------------------

# Difficulty: Medium

# Problem: Given the root of a binary tree, return the level order traversal
# of its nodes' values (i.e., from left to right, level by level).

# -----------------------

# For given tree:
#       3
#      / \
#     9  20
#        / \
#       15   7
# return [[3], [9, 20], [15, 7]]

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build example tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# ----------------------------------------------------
# BFS with Queue solution
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - queue holds at most one level of nodes
# ----------------------------------------------------


def level_order(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result


# Example
print(level_order(root))  # [[3], [9, 20], [15, 7]]


# ----------------------------------------------------
# Brute Force (DFS with depth tracking) solution
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - recursion stack up to tree height + result list
# ----------------------------------------------------


def level_order_brute_force(root):
    if not root:
        return []

    result = []

    def dfs(node, depth):
        if not node:
            return

        # Extend result list if we reach a new level
        if depth == len(result):
            result.append([])

        result[depth].append(node.val)

        dfs(node.left, depth + 1)
        dfs(node.right, depth + 1)

    dfs(root, 0)
    return result


# Example
print(level_order_brute_force(root))  # [[3], [9, 20], [15, 7]]
