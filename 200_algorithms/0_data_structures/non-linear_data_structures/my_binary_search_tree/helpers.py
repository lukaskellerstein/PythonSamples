# from graphviz import Digraph

# def visualize(fileName, rootNode):
#     if not rootNode:
#         print("Tree is empty.")
#         return

#     # Use graphviz to create a visual representation of the tree
#     dot = Digraph(format='png')
#     _add_nodes(dot, rootNode)
#     dot.render(fileName, view=True)

# def _add_nodes(dot, node):
#     dot.node(str(node.value), str(node.value))

#     if node.left:
#         dot.edge(str(node.value), str(node.left.value))
#         _add_nodes(dot, node.left)

#     if node.right:
#         dot.edge(str(node.value), str(node.right.value))
#         _add_nodes(dot, node.right)


# -------------------------------
# Variant 2
# -------------------------------
# from graphviz import Digraph

# def visualize(fileName, rootNode):
#     if not rootNode:
#         print("Tree is empty.")
#         return

#     # Create a Digraph object with additional style customizations
#     dot = Digraph(format='png')
#     dot.attr('node', shape='circle', style='filled', color='lightblue', fontname='Helvetica')

#     _add_nodes(dot, rootNode)

#     # Render the tree visualization
#     dot.render(fileName, view=True)

# def _add_nodes(dot, node):
#     # Add the current node
#     dot.node(str(id(node)), str(node.value))

#     # Add left child
#     if node.left:
#         dot.edge(str(id(node)), str(id(node.left)), label='L', color='blue')
#         _add_nodes(dot, node.left)

#     # Add right child
#     if node.right:
#         dot.edge(str(id(node)), str(id(node.right)), label='R', color='red')
#         _add_nodes(dot, node.right)


# -------------------------------
# Variant 3
# -------------------------------
from graphviz import Digraph

def visualize(fileName, rootNode):
    """
    Visualizes a binary tree using Graphviz.
    
    Args:
        fileName (str): The output file name for the visualization.
        rootNode (TreeNode): The root node of the binary tree.
    """
    if not rootNode:
        print("Tree is empty.")
        return

    # Initialize Graphviz Digraph with node and edge styles
    dot = Digraph(format='png')
    dot.attr('node', shape='circle', style='filled', color='lightblue', fontname='Helvetica')

    # Recursively add nodes and edges to the graph
    _add_nodes(dot, rootNode)

    # Render the tree visualization
    dot.render(fileName, view=True)

def _add_nodes(dot, node):
    """
    Recursively adds nodes and edges to the Graphviz Digraph.

    Args:
        dot (Digraph): The Graphviz Digraph object.
        node (TreeNode): The current node to process.
    """
    # Use unique identifier for each node to handle duplicate values
    node_id = str(id(node))
    dot.node(node_id, str(node.value))

    # Add left child if it exists
    if node.left:
        left_id = str(id(node.left))
        dot.edge(node_id, left_id, label='L', color='blue')
        _add_nodes(dot, node.left)

    # Add right child if it exists
    if node.right:
        right_id = str(id(node.right))
        dot.edge(node_id, right_id, label='R', color='red')
        _add_nodes(dot, node.right)


