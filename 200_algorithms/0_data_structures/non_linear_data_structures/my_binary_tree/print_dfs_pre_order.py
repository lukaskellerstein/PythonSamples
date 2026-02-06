from binary_tree import BinaryTree

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



# Example: Create a tree to demonstrate BFS
if __name__ == "__main__":

    # -------------------
    # Create a tree to compare BFS vs DFS
    # -------------------
    #
    #         A
    #        / \
    #       B   C
    #      / \ / \
    #     D  E F  G
    #
    # BFS traversal: A B C D E F G (level by level)
    # -------------------

    bt = BinaryTree()
    bt.insert("A")
    bt.insert("B")
    bt.insert("C")
    bt.insert("D")
    bt.insert("E")
    bt.insert("F")
    bt.insert("G")

    # A B D E C F G
    print_dfs_pre_order(bt.root) 
