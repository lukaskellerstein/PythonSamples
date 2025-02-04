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
tree2Root = mirror_tree(tree1.root)
tree2 = BinaryTree()
tree2.root = tree2Root
visualize("mirror-tree", tree2.root)

# ---------------------------------------------
# CHECK IF IT IS A MIRROR TREE
# ---------------------------------------------
def check_if_mirror_tree(tree1, tree2):
    if not tree1 and not tree2:
        return True  # Both trees are null, so they are mirrors
    if not tree1 or not tree2:
        return False  # One is null and the other isn't

    # Values must match and mirrored subtrees must also match
    return (
        tree1.value == tree2.value and
        check_if_mirror_tree(tree1.left, tree2.right) and
        check_if_mirror_tree(tree1.right, tree2.left)
    )

# Check if tree1 and tree2 are mirror images of each other
print(check_if_mirror_tree(tree1.root, tree2.root))  # true
