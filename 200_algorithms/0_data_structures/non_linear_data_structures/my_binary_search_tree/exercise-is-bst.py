# Hack to import module outside this project
import sys
from pathlib import Path
# Add the top-level directory to the Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Import the binary tree and binary search tree modules (placeholder imports)
from my_binary_tree.binary_tree import bt1
from binary_search_tree import bst1

# ---------------------------------------------
# TEST IF IT IS A Binary Search Tree (BST)
# ---------------------------------------------
def is_bst(node, left=None, right=None):
    # If the node is None, we've reached a leaf or an empty tree, return True
    if node is None:
        return True

    # Check if the current node's value violates the BST property
    if left is not None and node.value <= left.value:
        return False
    if right is not None and node.value >= right.value:
        return False

    # Recursively check the left and right subtrees
    return is_bst(node.left, left, node) and is_bst(node.right, node, right)

# Test with the binary search tree
result1 = is_bst(bst1.root)
print(f"is the tree a BST? {result1}")

# Test with a general binary tree
result2 = is_bst(bt1.root)
print(f"is the tree a BST? {result2}")
