from typing import Optional, List
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# ============================================================
# PROBLEM: Diagonal Traversal of Binary Tree
# ============================================================
# Difficulty: Medium
# Pattern: BFS (Level-Order Traversal)
#
# Given a binary tree, return the diagonal traversal of the tree.
# A diagonal contains all nodes that can be reached by repeatedly
# going to the right child. Going left moves you to the next diagonal.
# Nodes on the same diagonal are traversed from top-right to bottom-left.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
#   Output: [[8, 10, 14], [3, 6, 7, 13], [1, 4]]
#   Explanation: Diagonal 0: 8->10->14, Diagonal 1: 3->6->7->13, Diagonal 2: 1->4
#
# Example 2:
#   Input: root = [1,2,3]
#   Output: [[1, 3], [2]]
#   Explanation: Diagonal 0: 1->3, Diagonal 1: 2
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the tree is in the range [0, 10^4]
# - -100 <= Node.val <= 100
#
# ============================================================
# VISUALIZATION
# ============================================================
#
#         8
#        / \
#       3   10
#      / \    \
#     1   6   14
#        / \  /
#       4  7 13
#
# Diagonal 0 (d=0): 8 --> 10 --> 14      (right keeps same diagonal)
# Diagonal 1 (d=1): 3 --> 6 --> 7 --> 13 (left moves to next diagonal)
# Diagonal 2 (d=2): 1 --> 4
#
# Output: [[8, 10, 14], [3, 6, 7, 13], [1, 4]]
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

def diagonal_traversal_brute_force(root: Optional[TreeNode]) -> List[List[int]]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def diagonal_traversal(root: Optional[TreeNode]) -> List[List[int]]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    # Test case 1
    root1 = TreeNode(8)
    root1.left = TreeNode(3)
    root1.right = TreeNode(10)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(6)
    root1.right.right = TreeNode(14)
    root1.left.right.left = TreeNode(4)
    root1.left.right.right = TreeNode(7)
    root1.right.right.left = TreeNode(13)

    # Test case 2
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)

    test_cases = [
        {"args": (root1,), "expected": [[8, 10, 14], [3, 6, 7, 13], [1, 4]]},
        {"args": (root2,), "expected": [[1, 3], [2]]},
        {"args": (None,), "expected": []},
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = diagonal_traversal_brute_force(*args)
        result2 = diagonal_traversal(*args)

        assert result1 == expected, f"Brute force failed: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed: got {result2}, expected {expected}"

        print(f"expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
