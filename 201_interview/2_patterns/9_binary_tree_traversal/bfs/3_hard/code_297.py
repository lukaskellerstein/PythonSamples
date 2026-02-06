from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Serialize and Deserialize Binary Tree (LeetCode 297)
# ============================================================
# Difficulty: Hard
# Pattern: BFS (Level-Order Traversal)
#
# Design an algorithm to serialize a binary tree into a string and
# deserialize that string back to the original tree structure. There
# is no restriction on how your serialization/deserialization algorithm
# should work. You just need to ensure that a binary tree can be
# serialized to a string and this string can be deserialized to the
# original tree structure.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [1,2,3,null,null,4,5]
#   Serialized: "1,2,3,null,null,4,5"
#   Output: [1,2,3,null,null,4,5]
#   Explanation: The tree is serialized level by level using BFS.
#                Null children are represented as "null".
#
# Example 2:
#   Input: root = []
#   Serialized: ""
#   Output: []
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the tree is in the range [0, 10^4]
# - -1000 <= Node.val <= 1000
#
# ============================================================
# VISUALIZATION
# ============================================================
#
#       1
#      / \
#     2   3
#        / \
#       4   5
#
# BFS Level-Order serialization:
#   Level 0: 1
#   Level 1: 2, 3
#   Level 2: null, null, 4, 5
#
#   Serialized: "1,2,3,null,null,4,5"
#
# Deserialization rebuilds the tree by reading values and
# assigning left/right children level by level using a queue.
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (DFS Pre-Order)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def serialize_brute_force(root: Optional[TreeNode]) -> str:
    pass


def deserialize_brute_force(data: str) -> Optional[TreeNode]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (BFS Level-Order)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def serialize(root: Optional[TreeNode]) -> str:
    pass


def deserialize(data: str) -> Optional[TreeNode]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here

    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)
    # serialize(root1) -> "1,2,3,null,null,4,5"
    # deserialize("1,2,3,null,null,4,5") -> reconstructed tree

    # Test case 2: empty tree
    root2 = None
    # serialize(root2) -> ""
    # deserialize("") -> None

    # Test case 3: single node
    root3 = TreeNode(42)
    # serialize(root3) -> "42"
    # deserialize("42") -> TreeNode(42)

    pass
