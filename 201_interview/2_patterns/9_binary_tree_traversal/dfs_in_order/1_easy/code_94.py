from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Binary Tree Inorder Traversal (LeetCode 94)
# ============================================================
# Difficulty: Easy
# Pattern: DFS In-Order Traversal
#
# Given the root of a binary tree, return the inorder traversal
# of its nodes' values. Inorder traversal visits nodes in the
# order: Left subtree -> Root -> Right subtree.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [1,null,2,3]
#   Output: [1, 3, 2]
#   Explanation: Go left (none), visit 1, go right to 2,
#                go left to 3, visit 3, back to 2, visit 2.
#
# Example 2:
#   Input: root = []
#   Output: []
#
# Example 3:
#   Input: root = [1]
#   Output: [1]
#
# Example 4:
#   Input: root = [4,2,6,1,3,5,7] (BST)
#   Output: [1, 2, 3, 4, 5, 6, 7]
#   Explanation: Inorder traversal of a BST yields sorted order.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the tree is in the range [0, 100]
# - -100 <= Node.val <= 100
#
# ============================================================
# VISUALIZATION
# ============================================================
#
#       1
#        \
#         2
#        /
#       3
#
# Inorder: Left -> Root -> Right
# Visit 1 (no left) -> print 1 -> go right to 2
# Visit 2 (go left to 3) -> 3 (no left) -> print 3 -> back to 2 -> print 2
# Result: [1, 3, 2]
#
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7
#
# Inorder: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (sorted for BST!)
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Recursive)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def inorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Iterative with Stack)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1
    root1 = TreeNode(1)
    root1.right = TreeNode(2)
    root1.right.left = TreeNode(3)
    # Expected: [1, 3, 2]

    # Test case 2: empty tree
    root2 = None
    # Expected: []

    # Test case 3: single node
    root3 = TreeNode(1)
    # Expected: [1]

    # Test case 4: BST
    root4 = TreeNode(4)
    root4.left = TreeNode(2)
    root4.right = TreeNode(6)
    root4.left.left = TreeNode(1)
    root4.left.right = TreeNode(3)
    root4.right.left = TreeNode(5)
    root4.right.right = TreeNode(7)
    # Expected: [1, 2, 3, 4, 5, 6, 7]

    pass
