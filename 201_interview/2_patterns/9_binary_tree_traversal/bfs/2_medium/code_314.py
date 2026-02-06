from typing import Optional, List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Binary Tree Vertical Order Traversal (LeetCode 314)
# ============================================================
# Difficulty: Medium
# Pattern: BFS (Level-Order Traversal)
#
# Given the root of a binary tree, return the vertical order traversal
# of its nodes' values (i.e., from top to bottom, column by column).
# If two nodes are in the same row and column, the order should be
# from left to right.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [3,9,20,null,null,15,7]
#   Output: [[9], [3, 15], [20], [7]]
#   Explanation: Column -1: [9], Column 0: [3, 15], Column 1: [20], Column 2: [7]
#
# Example 2:
#   Input: root = [3,9,8,4,0,1,7]
#   Output: [[4], [9], [3, 0, 1], [8], [7]]
#   Explanation: Nodes 0 and 1 are both at column 0, row 2. Left-to-right order.
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
#         3 (col=0)
#        / \
#  (c=-1)9  20 (col=1)
#           / \
#     (c=0)15  7 (col=2)
#
# Column -1: [9]
# Column  0: [3, 15]
# Column  1: [20]
# Column  2: [7]
#
#         3 (col=0)
#        / \
#  (c=-1)9   8 (col=1)
#      / \  / \
# (c=-2)4 0 1  7 (col=2)
#      (c=0)(c=0)
#
# Column -2: [4]
# Column -1: [9]
# Column  0: [3, 0, 1]
# Column  1: [8]
# Column  2: [7]
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def vertical_order_brute_force(root: Optional[TreeNode]) -> List[List[int]]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def vertical_order(root: Optional[TreeNode]) -> List[List[int]]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    # Expected: [[9], [3, 15], [20], [7]]

    # Test case 2
    root2 = TreeNode(3)
    root2.left = TreeNode(9)
    root2.right = TreeNode(8)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(0)
    root2.right.left = TreeNode(1)
    root2.right.right = TreeNode(7)
    # Expected: [[4], [9], [3, 0, 1], [8], [7]]

    # Test case 3: empty tree
    # Expected: []

    pass
