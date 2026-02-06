from binary_tree import BinaryTree

def print_bfs(root):
    """Print the tree level-by-level (Breadth-First Traversal)."""
    if not root:
        print("Tree is empty.")
        return

    queue = [root]
    while queue:
        current = queue.pop(0)

        # ---------------------------
        print(current.value, end=" ")
        # ---------------------------

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)


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
    # DFS traversal: A C G F B E D (depends on order, goes deep first)
    # -------------------

    bt = BinaryTree()
    bt.insert("A")
    bt.insert("B")
    bt.insert("C")
    bt.insert("D")
    bt.insert("E")
    bt.insert("F")
    bt.insert("G")

    # A B C D E F G
    print_bfs(bt.root)
