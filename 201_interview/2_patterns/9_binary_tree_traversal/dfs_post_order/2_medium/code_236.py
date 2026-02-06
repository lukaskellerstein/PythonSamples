from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Lowest Common Ancestor of a Binary Tree (LeetCode 236)
# ============================================================
# Difficulty: Medium
# Pattern: DFS Post-Order Traversal
#
# Given a binary tree, find the lowest common ancestor (LCA) of two
# given nodes p and q. The lowest common ancestor is defined as the
# lowest node in the tree that has both p and q as descendants (where
# we allow a node to be a descendant of itself).
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
#   Output: 3
#   Explanation: The LCA of nodes 5 and 1 is 3 (the root).
#
# Example 2:
#   Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
#   Output: 5
#   Explanation: The LCA of nodes 5 and 4 is 5, since a node can
#                be a descendant of itself.
#
# Example 3:
#   Input: root = [1,2], p = 1, q = 2
#   Output: 1
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the tree is in the range [2, 10^5]
# - -10^9 <= Node.val <= 10^9
# - All Node.val are unique
# - p != q
# - p and q will exist in the tree
#
# ============================================================
# VISUALIZATION
# ============================================================
#
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
#
# LCA(5, 1) = 3  (5 is in left subtree, 1 is in right subtree)
# LCA(5, 4) = 5  (4 is descendant of 5, so 5 is the LCA)
# LCA(6, 4) = 5  (both 6 and 4 are in the left subtree under 5)
#
# Post-order approach: process children first, then decide at parent.
# If left subtree returns p/q and right subtree returns p/q,
# then current node is the LCA.
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Path Finding)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def lowest_common_ancestor_brute_force(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Post-Order DFS)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def lowest_common_ancestor(
    root: Optional[TreeNode], p: TreeNode, q: TreeNode
) -> Optional[TreeNode]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Build test tree
    #         3
    #        / \
    #       5   1
    #      / \ / \
    #     6  2 0  8
    #       / \
    #      7   4
    root = TreeNode(3)
    root.left = TreeNode(5)
    root.right = TreeNode(1)
    root.left.left = TreeNode(6)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(0)
    root.right.right = TreeNode(8)
    root.left.right.left = TreeNode(7)
    root.left.right.right = TreeNode(4)

    # Test case 1: LCA(5, 1) = 3
    p1, q1 = root.left, root.right

    # Test case 2: LCA(5, 4) = 5
    p2, q2 = root.left, root.left.right.right

    # Test case 3: LCA(6, 4) = 5
    p3, q3 = root.left.left, root.left.right.right

    pass
