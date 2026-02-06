# Node class to represent each element in the linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# LinkedList class to manage the list
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a new node at the beginning
    def insert_at_head(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # Insert a new node at the end
    def insert_at_end(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Delete a node with a specific value
    def delete(self, value):
        if not self.head:
            return

        # If the node to delete is the head
        if self.head.value == value:
            self.head = self.head.next
            return

        # Find the node to delete
        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        # If the node was found, unlink it
        if current.next:
            current.next = current.next.next

    # Display the entire list
    def display(self):
        current = self.head
        output = []
        while current:
            output.append(str(current.value))
            current = current.next
        print(" -> ".join(output) + " -> None")

# Example usage:
list = LinkedList()
list.insert_at_head(10)
list.insert_at_head(5)
list.insert_at_end(20)
list.display()  # Output: 5 -> 10 -> 20 -> None

list.delete(10)
list.display()  # Output: 5 -> 20 -> None
