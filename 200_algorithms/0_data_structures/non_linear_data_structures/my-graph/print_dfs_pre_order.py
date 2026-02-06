from graph import SimplestGraph

def dfs_pre_order(graph, start, visited=None):
    """Recursive implementation of pre-order DFS traversal."""
    if visited is None:
        visited = set()

    if start in visited:
        return

    visited.add(start)

    # Print the current node (pre-order = process node first)
    print(start, end=" ")

    # Recursively visit all neighbors
    for neighbor in graph.adj_list.get(start, []):
        if neighbor not in visited:
            dfs_pre_order(graph, neighbor, visited)


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

    g = SimplestGraph()

    # Level 1
    g.add_edge("A", "B")
    g.add_edge("A", "C")

    # Level 2
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "F")
    g.add_edge("C", "G")

    # A B D E C F G
    dfs_pre_order(g, "A")
