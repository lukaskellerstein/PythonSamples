
from collections import deque

# --------------------------------------------
# BFS traversal (iterative with QUEUE)
# --------------------------------------------

def bfs(graph, start):
    visited = set()
    visited.add(start)

    queue = deque([start])

    while queue:
        curr = queue.popleft()

        # ------------------------
        print(curr, end=" ")
        # ------------------------

        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)



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

    # A B C D E F G
    bfs(graph, "A")
