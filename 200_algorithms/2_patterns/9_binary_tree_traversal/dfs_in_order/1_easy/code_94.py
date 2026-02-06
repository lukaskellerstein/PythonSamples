
# -----------------------
# Binary Tree Inorder Traversal (LeetCode 94)
# -----------------------

# Difficulty: Easy

# Problem: Given the root of a binary tree, return the inorder traversal
# of its nodes' values. Inorder: Left -> Root -> Right.

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
# Inorder traversal: Left -> Root -> Right
# Visit: 1(no left) -> print 1 -> go right to 2
#        2(go left to 3) -> 3(no left) -> print 3 -> back to 2 -> print 2
# Result: [1, 3, 2]
#
#       4
#      / \
#     2   6
#    / \ / \
#   1  3 5  7
#
# Inorder: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 (sorted for BST!)
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
# Iterative Inorder solution (Optimal)
#
# time complexity = O(n) - visit every node once
# space complexity = O(h) - h = height of tree (stack size)
# ----------------------------------------------------

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    result = []
    stack = []
    current = root

    while current or stack:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()
        result.append(current.val)

        # Move to right subtree
        current = current.right

    return result


# Example
print(inorder_traversal(root))  # [1, 3, 2]


# ----------------------------------------------------
# Recursive solution
#
# time complexity = O(n) - visit every node once
# space complexity = O(h) - recursion stack depth = height of tree
# ----------------------------------------------------

def inorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)         # Left
        result.append(node.val) # Root
        dfs(node.right)        # Right

    dfs(root)
    return result


# Example
print(inorder_traversal_recursive(root))  # [1, 3, 2]


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    # Test case 2: empty tree
    root2 = None

    # Test case 3: single node
    root3 = TreeNode(1)

    # Test case 4: BST
    root4 = TreeNode(4)
    root4.left = TreeNode(2)
    root4.right = TreeNode(6)
    root4.left.left = TreeNode(1)
    root4.left.right = TreeNode(3)
    root4.right.left = TreeNode(5)
    root4.right.right = TreeNode(7)

    test_cases = [
        (root, [1, 3, 2]),
        (root2, []),
        (root3, [1]),
        (root4, [1, 2, 3, 4, 5, 6, 7]),
    ]

    print("\nInorder Traversal Results:")
    print("-" * 50)
    print(f"{'Expected':<25} {'Iterative':<25} {'Recursive':<25}")
    print("-" * 50)

    for tree_root, expected in test_cases:
        result1 = inorder_traversal(tree_root)
        result2 = inorder_traversal_recursive(tree_root)
        print(f"{str(expected):<25} {str(result1):<25} {str(result2):<25}")
