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

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def average_of_levels_brute_force(root: Optional[TreeNode]) -> List[float]:
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

def average_of_levels(root: Optional[TreeNode]) -> List[float]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    # Test case 1: standard tree
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)

    # Test case 2: single node
    root2 = TreeNode(1)

    # Test case 3: left-skewed tree
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)

    test_cases = [
        {"args": (root1,), "expected": [3.0, 14.5, 11.0]},
        {"args": (root2,), "expected": [1.0]},
        {"args": (root3,), "expected": [1.0, 2.0, 3.0]},
    ]

    for test in test_cases:
        args = test["args"]
        expected = test["expected"]

        result1 = average_of_levels_brute_force(*args)
        result2 = average_of_levels(*args)

        assert result1 == expected, f"Brute force failed: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed: got {result2}, expected {expected}"

        print(f"expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
