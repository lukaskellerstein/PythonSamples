from typing import Optional, List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Vertical Order Traversal of a Binary Tree (LeetCode 987)
# ============================================================
# Difficulty: Hard
# Pattern: BFS (Level-Order Traversal)
#
# Given the root of a binary tree, calculate the vertical order
# traversal of the binary tree. For each node at position (row, col),
# its left child is at (row+1, col-1) and its right child is at
# (row+1, col+1). The vertical order traversal starts from the leftmost
# column and ends at the rightmost column. For nodes in the same row
# and column, sort them by value.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [3,9,20,null,null,15,7]
#   Output: [[9], [3, 15], [20], [7]]
#   Explanation: Column -1: [9], Column 0: [3,15], Column 1: [20], Column 2: [7]
#
# Example 2:
#   Input: root = [1,2,3,4,5,6,7]
#   Output: [[4], [2], [1, 5, 6], [3], [7]]
#   Explanation: Nodes 5 and 6 are at same position (row=2, col=0),
#                sorted by value: [5, 6]
#
# Example 3:
#   Input: root = [1,2,3,4,6,null,null,null,null,5]
#   Output: [[4], [2, 5], [1, 6], [3]]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the tree is in the range [1, 1000]
# - 0 <= Node.val <= 1000
#
# ============================================================
# VISUALIZATION
# ============================================================
#
#         1 (r=0,c=0)
#        / \
#       2   3 (r=1,c=1)
#  (r=1,c=-1)
#      / \ / \
#     4  5 6  7
# (r=2,  (r=2, (r=2,  (r=2,
#  c=-2)  c=0)  c=0)   c=2)
#
# Nodes 5 and 6 are at same (row=2, col=0) -> sorted by value: [5, 6]
#
# Column -2: [(2, 4)]          -> [4]
# Column -1: [(1, 2)]          -> [2]
# Column  0: [(0, 1),(2,5),(2,6)] -> [1, 5, 6] (5,6 sorted by value)
# Column  1: [(1, 3)]          -> [3]
# Column  2: [(2, 7)]          -> [7]
#
# Output: [[4], [2], [1, 5, 6], [3], [7]]
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def vertical_traversal_brute_force(root: Optional[TreeNode]) -> List[List[int]]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def vertical_traversal(root: Optional[TreeNode]) -> List[List[int]]:
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

    # Test case 2: nodes at same position
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)
    root2.right.left = TreeNode(6)
    root2.right.right = TreeNode(7)
    # Expected: [[4], [2], [1, 5, 6], [3], [7]]

    # Test case 3: same position, different values
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.right = TreeNode(3)
    root3.left.left = TreeNode(4)
    root3.left.right = TreeNode(6)
    root3.left.right.left = TreeNode(5)
    # Expected: [[4], [2, 5], [1, 6], [3]]

    pass
