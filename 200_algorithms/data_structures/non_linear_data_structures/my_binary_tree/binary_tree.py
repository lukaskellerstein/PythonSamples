from helpers import visualize


# --------------------------------------------------------
# BINARY TREE
#
# binary tree is a tree data structure
# in which each node has at most two children
#
# Insert = BFS - Breadth First Search (Or Level Order Traversal)
# Remove = BFS - Breadth First Search (Or Level Order Traversal)
#
# --------------------------------------------------------


# ------------------------------------------
# Node class 
# ------------------------------------------
class TreeNode:
    # ------------------------------------------
    # Node class
    # ------------------------------------------
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Queue:
    def __init__(self):
        self.arr = []

    def enqueue(self, item):
        self.arr.append(item)

    def dequeue(self):
        return self.arr.pop(0)

    def is_empty(self):
        return len(self.arr) == 0

    def size(self):
        return len(self.arr)


class BinaryTree:
    # ------------------------------------------
    # Binary tree class
    # ------------------------------------------
    def __init__(self):
        # root of a binary search tree
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return

        # --------------------------------
        # BFS - Breadth First Search (Or Level Order Traversal)
        # does not make sense to use DFS
        # => we want to keep tree balanced and complete !!!
        # --------------------------------
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            current_node = queue.dequeue()

            if not current_node.left:
                current_node.left = TreeNode(value)
                break
            else:
                queue.enqueue(current_node.left)

            if not current_node.right:
                current_node.right = TreeNode(value)
                break
            else:
                queue.enqueue(current_node.right)

    def remove(self, value):
        if not self.root:
            return

        if not self.root.left and not self.root.right:
            if self.root.value == value:
                self.root = None
            return

        # --------------------------------
        # BFS - Breadth First Search (Or Level Order Traversal)
        # does not make sense to use DFS
        # => we want to keep tree balanced and complete !!!
        # --------------------------------
        queue = Queue()
        queue.enqueue(self.root)

        first_node = None
        value_node = None

        while not queue.is_empty():
            first_node = queue.dequeue()

            if first_node.value == value:
                value_node = first_node

            if first_node.left:
                queue.enqueue(first_node.left)

            if first_node.right:
                queue.enqueue(first_node.right)

        if value_node:
            x = first_node.value
            self.remove_node(first_node)
            value_node.value = x

    def remove_node(self, del_node):
        # --------------------------------
        # BFS - Breadth First Search (Or Level Order Traversal)
        # does not make sense to use DFS
        # => we want to keep tree balanced and complete !!!
        # --------------------------------
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            temp = queue.dequeue()

            if temp.left:
                if temp.left == del_node:
                    temp.left = None
                    return
                else:
                    queue.enqueue(temp.left)

            if temp.right:
                if temp.right == del_node:
                    temp.right = None
                    return
                else:
                    queue.enqueue(temp.right)


# Example usage of the BinaryTree class
bt1 = BinaryTree()
bt1.insert(3)
bt1.insert(4)
bt1.insert(5)
bt1.insert(1)
bt1.insert(2)
bt1.insert(0)
bt1.insert(9)
bt1.insert(10)