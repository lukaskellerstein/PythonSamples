
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

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def binary_tree_paths_brute_force(root: Optional[TreeNode]) -> List[str]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Backtracking)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    # Test 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.right = TreeNode(5)

    # Test 2: single node
    root2 = TreeNode(1)

    test_cases = [
        {"args": (root1,), "expected": ["1->2->5", "1->3"]},
        {"args": (root2,), "expected": ["1"]},
    ]

    for test in test_cases:
        args = test["args"]
        expected = sorted(test["expected"])

        result1 = sorted(binary_tree_paths_brute_force(*args))
        result2 = sorted(binary_tree_paths(*args))

        assert result1 == expected, f"Brute force failed: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed: got {result2}, expected {expected}"

        print(f"expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
