
# ============================================================
# PROBLEM: Binary Tree Paths (LeetCode 257)
# ============================================================
# Difficulty: Easy
# Pattern: Backtracking
#
# Given the root of a binary tree, return all root-to-leaf paths in
# any order. A leaf is a node with no children. Each path should be
# represented as a string with node values separated by "->".
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [1,2,3,null,5]
#   Output: ["1->2->5", "1->3"]
#   Explanation: Two root-to-leaf paths exist in the tree.
#
# Example 2:
#   Input: root = [1]
#   Output: ["1"]
#   Explanation: Single node is both root and leaf.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the tree is in the range [1, 100]
# - -100 <= Node.val <= 100
#
# ============================================================
# VISUALIZATION
# ============================================================
#
#       1
#      / \
#     2   3
#      \
#       5
#
# Backtracking approach:
#   path = [1]
#     path = [1, 2]
#       path = [1, 2, 5]  <-- leaf! record "1->2->5"
#       backtrack: path = [1, 2]
#     backtrack: path = [1]
#     path = [1, 3]        <-- leaf! record "1->3"
#     backtrack: path = [1]
#
# Output: ["1->2->5", "1->3"]
#

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (String concatenation, no backtracking)
# ============================================================
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def binary_tree_paths_brute_force(root: Optional[TreeNode]) -> List[str]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Backtracking)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    pass


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
