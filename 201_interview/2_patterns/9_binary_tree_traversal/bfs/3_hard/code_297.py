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

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def serialize_brute_force(root: Optional[TreeNode]) -> str:
    pass


def deserialize_brute_force(data: str) -> Optional[TreeNode]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (BFS Level-Order)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def serialize(root: Optional[TreeNode]) -> str:
    pass


def deserialize(data: str) -> Optional[TreeNode]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    # Test case 1
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.right.left = TreeNode(4)
    root1.right.right = TreeNode(5)

    # Test case 2: empty tree
    root2 = None

    # Test case 3: single node
    root3 = TreeNode(42)

    test_cases = [
        {"root": root1, "description": "standard tree"},
        {"root": root2, "description": "empty tree"},
        {"root": root3, "description": "single node"},
    ]

    def trees_equal(t1, t2):
        if not t1 and not t2:
            return True
        if not t1 or not t2:
            return False
        return t1.val == t2.val and trees_equal(t1.left, t2.left) and trees_equal(t1.right, t2.right)

    for test in test_cases:
        root = test["root"]
        desc = test["description"]

        s1 = serialize_brute_force(root)
        r1 = deserialize_brute_force(s1)
        assert trees_equal(root, r1), f"Brute force round-trip failed for {desc}"

        s2 = serialize(root)
        r2 = deserialize(s2)
        assert trees_equal(root, r2), f"Optimal round-trip failed for {desc}"

        print(f"{desc}: brute_force='{s1}', optimal='{s2}' ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
