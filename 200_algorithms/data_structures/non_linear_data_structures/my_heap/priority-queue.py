# -------------------------------
# Priority Queue
# implemented using a List
#
# same as MinHeap,
# but instead of storing only value,
# we store a dictionary with { "value": ..., "priority": ... }
# -------------------------------

class PriorityQueue:
    def __init__(self):
        # Internal Min Heap to store elements
        self.heap = []

    # Get the index of the left child of a node
    def get_left_child_index(self, parent_index):
        return 2 * parent_index + 1

    # Get the index of the right child of a node
    def get_right_child_index(self, parent_index):
        return 2 * parent_index + 2

    # Get the index of the parent of a node
    def get_parent_index(self, child_index):
        return (child_index - 1) // 2

    # Enqueue a new element with a priority
    def enqueue(self, value, priority):
        # Add the element as a dictionary { "value": ..., "priority": ... }
        self.heap.append({"value": value, "priority": priority})
        # Bubble up to maintain heap order
        self.bubble_up(len(self.heap) - 1)

    # Dequeue the element with the highest priority (lowest priority value)
    def dequeue(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            # Only one element, remove and return it
            return self.heap.pop()["value"]

        # Remove the root element and replace it with the last element
        root = self.heap[0]["value"]
        self.heap[0] = self.heap.pop()
        # Bubble down to maintain heap order
        self.bubble_down(0)

        return root

    # Move a value up the tree until the heap property is restored
    def bubble_up(self, current_index):
        while current_index > 0:
            parent_index = self.get_parent_index(current_index)

            # Compare priorities; smaller priority means higher priority
            if self.heap[current_index]["priority"] < self.heap[parent_index]["priority"]:
                # Swap with parent
                self.heap[current_index], self.heap[parent_index] = (
                    self.heap[parent_index],
                    self.heap[current_index],
                )
                current_index = parent_index
            else:
                break

    # Move a value down the tree until the heap property is restored
    def bubble_down(self, current_index):
        smallest_index = current_index
        left_index = self.get_left_child_index(current_index)
        right_index = self.get_right_child_index(current_index)

        # Compare left child
        if (
            left_index < len(self.heap) and
            self.heap[left_index]["priority"] < self.heap[smallest_index]["priority"]
        ):
            smallest_index = left_index

        # Compare right child
        if (
            right_index < len(self.heap) and
            self.heap[right_index]["priority"] < self.heap[smallest_index]["priority"]
        ):
            smallest_index = right_index

        # Swap if needed and continue bubbling down
        if smallest_index != current_index:
            self.heap[current_index], self.heap[smallest_index] = (
                self.heap[smallest_index],
                self.heap[current_index],
            )
            self.bubble_down(smallest_index)


# Example usage:
pq = PriorityQueue()

# Enqueue elements with priorities
pq.enqueue("Task A", 3)  # Priority 3
pq.enqueue("Task B", 1)  # Priority 1 (highest priority)
pq.enqueue("Task C", 2)  # Priority 2

# Dequeue elements based on priority
print(pq.dequeue())  # Output: "Task B" (highest priority)
print(pq.dequeue())  # Output: "Task C"
print(pq.dequeue())  # Output: "Task A"
