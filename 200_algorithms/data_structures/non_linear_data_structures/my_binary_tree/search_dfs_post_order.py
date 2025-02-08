from binary_tree import bt1

# --------------------------------------------
# Post-order traversal = Left → Right → Root
# --------------------------------------------

def search_dfs_post_order(root, target):
    """Search for a value using Depth-First Search (DFS) with Post-order traversal."""
    if not root:
        return None

    # LEFT - Search in the left subtree
    left_result = search_dfs_post_order(root.left, target)
    if left_result:
        return left_result

    # RIGHT - Search in the right subtree
    right_result = search_dfs_post_order(root.right, target)
    if right_result:
        return right_result

    # ROOT - Check the current node
    if root.value == target:
        return root

    return None

print(search_dfs_post_order(bt1.root, 0) != None)
print(search_dfs_post_order(bt1.root, 100000) != None)