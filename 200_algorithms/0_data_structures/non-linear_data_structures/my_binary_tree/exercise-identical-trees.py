from binary_tree import BinaryTree

def are_identical(a, b):
    # 1. both trees are empty
    if a is None and b is None:
        return True

    # 2. one tree is empty or values are not the same
    if a is None or b is None or a.value != b.value:
        return False

    # 3. check left and right subtrees
    return are_identical(a.left, b.left) and are_identical(a.right, b.right)


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
