from binary_tree import BinaryTree

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

    # D E B F G C A
    print_dfs_post_order(bt.root)
