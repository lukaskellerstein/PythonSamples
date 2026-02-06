
# -----------------------
# Serialize and Deserialize Binary Tree (LeetCode 297)
# -----------------------

# Difficulty: Hard

# Problem: Design an algorithm to serialize a binary tree to a string and
# deserialize that string back to the original tree structure. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.

# -----------------------

# For given tree:
#       1
#      / \
#     2   3
#        / \
#       4   5
# serialize to "1,2,3,null,null,4,5" and deserialize back to the same tree.

from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Build example tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.left = TreeNode(4)
root.right.right = TreeNode(5)

# # ----------------------------------------------------
# # BFS (Level Order) solution
# #
# # time complexity = O(n) - visit each node once for both serialize and deserialize
# # space complexity = O(n) - queue and string store all nodes
# # ----------------------------------------------------


# def serialize(root):
#     if not root:
#         return ""

#     result = []
#     queue = deque([root])

#     while queue:
#         node = queue.popleft()

#         if node:
#             result.append(str(node.val))
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append("null")

#     return ",".join(result)


# def deserialize(data):
#     if not data:
#         return None

#     values = data.split(",")
#     root = TreeNode(int(values[0]))
#     queue = deque([root])
#     i = 1

#     while queue and i < len(values):
#         node = queue.popleft()

#         # Left child
#         if values[i] != "null":
#             node.left = TreeNode(int(values[i]))
#             queue.append(node.left)
#         i += 1

#         # Right child
#         if i < len(values) and values[i] != "null":
#             node.right = TreeNode(int(values[i]))
#             queue.append(node.right)
#         i += 1

#     return root


# # Example
# serialized = serialize(root)
# print(serialized)  # 1,2,3,null,null,4,5
# deserialized = deserialize(serialized)
# print(serialize(deserialized))  # 1,2,3,null,null,4,5


# ----------------------------------------------------
# Brute Force (Preorder DFS) solution
#
# time complexity = O(n) - visit each node once for both serialize and deserialize
# space complexity = O(n) - recursion stack up to tree height + string stores all nodes
# ----------------------------------------------------


def serialize_brute_force(root):
    result = []

    def dfs(node):
        if not node:
            result.append("null")
            return

        result.append(str(node.val))
        dfs(node.left)
        dfs(node.right)

    dfs(root)
    return ",".join(result)


def deserialize_brute_force(data):
    if not data:
        return None

    values = iter(data.split(","))

    def dfs():
        val = next(values)

        if val == "null":
            return None

        node = TreeNode(int(val))
        node.left = dfs()
        node.right = dfs()
        return node

    return dfs()


# Example
serialized_bf = serialize_brute_force(root)
print(serialized_bf)  # 1,2,null,null,3,4,null,null,5,null,null
deserialized_bf = deserialize_brute_force(serialized_bf)
print(serialize_brute_force(deserialized_bf))  # 1,2,null,null,3,4,null,null,5,null,null
