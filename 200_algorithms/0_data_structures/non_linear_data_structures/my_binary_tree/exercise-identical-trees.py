# Time Complexity: O(n) - where n is the number of nodes in the smaller tree (visits each node once)
# Space Complexity: O(h) - where h is the height of the tree (recursion stack), O(log n) balanced, O(n) skewed

from binary_tree import BinaryTree

def are_identical(tree1, tree2):

    if tree1 is None and tree2 is None:
        return True
    
    if tree1 is None or tree2 is None:
        return False
    
    if tree1.value != tree2.value:
        return False

    left = are_identical(tree1.left, tree2.left)
    right = are_identical(tree1.right, tree2.right)

    return left and right


# First tree
tree1 = BinaryTree()
tree1.insert(3)
tree1.insert(4)
tree1.insert(5)
tree1.insert(1)
tree1.insert(2)
tree1.insert(0)
tree1.insert(9)
tree1.insert(10)

# Second tree
tree2 = BinaryTree()
tree2.insert(3)
tree2.insert(4)
tree2.insert(5)
tree2.insert(1)
tree2.insert(2)
tree2.insert(0)

# TEST
print(are_identical(tree1.root, tree2.root))  # Output: False
