from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Binary Tree Preorder Traversal (LeetCode 144)
# ============================================================
# Difficulty: Easy
# Pattern: DFS Pre-Order Traversal
#
# Given the root of a binary tree, return the preorder traversal
# of its nodes' values. Preorder traversal visits nodes in the
# order: Root -> Left subtree -> Right subtree.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [1,null,2,3]
#   Output: [1, 2, 3]
#   Explanation: Visit 1 (root), no left child, go right to 2,
#                visit 2, go left to 3, visit 3.
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
#   Input: root = [1,2,3,4,5]
#   Output: [1, 2, 4, 5, 3]
#   Explanation: Root first (1), then entire left subtree (2,4,5),
#                then right subtree (3).
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
# Preorder: Root -> Left -> Right
# Visit: print 1 -> 1 (no left) -> go right to 2
# Visit: print 2 -> go left to 3
# Visit: print 3 -> 3 (no children) -> done
# Result: [1, 2, 3]
#
#       1
#      / \
#     2   3
#    / \
#   4   5
#
# Preorder: 1 -> 2 -> 4 -> 5 -> 3
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Recursive)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def preorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Iterative with Stack)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
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
    # Expected: [1, 2, 3]

    # Test case 2: empty tree
    root2 = None
    # Expected: []

    # Test case 3: single node
    root3 = TreeNode(1)
    # Expected: [1]

    # Test case 4: full tree
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)
    # Expected: [1, 2, 4, 5, 3]

    pass
