from binary_tree import bt1

# --------------------------------------------
# In-order traversal = Left → Root → Right
# --------------------------------------------

def search_dfs_in_order(root, target):
    """Search for a value using Depth-First Search (DFS) with In-order traversal."""
    if not root:
        return None

    # LEFT - Search in the left subtree
    left_result = search_dfs_in_order(root.left, target)
    if left_result:
        return left_result

    # ROOT - Check the current node
    if root.value == target:
        return root

    # RIGHT - Search in the right subtree
    return search_dfs_in_order(root.right, target)

print(search_dfs_in_order(bt1.root, 0) != None)
print(search_dfs_in_order(bt1.root, 100000) != None)