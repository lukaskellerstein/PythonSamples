
# -----------------------
# Binary Tree Vertical Order Traversal (LeetCode 314)
# -----------------------

# Difficulty: Medium

# Problem: Given the root of a binary tree, return the vertical order traversal
# of its nodes' values. (i.e., from top to bottom, column by column).
#
# If two nodes are in the same row and column, the order should be from left
# to right.

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
# Column indices:
#         3 (col=0)
#        / \
#   (col=-1)9  20 (col=1)
#             / \
#       (col=0)15  7 (col=2)

from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Build example tree
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

# Example 2:
#         3
#        / \
#       9  8
#      / \  / \
#     4  0 1   7
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(8)
root2.left.left = TreeNode(4)
root2.left.right = TreeNode(0)
root2.right.left = TreeNode(1)
root2.right.right = TreeNode(7)


# ----------------------------------------------------
# BFS with Column Index solution (Optimal)
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - queue and column map storage
#
# Idea: Use BFS to traverse level by level. Track column index for each node.
# Left child: col - 1, Right child: col + 1. Group nodes by column.
# BFS naturally handles top-to-bottom, left-to-right ordering.
# ----------------------------------------------------


def vertical_order(root):
    if not root:
        return []

    # Map column index to list of values
    column_map = defaultdict(list)
    min_col = max_col = 0

    # BFS: queue contains (node, column)
    queue = deque([(root, 0)])

    while queue:
        node, col = queue.popleft()

        column_map[col].append(node.val)
        min_col = min(min_col, col)
        max_col = max(max_col, col)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    # Build result from leftmost to rightmost column
    return [column_map[col] for col in range(min_col, max_col + 1)]

print(vertical_order(root1))  # [[9], [3, 15], [20], [7]]
print(vertical_order(root2))  # [[4], [9], [3, 0, 1], [8], [7]]


# ----------------------------------------------------
# BFS with Sorting solution (Alternative)
#
# time complexity = O(n log n) - sorting the columns
# space complexity = O(n) - storing all nodes
#
# Idea: Same as above but use sorting instead of tracking min/max columns.
# ----------------------------------------------------


def vertical_order_sorting(root):
    if not root:
        return []

    column_map = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, col = queue.popleft()
        column_map[col].append(node.val)

        if node.left:
            queue.append((node.left, col - 1))
        if node.right:
            queue.append((node.right, col + 1))

    # Sort by column index
    return [column_map[col] for col in sorted(column_map.keys())]


print(vertical_order_sorting(root1))  # [[9], [3, 15], [20], [7]]
print(vertical_order_sorting(root2))  # [[4], [9], [3, 0, 1], [8], [7]]

