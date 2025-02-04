from binary_tree import bt1

# --------------------------------------------
# In-order traversal = Left → Root → Right
# --------------------------------------------

def print_dfs_in_order(root):
    """Print the tree using In-order DFS traversal."""
    if not root:
        return
    
    # LEFT
    print_dfs_in_order(root.left)
    # ROOT
    print(root.value, end=" ")
    # RIGHT
    print_dfs_in_order(root.right)


print_dfs_in_order(bt1.root)