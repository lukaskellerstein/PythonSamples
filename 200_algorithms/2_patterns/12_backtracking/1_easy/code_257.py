
# -----------------------
# Binary Tree Paths (LeetCode 257)
# -----------------------

# Difficulty: Easy

# Problem: Given the root of a binary tree, return all root-to-leaf paths
# in any order. A leaf is a node with no children.

# -----------------------
# VISUALIZATION
# -----------------------
#
#       1
#      / \
#     2   3
#      \
#       5
#
# Root-to-leaf paths:
#   1 -> 2 -> 5  (path: "1->2->5")
#   1 -> 3       (path: "1->3")
#
# Backtracking approach:
#   path = [1]
#     path = [1, 2]
#       path = [1, 2, 5] <- leaf! record "1->2->5"
#       backtrack: path = [1, 2]
#     backtrack: path = [1]
#     path = [1, 3] <- leaf! record "1->3"
#     backtrack: path = [1]
#
# Output: ["1->2->5", "1->3"]
#
# -----------------------

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build test tree:  1
#                  / \
#                 2   3
#                  \
#                   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)


# ----------------------------------------------------
# Backtracking solution (Optimal)
#
# time complexity = O(n) - visit every node once
# space complexity = O(h) - h = height of tree (recursion + path)
# ----------------------------------------------------

def binary_tree_paths(root: Optional[TreeNode]) -> List[str]:
    if not root:
        return []

    result = []
    path = []

    def backtrack(node):
        path.append(str(node.val))

        # Leaf node — record the path
        if not node.left and not node.right:
            result.append("->".join(path))
        else:
            if node.left:
                backtrack(node.left)
            if node.right:
                backtrack(node.right)

        path.pop()  # backtrack

    backtrack(root)
    return result


# Example
print(binary_tree_paths(root))  # ["1->2->5", "1->3"]


# ----------------------------------------------------
# Brute Force solution (String concatenation, no backtracking)
#
# time complexity = O(n * h) - each path string copied at each level
# space complexity = O(n * h) - storing partial path strings
# ----------------------------------------------------

def binary_tree_paths_brute_force(root: Optional[TreeNode]) -> List[str]:
    if not root:
        return []

    result = []

    # Stack of (node, path_string)
    stack = [(root, str(root.val))]

    while stack:
        node, path = stack.pop()

        # Leaf node
        if not node.left and not node.right:
            result.append(path)
        else:
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))

    return result


# Example
print(binary_tree_paths_brute_force(root))  # ["1->2->5", "1->3"]


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    # Test case 2: single node
    root2 = TreeNode(1)

    # Test case 3: left-skewed tree
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)

    # Test case 4: full tree
    root4 = TreeNode(1)
    root4.left = TreeNode(2)
    root4.right = TreeNode(3)
    root4.left.left = TreeNode(4)
    root4.left.right = TreeNode(5)

    test_cases = [
        (root, ["1->2->5", "1->3"]),
        (root2, ["1"]),
        (root3, ["1->2->3"]),
        (root4, ["1->2->4", "1->2->5", "1->3"]),
    ]

    print("\nBinary Tree Paths Results:")
    print("-" * 60)

    for tree_root, expected in test_cases:
        result1 = sorted(binary_tree_paths(tree_root))
        result2 = sorted(binary_tree_paths_brute_force(tree_root))
        exp_sorted = sorted(expected)
        print(f"Backtrack:  {result1}")
        print(f"BruteForce: {result2}")
        print(f"Expected:   {exp_sorted}")
        print(f"Match:      {result1 == exp_sorted and result2 == exp_sorted}")
        print("-" * 60)
