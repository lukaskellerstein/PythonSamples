
# -----------------------
# House Robber III (LeetCode 337)
# -----------------------

# Difficulty: Medium
# Sub-pattern: Tree DP

# Problem: The thief has found himself a new place for his thievery again.
# There is only one entrance to this area, called root. Besides the root,
# each house has one and only one parent house. The thief realized that all
# houses in this place form a binary tree. It will automatically contact the
# police if two directly-linked houses were broken into on the same night.
# Return the maximum amount of money the thief can rob without alerting police.

# -----------------------

#       3
#      / \
#     2   3
#      \   \
#       3   1
# Answer: 7 (rob nodes 3 + 3 + 1 = 7, skipping the two 2/3 children)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build example tree
root = TreeNode(3)
root.left = TreeNode(2, None, TreeNode(3))
root.right = TreeNode(3, None, TreeNode(1))

# ----------------------------------------------------
# Tree DP solution (post-order traversal)
#
# Each node returns a tuple: (max_if_not_robbed, max_if_robbed)
#
# time complexity = O(n) - visit each node once
# space complexity = O(h) - recursion stack, h = tree height
# ----------------------------------------------------


def rob(root):
    def dp(node):
        if not node:
            return (0, 0)  # (not_robbed, robbed)

        left = dp(node.left)
        right = dp(node.right)

        # If we don't rob this node: take max of children (rob or not each)
        not_robbed = max(left) + max(right)

        # If we rob this node: children must NOT be robbed
        robbed = node.val + left[0] + right[0]

        return (not_robbed, robbed)

    return max(dp(root))


# Example
print(rob(root))  # 7


# ----------------------------------------------------
# Memoization solution (HashMap on nodes)
#
# time complexity = O(n) - each node solved once
# space complexity = O(n) - memo dict + recursion stack
# ----------------------------------------------------


def rob_memo(root):
    memo = {}

    def dp(node):
        if not node:
            return 0
        if node in memo:
            return memo[node]

        # Rob this node → skip children, take grandchildren
        rob_this = node.val
        if node.left:
            rob_this += dp(node.left.left) + dp(node.left.right)
        if node.right:
            rob_this += dp(node.right.left) + dp(node.right.right)

        # Skip this node → take children
        skip_this = dp(node.left) + dp(node.right)

        memo[node] = max(rob_this, skip_this)
        return memo[node]

    return dp(root)


# Example
print(rob_memo(root))  # 7


# ----------------------------------------------------
# Brute Force (Recursion) solution
#
# time complexity = O(2^n) - overlapping subproblems recomputed
# space complexity = O(h) - recursion stack
# ----------------------------------------------------


def rob_brute(root):
    def dp(node):
        if not node:
            return 0

        # Rob this node → skip children, take grandchildren
        rob_this = node.val
        if node.left:
            rob_this += dp(node.left.left) + dp(node.left.right)
        if node.right:
            rob_this += dp(node.right.left) + dp(node.right.right)

        # Skip this node → take children
        skip_this = dp(node.left) + dp(node.right)

        return max(rob_this, skip_this)

    return dp(root)


# Example
print(rob_brute(root))  # 7
