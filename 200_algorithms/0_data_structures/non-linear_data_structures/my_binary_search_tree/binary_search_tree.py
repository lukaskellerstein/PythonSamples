# --------------------------------------------------------
# BINARY SEARCH TREE
#
# also called an ordered or sorted binary tree 
#
# SORTED
#
# print methods and search methods are the same as in the binary tree
# BUT
# we can leverage the property of the binary search tree => faster search
# viz. search.py and search.md
# --------------------------------------------------------


# ------------------------------------------
# Node class 
# ------------------------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# ------------------------------------------
# Binary Search tree class 
# ------------------------------------------
class BinarySearchTree:
    def __init__(self):
        # root of a binary search tree
        self.root = None

    def insert(self, value):
        # Creating a node and initializing with data 
        new_node = TreeNode(value)

        # root is null then node will 
        # be added to the tree and made root.
        if self.root is None:
            self.root = new_node
        else:
            # find the correct position in the 
            # tree and add the node 
            self.insert_node(self.root, new_node)

    # Method to insert a node in a tree 
    # it moves over the tree to find the location 
    # to insert a node with a given data 
    def insert_node(self, node, new_node):
        # if the data is less than the node 
        # data move left of the tree 
        if new_node.value < node.value:
            # if left is null insert node here 
            if node.left is None:
                node.left = new_node
            else:
                # if left is not null recur until 
                # null is found 
                self.insert_node(node.left, new_node)

        # if the data is more than the node 
        # data move right of the tree 
        else:
            # if right is null insert node here 
            if node.right is None:
                node.right = new_node
            else:
                # if right is not null recur until 
                # null is found 
                self.insert_node(node.right, new_node)

    def remove(self, value):
        # root is re-initialized with 
        # root of a modified tree.
        self.root = self.remove_node(self.root, value)

    # Method to remove node with a 
    # given data 
    # it recur over the tree to find the 
    # data and removes it 
    def remove_node(self, node, value):
        # if the root is null then tree is empty
        if node is None:
            return node

        # if data to be deleted is less than 
        # root's data then move to left subtree 
        if value < node.value:
            node.left = self.remove_node(node.left, value)
            return node

        # if data to be deleted is greater than 
        # root's data then move to right subtree 
        elif value > node.value:
            node.right = self.remove_node(node.right, value)
            return node

        # if data is similar to the root's data 
        # then delete this node 
        else:
            # deleting node with no children 
            if node.left is None and node.right is None:
                node = None
                return node

            # deleting node with one child
            if node.left is None:
                node = node.right
                return node

            elif node.right is None:
                node = node.left
                return node

            # deleting node with two children 
            # minimum node of the right subtree is stored in aux
            aux = self.find_min_node(node.right)
            node.value = aux.value

            node.right = self.remove_node(node.right, aux.value)
            return node

    # Helper function 
    # finds the minimum node in tree 
    # searching starts from given node 
    def find_min_node(self, node):
        # if left of a node is null 
        # then it must be the minimum node 
        if node.left is None:
            return node
        else:
            return self.find_min_node(node.left)


# Example usage of the BinarySearchTree class
bst1 = BinarySearchTree()
bst1.insert(3)
bst1.insert(4)
bst1.insert(5)
bst1.insert(1)
bst1.insert(2)
bst1.insert(0)
bst1.insert(9)
bst1.insert(10)

