from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Binary Tree Level Order Traversal (LeetCode 102)
# ============================================================
# Difficulty: Medium
# Pattern: BFS (Level-Order Traversal)
#
# Given the root of a binary tree, return the level order traversal
# of its nodes' values (i.e., from left to right, level by level).
# Each level should be returned as a separate list.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [3,9,20,null,null,15,7]
#   Output: [[3], [9, 20], [15, 7]]
#   Explanation: Level 0: [3], Level 1: [9, 20], Level 2: [15, 7]
#
# Example 2:
#   Input: root = [1]
#   Output: [[1]]
#
# Example 3:
#   Input: root = []
#   Output: []
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the tree is in the range [0, 2000]
# - -1000 <= Node.val <= 1000
#
# ============================================================
# VISUALIZATION
# ============================================================
#
#       3           Level 0: [3]
#      / \
#     9   20        Level 1: [9, 20]
#        /  \
#       15   7      Level 2: [15, 7]
#
# BFS uses a queue to process nodes level by level:
#   Queue: [3] -> process 3, add 9, 20
#   Queue: [9, 20] -> process 9 (no children), process 20 (add 15, 7)
#   Queue: [15, 7] -> process 15, process 7
#
# Output: [[3], [9, 20], [15, 7]]
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def level_order_brute_force(root: Optional[TreeNode]) -> List[List[int]]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1: standard tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    # Expected: [[3], [9, 20], [15, 7]]

    # Test case 2: single node
    root2 = TreeNode(1)
    # Expected: [[1]]

    # Test case 3: empty tree
    root3 = None
    # Expected: []

    # Test case 4: left-skewed tree
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.left.left = TreeNode(3)
    # Expected: [[1], [2], [3]]

    pass
