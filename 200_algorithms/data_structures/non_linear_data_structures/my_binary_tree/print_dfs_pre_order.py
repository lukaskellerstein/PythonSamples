from binary_tree import bt1

# --------------------------------------------
# Pre-order traversal = Root → Left → Right
# --------------------------------------------

def print_dfs_pre_order(root):
    """Print the tree using Pre-order DFS traversal."""
    if not root:
        return
    
    # ROOT
    print(root.value, end=" ")
    # LEFT
    print_dfs_pre_order(root.left)
    # RIGHT
    print_dfs_pre_order(root.right)

print_dfs_pre_order(bt1.root)