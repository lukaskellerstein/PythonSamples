
# -----------------------
# Binary Tree Postorder Traversal (LeetCode 145)
# -----------------------

# Difficulty: Easy

# Problem: Given the root of a binary tree, return the postorder traversal
# of its nodes' values. Postorder: Left -> Right -> Root.

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
# Postorder traversal: Left -> Right -> Root
# Visit: 1(no left) -> go right to 2
#        2(go left to 3) -> 3(no left, no right) -> print 3
#        back to 2(no right) -> print 2
#        back to 1 -> print 1
# Result: [3, 2, 1]
#
#       1
#      / \
#     2   3
#    / \
#   4   5
#
# Postorder: 4 -> 5 -> 2 -> 3 -> 1
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
# Iterative Postorder solution (Optimal)
#
# time complexity = O(n) - visit every node once
# space complexity = O(h) - h = height of tree (stack size)
# ----------------------------------------------------

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    # Trick: modified preorder (Root -> Right -> Left) then reverse
    result = []
    stack = [root]

    while stack:
        node = stack.pop()
        result.append(node.val)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return result[::-1]  # Reverse to get Left -> Right -> Root


# Example
print(postorder_traversal(root))  # [3, 2, 1]


# ----------------------------------------------------
# Recursive solution
#
# time complexity = O(n) - visit every node once
# space complexity = O(h) - recursion stack depth = height of tree
# ----------------------------------------------------

def postorder_traversal_recursive(root: Optional[TreeNode]) -> List[int]:
    result = []

    def dfs(node):
        if not node:
            return

        dfs(node.left)          # Left
        dfs(node.right)         # Right
        result.append(node.val) # Root

    dfs(root)
    return result


# Example
print(postorder_traversal_recursive(root))  # [3, 2, 1]


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
        (root, [3, 2, 1]),
        (root2, []),
        (root3, [1]),
        (root4, [4, 5, 2, 3, 1]),
    ]

    print("\nPostorder Traversal Results:")
    print("-" * 50)
    print(f"{'Expected':<25} {'Iterative':<25} {'Recursive':<25}")
    print("-" * 50)

    for tree_root, expected in test_cases:
        result1 = postorder_traversal(tree_root)
        result2 = postorder_traversal_recursive(tree_root)
        print(f"{str(expected):<25} {str(result1):<25} {str(result2):<25}")
