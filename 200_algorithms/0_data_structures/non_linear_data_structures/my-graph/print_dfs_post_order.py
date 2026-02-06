from graph import SimplestGraph

def dfs_post_order(graph, start, visited=None):
    """Recursive implementation of post-order DFS traversal."""
    if visited is None:
        visited = set()

    if start in visited:
        return

    visited.add(start)

    # Recursively visit all neighbors first
    for neighbor in graph.adj_list.get(start, []):
        if neighbor not in visited:
            dfs_post_order(graph, neighbor, visited)

    # Print the current node after visiting all neighbors (post-order)
    print(start, end=" ")




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

    # D E B F G C A
    dfs_post_order(g, "A")
