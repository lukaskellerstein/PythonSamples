from typing import Optional
import math


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Validate Binary Search Tree (LeetCode 98)
# ============================================================
# Difficulty: Medium
# Pattern: DFS In-Order Traversal
#
# Given the root of a binary tree, determine if it is a valid binary
# search tree (BST). A valid BST is defined as follows: the left
# subtree of a node contains only nodes with keys strictly less than
# the node's key, the right subtree contains only nodes with keys
# strictly greater than the node's key, and both the left and right
# subtrees must also be valid BSTs.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [2,1,3]
#   Output: True
#   Explanation: Left child 1 < 2 and right child 3 > 2.
#
# Example 2:
#   Input: root = [5,1,4,null,null,3,6]
#   Output: False
#   Explanation: Node 4 is in the right subtree of 5 but has
#                left child 3 which is less than 5.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the tree is in the range [1, 10^4]
# - -2^31 <= Node.val <= 2^31 - 1
#
# ============================================================
# VISUALIZATION
# ============================================================
#
#       2          Valid BST
#      / \         1 < 2 < 3
#     1   3
#
#       5          Invalid BST
#      / \
#     1   4        4 < 5 (wrong for right subtree)
#        / \
#       3   6      3 < 5 (violates: right subtree must have all > 5)
#
# Key insight: It's not enough to check parent-child relationship.
# Every node in the right subtree must be greater than the root.
#
# In-order traversal of a valid BST is strictly increasing:
#   Valid:   1 -> 2 -> 3 (increasing)
#   Invalid: 1 -> 5 -> 3 -> 4 -> 6 (3 < 5, not increasing)
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Min/Max Range Checking)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def is_valid_bst_brute_force(root: Optional[TreeNode]) -> bool:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (In-Order Traversal)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1: invalid BST
    root1 = TreeNode(5)
    root1.left = TreeNode(1)
    root1.right = TreeNode(4)
    root1.right.left = TreeNode(3)
    root1.right.right = TreeNode(6)
    # Expected: False

    # Test case 2: valid BST
    root2 = TreeNode(2)
    root2.left = TreeNode(1)
    root2.right = TreeNode(3)
    # Expected: True

    # Test case 3: single node
    root3 = TreeNode(1)
    # Expected: True

    # Test case 4: equal values (invalid)
    root4 = TreeNode(1)
    root4.left = TreeNode(1)
    # Expected: False

    pass
