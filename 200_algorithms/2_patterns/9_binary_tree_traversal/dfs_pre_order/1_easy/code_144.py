
# -----------------------
# Binary Tree Preorder Traversal (LeetCode 144)
# -----------------------

# Difficulty: Easy

# Problem: Given the root of a binary tree, return the preorder traversal
# of its nodes' values. Preorder: Root -> Left -> Right.

# -----------------------
# VISUALIZATION
# -----------------------
#
#       1
#        \
#         2
#        /
#       3
#
# Preorder traversal: Root -> Left -> Right
# Visit: print 1 -> 1(no left) -> go right to 2
#        print 2 -> go left to 3
#        print 3 -> 3(no left, no right) -> done
# Result: [1, 2, 3]
#
#       1
#      / \
#     2   3
#    / \
#   4   5
#
# Preorder: 1 -> 2 -> 4 -> 5 -> 3
#
# -----------------------

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build test tree:  1
#                    \
#                     2
#                    /
#                   3
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)


# ----------------------------------------------------
# Iterative Preorder solution (Optimal)
#
# time complexity = O(n) - visit every node once
# space complexity = O(h) - h = height of tree (stack size)
# ----------------------------------------------------

def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first so left is processed first (LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result


# Example
print(preorder_traversal(root))  # [1, 2, 3]


# ----------------------------------------------------
# Recursive solution
#
# time complexity = O(n) - visit every node once
# space complexity = O(h) - recursion stack depth = height of tree
# ----------------------------------------------------

def preorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
        if not node:
            return

        result.append(node.val) # Root
        dfs(node.left)          # Left
        dfs(node.right)         # Right

    dfs(root)
    return result


# Example
print(preorder_traversal_recursive(root))  # [1, 2, 3]


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    # Test case 2: empty tree
    root2 = None

    # Test case 3: single node
    root3 = TreeNode(1)

    # Test case 4: full tree
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)

    test_cases = [
        (root, [1, 2, 3]),
        (root2, []),
        (root3, [1]),
        (root4, [1, 2, 4, 5, 3]),
    ]

    print("\nPreorder Traversal Results:")
    print("-" * 50)
    print(f"{'Expected':<25} {'Iterative':<25} {'Recursive':<25}")
    print("-" * 50)

    for tree_root, expected in test_cases:
        result1 = preorder_traversal(tree_root)
        result2 = preorder_traversal_recursive(tree_root)
        print(f"{str(expected):<25} {str(result1):<25} {str(result2):<25}")
