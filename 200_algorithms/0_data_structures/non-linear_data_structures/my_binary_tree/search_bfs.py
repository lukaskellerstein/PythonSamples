from binary_tree import bt1

def search_bfs(root, target):
    """Search for a value using Breadth-First Search (BFS)."""
    if not root:
        return None

    queue = [root]
    while queue:
        current = queue.pop(0)
        if current.value == target:
            return current

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return None

print(search_bfs(bt1.root, 0) != None)
print(search_bfs(bt1.root, 100000) != None)
