from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Binary Tree Postorder Traversal (LeetCode 145)
# ============================================================
# Difficulty: Easy
# Pattern: DFS Post-Order Traversal
#
# Given the root of a binary tree, return the postorder traversal
# of its nodes' values. Postorder traversal visits nodes in the
# order: Left subtree -> Right subtree -> Root.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [1,null,2,3]
#   Output: [3, 2, 1]
#   Explanation: Go right to 2, go left to 3, visit 3 (leaf),
#                visit 2 (right done), visit 1 (all done).
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
#   Output: [4, 5, 2, 3, 1]
#   Explanation: Left subtree first (4,5,2), then right (3), then root (1).
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
# Postorder: Left -> Right -> Root
# Visit 1 (no left) -> go right to 2
# Visit 2 (go left to 3) -> 3 (no left, no right) -> print 3
# Back to 2 (no right) -> print 2
# Back to 1 -> print 1
# Result: [3, 2, 1]
#
#       1
#      / \
#     2   3
#    / \
#   4   5
#
# Postorder: 4 -> 5 -> 2 -> 3 -> 1
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Recursive)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def postorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Iterative with Stack)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
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
    # Expected: [3, 2, 1]

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
    # Expected: [4, 5, 2, 3, 1]

    pass
