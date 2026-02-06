
# -----------------------
# Validate Binary Search Tree (LeetCode 98)
# -----------------------

# Difficulty: Medium

# Problem: Given the root of a binary tree, determine if it is a valid binary
# search tree (BST). A valid BST is defined as: the left subtree of a node
# contains only nodes with keys less than the node's key, the right subtree
# contains only nodes with keys greater than the node's key, and both subtrees
# must also be valid BSTs.

# -----------------------

# For given tree:
#       5
#      / \
#     1   4
#        / \
#       3   6
# return False (4 has left child 3, but 3 < 5 violates BST for right subtree)
#
# For given tree:
#       2
#      / \
#     1   3
# return True

import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build example trees
root1 = TreeNode(5)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.right.left = TreeNode(3)
root1.right.right = TreeNode(6)

root2 = TreeNode(2)
root2.left = TreeNode(1)
root2.right = TreeNode(3)



# ----------------------------------------------------
# Iterative Inorder Traversal (with STACK)
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - explicit stack up to tree height
# ----------------------------------------------------


def is_valid_bst_iterative(root):
    stack = []
    prev = -math.inf
    current = root

    while stack or current:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left

        # Process the node
        current = stack.pop()

        # Inorder value must be strictly increasing
        if current.val <= prev:
            return False
        prev = current.val

        # Move to right subtree
        current = current.right

    return True


# Example
print(is_valid_bst_iterative(root1))  # False
print(is_valid_bst_iterative(root2))  # True


# ----------------------------------------------------
# DFS Inorder Traversal (with RECURSION)
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - recursion stack up to tree height
# ----------------------------------------------------


def is_valid_bst(root):
    # Inorder traversal of a valid BST is strictly increasing
    prev = -math.inf

    def inorder(node):
        nonlocal prev

        if not node:
            return True

        # Check left subtree
        if not inorder(node.left):
            return False

        # Current node must be greater than previous
        if node.val <= prev:
            return False
        prev = node.val

        # Check right subtree
        return inorder(node.right)

    return inorder(root)


# Example
print(is_valid_bst(root1))  # False
print(is_valid_bst(root2))  # True


# ----------------------------------------------------
# Brute Force (Min/Max range checking) solution
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - recursion stack up to tree height
# ----------------------------------------------------


def is_valid_bst_brute_force(root):
    def validate(node, low, high):
        if not node:
            return True

        # Current node must be within the valid range
        if node.val <= low or node.val >= high:
            return False

        # Left child must be less than current, right must be greater
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, -math.inf, math.inf)


# Example
print(is_valid_bst_brute_force(root1))  # False
print(is_valid_bst_brute_force(root2))  # True

