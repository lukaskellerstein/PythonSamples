
# --------------------------------------------
# Pre-order traversal = Root → Left → Right
# --------------------------------------------

def print_dfs_pre_order(root):
    """Print the tree using Pre-order DFS traversal."""
    if not root:
        return

    # ROOT
    print(root.val, end=" ")
    # LEFT
    print_dfs_pre_order(root.left)
    # RIGHT
    print_dfs_pre_order(root.right)



# --------------------------------------------
# Pre-order traversal ITERATIVE (with STACK) = Root → Left → Right
# --------------------------------------------

def print_dfs_pre_order_iterative(root):
    """Print the tree using Pre-order DFS traversal (iterative with stack)."""
    if not root:
        return

    stack = [root]

    while stack:
        # Process the node
        node = stack.pop()
        print(node.val, end=" ")

        # Push right first so left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)



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

    # A B D E C F G
    print_dfs_pre_order(root)

    print()  # newline

    # A B D E C F G
    print_dfs_pre_order_iterative(root)
