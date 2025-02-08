# -------------------------------
# Min Heap
# implemented using a List
# -------------------------------

class MyMinHeap:
    def __init__(self):
        # List representation of the heap
        self.arr = []

    # Get the index of the left child of a node
    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    # Get the index of the right child of a node
    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    # Get the index of the parent of a node
    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    # Insert a new value into the heap and maintain heap order
    def insert(self, value):
        # Add value to the end of the list
        self.arr.append(value)
        # Re-establish the heap property by bubbling the value up
        self.bubble_up(len(self.arr) - 1)

    # Remove a value from the heap
    def remove(self, value):
        if value not in self.arr:
            return  # Value not found

        # Find the index of the value to remove
        index = self.arr.index(value)

        # If the value is the last element, remove it directly
        if index == len(self.arr) - 1:
            self.arr.pop()
        else:
            # Replace the value with the last element and bubble down to maintain heap order
            self.arr[index] = self.arr.pop()
            self.bubble_down(index)

    # Move a value up the tree until the heap property is restored
    def bubble_up(self, current_index):
        while current_index > 0:
            # Find the parent of the current node
            parent_index = self.get_parent_index(current_index)

            # If the current value is smaller than the parent's value, swap them
            if self.arr[current_index] < self.arr[parent_index]:
                self.arr[current_index], self.arr[parent_index] = (
                    self.arr[parent_index],
                    self.arr[current_index],
                )
                # Continue bubbling up
                current_index = parent_index
            else:
                # Heap property is restored
                break

    # Move a value down the tree until the heap property is restored
    def bubble_down(self, current_index):
        # Get the indices of the left and right children
        left_index = self.get_left_child_index(current_index)
        right_index = self.get_right_child_index(current_index)

        # Start by assuming the current node is the smallest
        smallest_index = current_index

        # Check if the left child exists and is smaller than the current node
        if left_index < len(self.arr) and self.arr[left_index] < self.arr[smallest_index]:
            smallest_index = left_index  # Update smallest index to left child

        # Check if the right child exists and is smaller than the current smallest node
        if right_index < len(self.arr) and self.arr[right_index] < self.arr[smallest_index]:
            smallest_index = right_index  # Update smallest index to right child

        # If the smallest node is not the current node, swap and continue bubbling down
        if smallest_index != current_index:
            self.arr[current_index], self.arr[smallest_index] = (
                self.arr[smallest_index],
                self.arr[current_index],
            )
            # Recursively bubble down the swapped value
            self.bubble_down(smallest_index)

# Example usage:
my_heap = MyMinHeap()

# Insert values into the heap
my_heap.insert(1)
my_heap.insert(5)
my_heap.insert(3)
my_heap.insert(10)
my_heap.insert(4)

# Remove the smallest value (1) from the heap
my_heap.remove(1)

# Print the heap array
print(my_heap.arr)
