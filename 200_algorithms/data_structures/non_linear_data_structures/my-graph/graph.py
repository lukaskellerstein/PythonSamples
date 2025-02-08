# Define a Graph class
class Graph:
    # Initialize the graph with the number of vertices and an adjacency list
    def __init__(self, no_of_vertices):
        self.no_of_vertices = no_of_vertices
        self.adj_list = {}

    # Add a vertex to the graph
    def add_vertex(self, v):
        # Initialize the adjacency list for the vertex with an empty list
        self.adj_list[v] = []

    # Add an edge to the graph
    def add_edge(self, v, w):
        # Add vertex w to the adjacency list of vertex v
        self.adj_list[v].append(w)

        # Since the graph is undirected, add vertex v to the adjacency list of vertex w
        self.adj_list[w].append(v)

    # Print the graph's vertices and adjacency lists
    def print_graph(self):
        # Iterate over all vertices in the adjacency list
        for vertex in self.adj_list:
            # Get the adjacency list for the current vertex
            adj_vertices = self.adj_list[vertex]
            # Create a string representation of the adjacency list
            adj_string = " ".join(adj_vertices)
            # Print the vertex and its adjacency list
            print(f"{vertex} -> {adj_string}")


# Using the Graph class

# Create a graph with 6 vertices
g = Graph(6)

# Define the vertices
vertices = ['A', 'B', 'C', 'D', 'E', 'F']

# Add the vertices to the graph
for vertex in vertices:
    g.add_vertex(vertex)

# Add edges to the graph
g.add_edge('A', 'B')
g.add_edge('A', 'D')
g.add_edge('A', 'E')
g.add_edge('B', 'C')
g.add_edge('D', 'E')
g.add_edge('E', 'F')
g.add_edge('E', 'C')
g.add_edge('C', 'F')

# Print all vertices and their adjacency lists
# Expected output:
# A -> B D E
# B -> A C
# C -> B E F
# D -> A E
# E -> A D F C
# F -> E C
g.print_graph()
