
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
    print(root.val, end=" ")



# --------------------------------------------
# Post-order traversal ITERATIVE (with TWO STACKS) = Left → Right → Root
# --------------------------------------------

def print_dfs_post_order_iterative(root):
    """Print the tree using Post-order DFS traversal (iterative with two stacks)."""
    if not root:
        return

    stack1 = [root]
    stack2 = []

    # Build reverse post-order in stack2
    while stack1:
        node = stack1.pop()
        stack2.append(node)

        # Push left first so right is processed first
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # Print stack2 in reverse = post-order
    while stack2:
        print(stack2.pop().val, end=" ")



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

    # D E B F G C A
    print_dfs_post_order(root)

    print()  # newline

    # D E B F G C A
    print_dfs_post_order_iterative(root)
