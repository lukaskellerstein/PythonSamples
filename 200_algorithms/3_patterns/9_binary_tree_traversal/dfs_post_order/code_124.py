
# -----------------------
# Binary Tree Maximum Path Sum (LeetCode 124)
# -----------------------

# Difficulty: Hard

# Problem: A path in a binary tree is a sequence of nodes where each pair of
# adjacent nodes in the sequence has an edge connecting them. A node can only
# appear in the sequence at most once. Note that the path does not need to
# pass through the root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the root of a binary tree, return the maximum path sum of any non-empty path.

# -----------------------

# Example:
#       1
#      / \
#     2   3
# Output: 6 (path: 2 -> 1 -> 3)
#
#      -10
#      /  \
#     9   20
#        /  \
#       15   7
# Output: 42 (path: 15 -> 20 -> 7)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Example 1: Simple tree
#       1
#      / \
#     2   3
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)


# Example 2: Tree with negative root
#      -10
#      /  \
#     9   20
#        /  \
#       15   7
root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)

# Example 3: All negative values
root3 = TreeNode(-3)


# ----------------------------------------------------
# Iterative Postorder with Stack (STACK)
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - stack and hash map storage
#
# Idea: Use iterative postorder traversal with a hash map to store
# the maximum gain from each subtree.
# ----------------------------------------------------


def max_path_sum_iterative(root):
    if not root:
        return 0

    max_sum = float('-inf')
    # Store max gain extendable to parent for each node
    gains = {None: 0}

    stack = [(root, False)]

    while stack:
        node, processed = stack.pop()

        if processed:
            # Postorder: process after children
            left_gain = max(gains.get(node.left, 0), 0)
            right_gain = max(gains.get(node.right, 0), 0)

            # Path through current node
            current_path_sum = node.val + left_gain + right_gain
            max_sum = max(max_sum, current_path_sum)

            # Store gain for parent
            gains[node] = node.val + max(left_gain, right_gain)
        else:
            # Push node back to process after children
            stack.append((node, True))
            if node.right:
                stack.append((node.right, False))
            if node.left:
                stack.append((node.left, False))

    return max_sum


# Example
print(max_path_sum_iterative(root1))  # 6
print(max_path_sum_iterative(root2))  # 42
print(max_path_sum_iterative(root3))  # -3



# ----------------------------------------------------
# Postorder DFS solution (RECURSION)
#
# time complexity = O(n) - visit each node once
# space complexity = O(h) - recursion stack, h = height of tree
#
# Idea: For each node, calculate the maximum path sum that can be extended
# to its parent. Update global max considering paths through this node.
# Postorder because we need child results before processing current node.
# ----------------------------------------------------


def max_path_sum(root):
    max_sum = float('-inf')

    def dfs(node):
        nonlocal max_sum

        if not node:
            return 0

        # Get max path sum from left and right subtrees
        # Use max with 0 to ignore negative paths
        left_gain = max(dfs(node.left), 0)
        right_gain = max(dfs(node.right), 0)

        # Path through current node (could be the maximum path)
        current_path_sum = node.val + left_gain + right_gain

        # Update global maximum
        max_sum = max(max_sum, current_path_sum)

        # Return max gain if we extend path to parent
        # Can only choose one direction (left or right) to extend upward
        return node.val + max(left_gain, right_gain)

    dfs(root)
    return max_sum


print(max_path_sum(root1))  # 6
print(max_path_sum(root2))  # 42
print(max_path_sum(root3))  # -3


