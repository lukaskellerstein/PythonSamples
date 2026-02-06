
# Simplest graph structure

# The simplest graph = DIRECTED (DAG, only one direction)
class SimplestGraph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        self.adj_list[u].append(v)       


if __name__ == "__main__":

    mygraph = SimplestGraph()

    mygraph.add_node("A")
    mygraph.add_node("B")
    mygraph.add_node("C")
    mygraph.add_node("D")

    mygraph.add_edge("A", "B")
    mygraph.add_edge("B", "C")
    mygraph.add_edge("C", "D")

    # A -> B -> C -> D
    print("A -> B -> C -> D")




# The simplest graph = UNDIRECTED (Each edge goes both directions)
class SimplestGraph2:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, u, v):
        self.add_node(u)
        self.add_node(v)
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) # <----------------- aditional edge


if __name__ == "__main__":

    mygraph = SimplestGraph2()

    mygraph.add_node("A")
    mygraph.add_node("B")
    mygraph.add_node("C")
    mygraph.add_node("D")

    mygraph.add_edge("A", "B")
    mygraph.add_edge("B", "C")
    mygraph.add_edge("C", "D")

    # A <-> B <-> C <-> D
    print("A <-> B <-> C <-> D")
