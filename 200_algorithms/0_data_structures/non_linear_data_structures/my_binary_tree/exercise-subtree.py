# Time Complexity: O(n * m) - for each of the n nodes in the main tree, we may compare all m nodes of the subtree
# Space Complexity: O(h) - where h is the height of the main tree (recursion stack), O(log n) balanced, O(n) skewed

from binary_tree import BinaryTree

def are_identical(a, b):
    # 1. both trees are empty
    if a is None and b is None:
        return True

    # 2. one tree is empty or values are not the same
    if a is None or b is None or a.value != b.value:
        return False

    # 3. check if left and right subtrees are identical
    return are_identical(a.left, b.left) and are_identical(a.right, b.right)


def is_subtree(tree, subtree):
    # If the subtree is empty, it is always a subtree
    if subtree is None:
        return True

    # If the main tree is empty but the subtree is not, it's not a subtree
    if tree is None:
        return False

    # Check if the trees are identical starting from the current node
    if are_identical(tree, subtree):
        return True

    # Otherwise, recursively check the left and right subtrees
    return is_subtree(tree.left, subtree) or is_subtree(tree.right, subtree)


# Example usage:

# Create first tree (tree1)
tree1 = BinaryTree()
tree1.insert(4)
tree1.insert(1)
tree1.insert(2)
tree1.insert(10)

# Create second tree (tree2)
tree2 = BinaryTree()
tree2.insert(3)
tree2.insert(4)
tree2.insert(5)
tree2.insert(1)
tree2.insert(2)
tree2.insert(0)
tree2.insert(9)
tree2.insert(10)

# Check if tree1 is a subtree of tree2
print(is_subtree(tree2.root, tree1.root))  # Output: True or False depending on tree structure
