
# -----------------------
# Diagonal Traversal of Binary Tree
# -----------------------

# Difficulty: Medium

# Problem: Given a binary tree, return the diagonal traversal of the tree.
# A diagonal contains all nodes that have the same (col - row) value,
# traversed from top-right to bottom-left.
#
# Alternative definition: Going right keeps you on the same diagonal,
# going left moves you to the next diagonal.

# -----------------------

# Example:
#         8
#        / \
#       3   10
#      / \    \
#     1   6   14
#        / \  /
#       4  7 13
#
# Diagonal 0: 8 -> 10 -> 14
# Diagonal 1: 3 -> 6 -> 7 -> 13
# Diagonal 2: 1 -> 4
#
# Output: [[8, 10, 14], [3, 6, 7, 13], [1, 4]]

from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build example tree
#         8
#        / \
#       3   10
#      / \    \
#     1   6   14
#        / \  /
#       4  7 13
root1 = TreeNode(8)
root1.left = TreeNode(3)
root1.right = TreeNode(10)
root1.left.left = TreeNode(1)
root1.left.right = TreeNode(6)
root1.right.right = TreeNode(14)
root1.left.right.left = TreeNode(4)
root1.left.right.right = TreeNode(7)
root1.right.right.left = TreeNode(13)



# Example 2: Simple tree
#         1
#        / \
#       2   3
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)


# ----------------------------------------------------
# BFS with Diagonal Index solution (Optimal)
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - queue and diagonal map storage
#
# Idea: Use BFS to traverse. Track diagonal index for each node.
# Right child: same diagonal. Left child: diagonal + 1.
# BFS ensures top-to-bottom, left-to-right order within diagonals.
# ----------------------------------------------------


def diagonal_traversal(root):
    if not root:
        return []

    # Map diagonal index to list of values
    diagonal_map = defaultdict(list)
    max_diagonal = 0

    # BFS: queue contains (node, diagonal)
    queue = deque([(root, 0)])

    while queue:
        node, diag = queue.popleft()

        diagonal_map[diag].append(node.val)
        max_diagonal = max(max_diagonal, diag)

        # Right child stays on same diagonal
        if node.right:
            queue.append((node.right, diag))

        # Left child moves to next diagonal
        if node.left:
            queue.append((node.left, diag + 1))

    # Build result from diagonal 0 to max
    return [diagonal_map[d] for d in range(max_diagonal + 1)]



print(diagonal_traversal(root1))  # [[8, 10, 14], [3, 6, 7, 13], [1, 4]]
print(diagonal_traversal(root2))  # [[1, 3], [2]]


# ----------------------------------------------------
# Alternative: Using (row - col) as diagonal identifier
#
# time complexity = O(n log n) - sorting diagonals
# space complexity = O(n) - storing all nodes
#
# Idea: Diagonal can be identified by (row - col) value.
# Nodes with same (row - col) are on same diagonal.
# ----------------------------------------------------


def diagonal_traversal_row_col(root):
    if not root:
        return []

    # Map (row - col) to list of (row, value)
    diagonal_map = defaultdict(list)

    # BFS: queue contains (node, row, col)
    queue = deque([(root, 0, 0)])

    while queue:
        node, row, col = queue.popleft()

        diag = row - col  # Diagonal identifier
        diagonal_map[diag].append((row, node.val))

        if node.left:
            queue.append((node.left, row + 1, col - 1))
        if node.right:
            queue.append((node.right, row + 1, col + 1))

    # Sort diagonals by their identifier, then sort nodes by row within diagonal
    result = []
    for diag in sorted(diagonal_map.keys()):
        # Sort by row to ensure top-to-bottom order
        diagonal_map[diag].sort()
        result.append([val for row, val in diagonal_map[diag]])

    return result


print(diagonal_traversal_row_col(root1))  # [[8, 10, 14], [3, 6, 7, 13], [1, 4]]
print(diagonal_traversal_row_col(root2))  # [[1, 3], [2]]


# ----------------------------------------------------
# DFS solution (Brute Force)
#
# time complexity = O(n log n) - need to sort for correct order
# space complexity = O(n) - storing all nodes
#
# Idea: DFS to collect all nodes with their diagonal index.
# Need extra sorting to maintain order within diagonals.
# ----------------------------------------------------


def diagonal_traversal_dfs(root):
    if not root:
        return []

    # Store (diagonal, row, col, value) for ordering
    nodes = []

    def dfs(node, row, col, diag):
        if not node:
            return

        nodes.append((diag, row, col, node.val))

        # Right child: same diagonal
        dfs(node.right, row + 1, col + 1, diag)
        # Left child: next diagonal
        dfs(node.left, row + 1, col - 1, diag + 1)

    dfs(root, 0, 0, 0)

    # Sort by diagonal, then by row (top to bottom), then by col (right to left for ties)
    nodes.sort(key=lambda x: (x[0], x[1], -x[2]))

    # Group by diagonal
    result = []
    current_diag = -1
    for diag, row, col, val in nodes:
        if diag != current_diag:
            result.append([])
            current_diag = diag
        result[-1].append(val)

    return result


print(diagonal_traversal_dfs(root1))  # [[8, 10, 14], [3, 6, 7, 13], [1, 4]]
print(diagonal_traversal_dfs(root2))  # [[1, 3], [2]]

