from binary_tree import bt1

# --------------------------------------------
# Post-order traversal = Left → Right → Root
# --------------------------------------------

def print_dfs_post_order(root):
    """Print the tree using Post-order DFS traversal."""
    if not root:
        return
    
    # LEFT
    print_dfs_post_order(root.left)
    # RIGHT
    print_dfs_post_order(root.right)
    # ROOT
    print(root.value, end=" ")

print_dfs_post_order(bt1.root)