from binary_tree import BinaryTree

bt1 = BinaryTree()
bt1.insert(3)
bt1.insert(4)
bt1.insert(5)
bt1.insert(1)
bt1.insert(2)
bt1.insert(0)
bt1.insert(9)
bt1.insert(10)

# ---------------------------------------------
# CONVERT TO SUM TREE - EASY
# ---------------------------------------------

def sum_tree(node):
    if node is None:
        return 0

    # Sum the current node's value and recursively sum the left and right subtrees
    return node.value + sum_tree(node.left) + sum_tree(node.right)


print(sum_tree(bt1.root))  # Output: 34