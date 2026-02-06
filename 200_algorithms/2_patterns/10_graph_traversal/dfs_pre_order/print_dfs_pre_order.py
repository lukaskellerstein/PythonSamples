
# --------------------------------------------
# DFS Pre-order traversal (with RECURSION)
# --------------------------------------------

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
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs_pre_order(graph, neighbor, visited)


# --------------------------------------------
# DFS Pre-order traversal ITERATIVE (with STACK)
# --------------------------------------------

def dfs_pre_order_iterative(graph, start):
    """Iterative implementation of pre-order DFS traversal using a stack."""
    visited = set()
    stack = [start]

    while stack:
        curr = stack.pop()

        if curr in visited:
            continue

        visited.add(curr)

        # Print the current node (pre-order = process node first)
        print(curr, end=" ")

        # Push neighbors in reverse order so first neighbor is processed first
        for neighbor in reversed(graph.get(curr, [])):
            if neighbor not in visited:
                stack.append(neighbor)



# Example
if __name__ == "__main__":

    # -------------------
    #         A
    #        / \
    #       B   C
    #      / \ / \
    #     D  E F  G
    #
    # BFS traversal: A B C D E F G (level by level)
    # DFS traversal: A B D E C F G (goes deep first)
    # -------------------

    graph = {
        "A": ["B", "C"],
        "B": ["A", "D", "E"],
        "C": ["A", "F", "G"],
        "D": ["B"],
        "E": ["B"],
        "F": ["C"],
        "G": ["C"],
    }

    # A B D E C F G
    dfs_pre_order(graph, "A")

    print()  # newline

    # A B D E C F G
    dfs_pre_order_iterative(graph, "A")
