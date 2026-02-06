
# -----------------------
# Vertical Order Traversal of a Binary Tree (LeetCode 987)
# -----------------------

# Difficulty: Hard

# Problem: Given the root of a binary tree, calculate the vertical order
# traversal of the binary tree.
#
# For each node at position (row, col):
# - Its left child is at (row + 1, col - 1)
# - Its right child is at (row + 1, col + 1)
#
# The vertical order traversal starts from the leftmost column and ends at
# the rightmost column. For nodes in the same (row, col), sort by value.

# -----------------------

# Example:
#         3
#        / \
#       9  20
#          / \
#        15   7
#
# Output: [[9], [3, 15], [20], [7]]
#
# Example with same position nodes:
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
#
# Nodes 5 and 6 are at same (row=2, col=0) -> sort by value: [5, 6]
# Output: [[4], [2], [1, 5, 6], [3], [7]]

from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build example tree 1
#         3
#        / \
#       9  20
#          / \
#        15   7
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)


# Example 2: nodes at same position
#         1
#        / \
#       2   3
#      / \ / \
#     4  5 6  7
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(5)
root2.right.left = TreeNode(6)
root2.right.right = TreeNode(7)


# Example 3: same position, different values
#         1
#        / \
#       2   3
#      / \
#     4   6
#        /
#       5
root3 = TreeNode(1)
root3.left = TreeNode(2)
root3.right = TreeNode(3)
root3.left.left = TreeNode(4)
root3.left.right = TreeNode(6)
root3.left.right.left = TreeNode(5)

# ----------------------------------------------------
# BFS with Full Sorting solution (Optimal)
#
# time complexity = O(n log n) - sorting nodes within columns
# space complexity = O(n) - storing all nodes
#
# Idea: Track (row, value) for each column. Sort within each column by
# row first, then by value for same row. This handles the tie-breaking rule.
# ----------------------------------------------------


def vertical_traversal(root):
    if not root:
        return []

    # Map column -> list of (row, value)
    column_map = defaultdict(list)
    min_col = max_col = 0

    # BFS: queue contains (node, row, col)
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()

        column_map[col].append((row, node.val))
        min_col = min(min_col, col)
        max_col = max(max_col, col)

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    # Build result: sort each column by (row, value)
    result = []
    for col in range(min_col, max_col + 1):
        # Sort by row, then by value
        column_map[col].sort()
        result.append([val for row, val in column_map[col]])

    return result


print(vertical_traversal(root1))  # [[9], [3, 15], [20], [7]]
print(vertical_traversal(root2))  # [[4], [2], [1, 5, 6], [3], [7]]
print(vertical_traversal(root3))  # [[4], [2, 5], [1, 6], [3]]


# ----------------------------------------------------
# DFS with Sorting solution (Alternative)
#
# time complexity = O(n log n) - sorting all nodes
# space complexity = O(n) - storing all nodes
#
# Idea: Collect all nodes with (col, row, value), sort everything,
# then group by column.
# ----------------------------------------------------


def vertical_traversal_dfs(root):
    if not root:
        return []

    # Store (col, row, value) for each node
    nodes = []

    def dfs(node, row, col):
        if not node:
            return

        nodes.append((col, row, node.val))
        dfs(node.left, row + 1, col - 1)
        dfs(node.right, row + 1, col + 1)

    dfs(root, 0, 0)

    # Sort by column, then row, then value
    nodes.sort()

    # Group by column
    result = []
    current_col = None
    for col, row, val in nodes:
        if col != current_col:
            result.append([])
            current_col = col
        result[-1].append(val)

    return result


print(vertical_traversal_dfs(root1))  # [[9], [3, 15], [20], [7]]
print(vertical_traversal_dfs(root2))  # [[4], [2], [1, 5, 6], [3], [7]]
print(vertical_traversal_dfs(root3))  # [[4], [2, 5], [1, 6], [3]]

