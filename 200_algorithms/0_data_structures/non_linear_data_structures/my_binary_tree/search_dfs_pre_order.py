from binary_tree import bt1

# --------------------------------------------
# Pre-order traversal = Root → Left → Right
# --------------------------------------------

def search_dfs_pre_order(root, target):
    """Search for a value using Depth-First Search (DFS) with Pre-order traversal."""
    if not root:
        return None

    # ROOT - Check the current node
    if root.value == target:
        return root

    # LEFT - Recursively search in the left
    left_result = search_dfs_pre_order(root.left, target)
    if left_result:
        return left_result

    # RIGHT - Recursively search in the right
    return search_dfs_pre_order(root.right, target)


print(search_dfs_pre_order(bt1.root, 0) != None)
print(search_dfs_pre_order(bt1.root, 100000) != None)