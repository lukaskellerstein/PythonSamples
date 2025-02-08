from binary_search_tree import bst1

# Search function for BST
def search_bst(node, value):
    # Base case: node is null or value is found
    if node is None:
        return None  # Value not found
    if node.value == value:
        return node  # Value found

    # Value is smaller, search in the left subtree
    if value < node.value:
        return search_bst(node.left, value)

    # Value is larger, search in the right subtree
    return search_bst(node.right, value)

print(search_bst(bst1.root, 0) != None)
print(search_bst(bst1.root, 100000) != None)