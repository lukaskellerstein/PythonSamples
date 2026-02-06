# is_mirror_tree:
#   Time Complexity: O(n) - where n is the number of nodes in the smaller tree (visits each node once)
#   Space Complexity: O(h) - where h is the height of the tree (recursion stack), O(log n) balanced, O(n) skewed
#
# mirror_tree (convert):
#   Time Complexity: O(n) - visits every node once to swap children
#   Space Complexity: O(h) - where h is the height of the tree (recursion stack), O(log n) balanced, O(n) skewed

from binary_tree import BinaryTree
from helpers import visualize

# Create a new binary tree and insert values
tree1 = BinaryTree()
tree1.insert(3)
tree1.insert(4)
tree1.insert(5)
tree1.insert(1)
tree1.insert(2)
tree1.insert(0)
tree1.insert(9)
tree1.insert(10)

tree2 = BinaryTree()


# ---------------------------------------------
# CHECK IF IT IS A MIRROR TREE - EASY
# ---------------------------------------------
def is_mirror_tree(tree1, tree2):

    if tree1 is None and tree2 is None:
        return True
    
    if tree1 is None or tree2 is None:
        return False
    
    if tree1.value != tree2.value:
        return False
    

    leftRight = is_mirror_tree(tree1.left, tree2.right)
    rightLeft = is_mirror_tree(tree1.right, tree2.left)

    return leftRight and rightLeft

# Check if tree1 and tree2 are mirror images of each other
print(is_mirror_tree(tree1.root, tree2.root))  # true


# ---------------------------------------------
# CONVERT TO MIRROR TREE - EASY
# ---------------------------------------------
def mirror_tree(tree):
    if not tree:
        return None  # Base case: if the node is null, return

    # Recursively call for left and right children
    left = mirror_tree(tree.left)
    right = mirror_tree(tree.right)

    # Swap left and right children
    tree.left = right
    tree.right = left

    return tree

# Convert tree1 to its mirror and store the result in tree2
tree3Root = mirror_tree(tree1.root)
tree3 = BinaryTree()
tree3.root = tree3Root
visualize("mirror-tree", tree3.root)
