
# -----------------------
# Lowest Common Ancestor of a Binary Tree (LeetCode 236)
# -----------------------

# Difficulty: Medium

# Problem: Given a binary tree, find the lowest common ancestor (LCA) of two
# given nodes in the tree.
#
# The lowest common ancestor is defined as the lowest node in the tree that
# has both p and q as descendants (where we allow a node to be a descendant
# of itself).

# -----------------------

# Example:
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
#
# LCA(5, 1) = 3
# LCA(5, 4) = 5


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



# Build example tree
#         3
#        / \
#       5   1
#      / \ / \
#     6  2 0  8
#       / \
#      7   4
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

# Get references to nodes
p1, q1 = root.left, root.right  # 5 and 1
p2, q2 = root.left, root.left.right.right  # 5 and 4

# ----------------------------------------------------
# Postorder DFS solution (Optimal)
#
# time complexity = O(n) - visit each node once
# space complexity = O(h) - recursion stack, h = height of tree
#
# Idea: Postorder traversal - process children first, then current node.
# If current node is p or q, return it. If both left and right return
# non-null, current node is the LCA. Otherwise, return the non-null child.
# ----------------------------------------------------


def lowest_common_ancestor(root, p, q):
    if not root:
        return None

    # If we found p or q, return it
    if root == p or root == q:
        return root

    # Search in left and right subtrees (postorder: children first)
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # If both sides return a node, current node is LCA
    if left and right:
        return root

    # Otherwise, return the non-null result (or null if both are null)
    return left if left else right



print(lowest_common_ancestor(root, p1, q1).val)  # 3
print(lowest_common_ancestor(root, p2, q2).val)  # 5


# ----------------------------------------------------
# Iterative with Parent Pointers solution
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - parent map and ancestors set
#
# Idea: Build parent pointers using BFS/DFS. Then trace ancestors of p
# and find first common ancestor with q.
# ----------------------------------------------------

from collections import deque


def lowest_common_ancestor_iterative(root, p, q):
    if not root:
        return None

    # Build parent pointer map using BFS
    parent = {root: None}
    queue = deque([root])

    # Continue until we find both p and q
    while p not in parent or q not in parent:
        node = queue.popleft()
        if node.left:
            parent[node.left] = node
            queue.append(node.left)
        if node.right:
            parent[node.right] = node
            queue.append(node.right)

    # Collect all ancestors of p
    ancestors = set()
    while p:
        ancestors.add(p)
        p = parent[p]

    # Find first ancestor of q that is also ancestor of p
    while q not in ancestors:
        q = parent[q]

    return q


print(lowest_common_ancestor_iterative(root, p1, q1).val)  # 3
print(lowest_common_ancestor_iterative(root, p2, q2).val)  # 5


# ----------------------------------------------------
# Brute Force solution (Path Finding)
#
# time complexity = O(n) - but with higher constant factor
# space complexity = O(n) - storing paths
#
# Idea: Find paths from root to p and q, then find the last common node.
# ----------------------------------------------------


def lowest_common_ancestor_brute_force(root, p, q):
    def find_path(node, target, path):
        """Find path from node to target, return True if found."""
        if not node:
            return False

        path.append(node)

        if node == target:
            return True

        if find_path(node.left, target, path) or find_path(node.right, target, path):
            return True

        path.pop()
        return False

    # Find paths to p and q
    path_p = []
    path_q = []
    find_path(root, p, path_p)
    find_path(root, q, path_q)

    # Find last common node in both paths
    lca = None
    for i in range(min(len(path_p), len(path_q))):
        if path_p[i] == path_q[i]:
            lca = path_p[i]
        else:
            break

    return lca


print(lowest_common_ancestor_brute_force(root, p1, q1).val)  # 3
print(lowest_common_ancestor_brute_force(root, p2, q2).val)  # 5


# ----------------------------------------------------
# Naive Brute Force (Check each node)
#
# time complexity = O(n^2) - for each node, check if p and q are descendants
# space complexity = O(h) - recursion stack
#
# Idea: For each node, check if both p and q are in its subtree.
# The deepest such node is the LCA.
# ----------------------------------------------------


def lowest_common_ancestor_naive(root, p, q):
    def contains(node, target):
        """Check if target is in subtree rooted at node."""
        if not node:
            return False
        if node == target:
            return True
        return contains(node.left, target) or contains(node.right, target)

    def find_lca(node):
        if not node:
            return None

        # If current node is p or q, and the other is in subtree, this is LCA
        if node == p and contains(node, q):
            return node
        if node == q and contains(node, p):
            return node

        # Check if both are in left or right subtree
        p_in_left = contains(node.left, p)
        q_in_left = contains(node.left, q)

        # If both in same subtree, recurse into that subtree
        if p_in_left and q_in_left:
            return find_lca(node.left)
        if not p_in_left and not q_in_left:
            return find_lca(node.right)

        # Split across subtrees - current node is LCA
        return node

    return find_lca(root)


print(lowest_common_ancestor_naive(root, p1, q1).val)  # 3
print(lowest_common_ancestor_naive(root, p2, q2).val)  # 5
