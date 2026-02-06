from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Average of Levels in Binary Tree (LeetCode 637)
# ============================================================
# Difficulty: Easy
# Pattern: BFS (Level-Order Traversal)
#
# Given the root of a binary tree, return the average value of the
# nodes on each level in the form of an array. Answers within 10^-5
# of the actual answer will be accepted.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [3,9,20,null,null,15,7]
#   Output: [3.0, 14.5, 11.0]
#   Explanation: Level 0 avg = 3/1 = 3.0, Level 1 avg = (9+20)/2 = 14.5,
#                Level 2 avg = (15+7)/2 = 11.0
#
# Example 2:
#   Input: root = [1]
#   Output: [1.0]
#
# Example 3:
#   Input: root = [1,2,null,3]
#   Output: [1.0, 2.0, 3.0]
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
#       3
#      / \
#     9   20
#        /  \
#       15   7
#
# Level 0: [3]       -> avg = 3.0
# Level 1: [9, 20]   -> avg = 14.5
# Level 2: [15, 7]   -> avg = 11.0
#
# Output: [3.0, 14.5, 11.0]
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def average_of_levels_brute_force(root: Optional[TreeNode]) -> List[float]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def average_of_levels(root: Optional[TreeNode]) -> List[float]:
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
    # Expected: [3.0, 14.5, 11.0]

    # Test case 2: single node
    root2 = TreeNode(1)
    # Expected: [1.0]

    # Test case 3: left-skewed tree
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    # Expected: [1.0, 2.0, 3.0]

    pass
