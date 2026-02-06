
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
    print(root.val, end=" ")
    # RIGHT
    print_dfs_in_order(root.right)



# --------------------------------------------
# In-order traversal ITERATIVE (with STACK) = Left → Root → Right
# --------------------------------------------

def print_dfs_in_order_iterative(root):
    """Print the tree using In-order DFS traversal (iterative with stack)."""
    stack = []
    current = root

    while stack or current:
        # Go as far left as possible
        while current:
            stack.append(current)
            current = current.left

        # Process the node
        current = stack.pop()
        print(current.val, end=" ")

        # Move to right subtree
        current = current.right



# Example
if __name__ == "__main__":

    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    # -------------------
    #         A
    #        / \
    #       B   C
    #      / \ / \
    #     D  E F  G
    # -------------------

    root = TreeNode("A")
    root.left = TreeNode("B")
    root.right = TreeNode("C")
    root.left.left = TreeNode("D")
    root.left.right = TreeNode("E")
    root.right.left = TreeNode("F")
    root.right.right = TreeNode("G")

    # D B E A F C G
    print_dfs_in_order(root)

    print()  # newline

    # D B E A F C G
    print_dfs_in_order_iterative(root)
