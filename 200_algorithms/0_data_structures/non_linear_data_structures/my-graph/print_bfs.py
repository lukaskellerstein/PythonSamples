from graph import SimplestGraph

def bfs(graph, start):

    visited = set()
    visited.add(start)

    myq = []
    myq.append(start)

    while myq:
        curr = myq.pop(0)

        # ------------------------
        print(curr, end=" ")
        # ------------------------

        for neighbor in graph.adj_list.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                myq.append(neighbor)



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

    g = SimplestGraph()

    # Level 1
    g.add_edge("A", "B")
    g.add_edge("A", "C")

    # Level 2
    g.add_edge("B", "D")
    g.add_edge("B", "E")
    g.add_edge("C", "F")
    g.add_edge("C", "G")

    
    # A B C D E F G
    bfs(g, "A")
