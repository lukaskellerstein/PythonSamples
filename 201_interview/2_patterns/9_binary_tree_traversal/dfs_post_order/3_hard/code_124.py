from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Binary Tree Maximum Path Sum (LeetCode 124)
# ============================================================
# Difficulty: Hard
# Pattern: DFS Post-Order Traversal
#
# A path in a binary tree is a sequence of nodes where each pair of
# adjacent nodes has an edge connecting them. A node can only appear
# in the sequence at most once. The path does not need to pass through
# the root. Given the root of a binary tree, return the maximum path
# sum of any non-empty path.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [1,2,3]
#   Output: 6
#   Explanation: The optimal path is 2 -> 1 -> 3 with sum 2 + 1 + 3 = 6.
#
# Example 2:
#   Input: root = [-10,9,20,null,null,15,7]
#   Output: 42
#   Explanation: The optimal path is 15 -> 20 -> 7 with sum 15 + 20 + 7 = 42.
#
# Example 3:
#   Input: root = [-3]
#   Output: -3
#   Explanation: Single node, the maximum path sum is -3.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the tree is in the range [1, 3 * 10^4]
# - -1000 <= Node.val <= 1000
#
# ============================================================
# VISUALIZATION
# ============================================================
#
#       1
#      / \
#     2   3
#
# Path: 2 -> 1 -> 3, Sum = 6
#
#      -10
#      /  \
#     9   20
#        /  \
#       15   7
#
# Path: 15 -> 20 -> 7, Sum = 42
# (Skips -10 and 9 because they reduce the sum)
#
# Key insight: At each node, we decide:
#   1. The path through this node (left + node + right) - could be max
#   2. The gain we can extend to parent (node + max(left, right))
#      We can only extend one direction upward (not both).
#   3. Negative gains are ignored (clamped to 0).
#


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def max_path_sum_brute_force(root: Optional[TreeNode]) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Post-Order DFS)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def max_path_sum(root: Optional[TreeNode]) -> int:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    # Test case 1: simple tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    # Test case 2: tree with negative root
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)

    # Test case 3: single negative node
    root3 = TreeNode(-3)

    # Test case 4: all negative
    root4 = TreeNode(-1)
    root4.left = TreeNode(-2)
    root4.right = TreeNode(-3)

    test_cases = [
        {"args": (root1,), "expected": 6},
        {"args": (root2,), "expected": 42},
        {"args": (root3,), "expected": -3},
        {"args": (root4,), "expected": -1},
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = max_path_sum_brute_force(*args)
        result2 = max_path_sum(*args)

        assert result1 == expected, f"Brute force failed: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed: got {result2}, expected {expected}"

        print(f"expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
