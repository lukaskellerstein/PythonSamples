from binary_tree import BinaryTree

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

    # D B E A F C G
    print_dfs_in_order(bt.root)

