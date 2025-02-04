from binary_tree import bt1

def print_bfs(root):
    """Print the tree level-by-level (Breadth-First Traversal)."""
    if not root:
        print("Tree is empty.")
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.value, end=" ")

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    print()

print_bfs(bt1.root)