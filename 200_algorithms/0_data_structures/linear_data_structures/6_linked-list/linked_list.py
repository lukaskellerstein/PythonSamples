# ----------------------------------
# ----------------------------------
# LINKED LIST
# A linked list is a linear data structure where elements (nodes) are not stored
# in contiguous memory locations. Each node contains data and a reference (link)
# to the next node. Unlike arrays/lists, linked lists don't support random access
# but excel at insertions/deletions when you have a reference to the location.
# ----------------------------------
# ----------------------------------

# Types of Linked Lists:
# 1. Singly Linked List: Each node points to the next node
# 2. Doubly Linked List: Each node points to both next and previous nodes
# 3. Circular Linked List: Last node points back to the first node

# ----------------------------------
# SINGLY LINKED LIST - NODE DEFINITION
# ----------------------------------

class Node:
    """Node for Singly Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


# ----------------------------------
# SINGLY LINKED LIST - IMPLEMENTATION
# ----------------------------------

class SinglyLinkedList:
    """Singly Linked List with head pointer"""

    def __init__(self):
        self.head = None
        self.size = 0

    # ----------------------------------
    # BASIC OPERATIONS
    # ----------------------------------

    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None

    def get_size(self):
        """Get size of list - O(1) since we track it"""
        return self.size

    def __len__(self):
        """Enable len(list) - O(1)"""
        return self.size

    # ----------------------------------
    # INSERTION OPERATIONS
    # ----------------------------------

    def insert_at_beginning(self, data):
        """Insert at the beginning - O(1)"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insert_at_end(self, data):
        """Insert at the end - O(n) without tail pointer"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.size += 1
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node
        self.size += 1

    def insert_at_position(self, data, position):
        """Insert at specific position (0-indexed) - O(n)"""
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head

        for _ in range(position - 1):
            current = current.next

        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def insert_after_node(self, prev_node, data):
        """Insert after a given node - O(1) if you have the node reference"""
        if prev_node is None:
            raise ValueError("Previous node cannot be None")

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.size += 1

    # ----------------------------------
    # DELETION OPERATIONS
    # ----------------------------------

    def delete_at_beginning(self):
        """Delete first node - O(1)"""
        if self.head is None:
            raise IndexError("Delete from empty list")

        deleted_data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return deleted_data

    def delete_at_end(self):
        """Delete last node - O(n)"""
        if self.head is None:
            raise IndexError("Delete from empty list")

        if self.head.next is None:
            deleted_data = self.head.data
            self.head = None
            self.size -= 1
            return deleted_data

        current = self.head
        while current.next.next:
            current = current.next

        deleted_data = current.next.data
        current.next = None
        self.size -= 1
        return deleted_data

    def delete_at_position(self, position):
        """Delete node at specific position (0-indexed) - O(n)"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")

        if position == 0:
            return self.delete_at_beginning()

        current = self.head
        for _ in range(position - 1):
            current = current.next

        deleted_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return deleted_data

    def delete_by_value(self, value):
        """Delete first node with given value - O(n)"""
        if self.head is None:
            raise ValueError("Value not found in list")

        if self.head.data == value:
            return self.delete_at_beginning()

        current = self.head
        while current.next and current.next.data != value:
            current = current.next

        if current.next is None:
            raise ValueError("Value not found in list")

        deleted_data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return deleted_data

    # ----------------------------------
    # SEARCH OPERATIONS
    # ----------------------------------

    def search(self, value):
        """Search for value, return True if found - O(n)"""
        current = self.head
        while current:
            if current.data == value:
                return True
            current = current.next
        return False

    def find_node(self, value):
        """Find and return the node containing value - O(n)"""
        current = self.head
        while current:
            if current.data == value:
                return current
            current = current.next
        return None

    def get_at_position(self, position):
        """Get data at specific position (0-indexed) - O(n)"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")

        current = self.head
        for _ in range(position):
            current = current.next

        return current.data

    # ----------------------------------
    # TRAVERSAL AND DISPLAY
    # ----------------------------------

    def display(self):
        """Display the list - O(n)"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements) + " -> None"

    def __str__(self):
        """String representation"""
        return self.display()

    def to_list(self):
        """Convert to Python list - O(n)"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def __iter__(self):
        """Make the list iterable"""
        current = self.head
        while current:
            yield current.data
            current = current.next

    # ----------------------------------
    # ADVANCED OPERATIONS
    # ----------------------------------

    def reverse(self):
        """Reverse the linked list in place - O(n)"""
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev

    def get_middle(self):
        """Get middle element using slow/fast pointer - O(n)"""
        if self.head is None:
            return None

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data

    def detect_cycle(self):
        """Detect if list has a cycle using Floyd's algorithm - O(n)"""
        if self.head is None:
            return False

        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False

    def remove_duplicates(self):
        """Remove duplicates from sorted list - O(n)"""
        current = self.head

        while current and current.next:
            if current.data == current.next.data:
                current.next = current.next.next
                self.size -= 1
            else:
                current = current.next

    def remove_duplicates_unsorted(self):
        """Remove duplicates from unsorted list - O(n) with O(n) space"""
        if self.head is None:
            return

        seen = set()
        current = self.head
        seen.add(current.data)
        prev = current

        while current.next:
            if current.next.data in seen:
                current.next = current.next.next
                self.size -= 1
            else:
                seen.add(current.next.data)
                current = current.next

    def clear(self):
        """Clear the entire list - O(1)"""
        self.head = None
        self.size = 0


# ----------------------------------
# DOUBLY LINKED LIST - NODE DEFINITION
# ----------------------------------

class DoublyNode:
    """Node for Doubly Linked List"""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return f"DoublyNode({self.data})"


# ----------------------------------
# DOUBLY LINKED LIST - IMPLEMENTATION
# ----------------------------------

class DoublyLinkedList:
    """Doubly Linked List with head and tail pointers"""

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # ----------------------------------
    # BASIC OPERATIONS
    # ----------------------------------

    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None

    def get_size(self):
        """Get size of list - O(1)"""
        return self.size

    def __len__(self):
        """Enable len(list) - O(1)"""
        return self.size

    # ----------------------------------
    # INSERTION OPERATIONS
    # ----------------------------------

    def insert_at_beginning(self, data):
        """Insert at the beginning - O(1)"""
        new_node = DoublyNode(data)

        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def insert_at_end(self, data):
        """Insert at the end - O(1) with tail pointer"""
        new_node = DoublyNode(data)

        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1

    def insert_at_position(self, data, position):
        """Insert at specific position (0-indexed) - O(n)"""
        if position < 0 or position > self.size:
            raise IndexError("Position out of bounds")

        if position == 0:
            self.insert_at_beginning(data)
            return

        if position == self.size:
            self.insert_at_end(data)
            return

        new_node = DoublyNode(data)
        current = self.head

        for _ in range(position - 1):
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        current.next.prev = new_node
        current.next = new_node
        self.size += 1

    # ----------------------------------
    # DELETION OPERATIONS
    # ----------------------------------

    def delete_at_beginning(self):
        """Delete first node - O(1)"""
        if self.head is None:
            raise IndexError("Delete from empty list")

        deleted_data = self.head.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

        self.size -= 1
        return deleted_data

    def delete_at_end(self):
        """Delete last node - O(1) with tail pointer"""
        if self.tail is None:
            raise IndexError("Delete from empty list")

        deleted_data = self.tail.data

        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return deleted_data

    def delete_at_position(self, position):
        """Delete node at specific position (0-indexed) - O(n)"""
        if position < 0 or position >= self.size:
            raise IndexError("Position out of bounds")

        if position == 0:
            return self.delete_at_beginning()

        if position == self.size - 1:
            return self.delete_at_end()

        current = self.head
        for _ in range(position):
            current = current.next

        deleted_data = current.data
        current.prev.next = current.next
        current.next.prev = current.prev
        self.size -= 1
        return deleted_data

    # ----------------------------------
    # TRAVERSAL AND DISPLAY
    # ----------------------------------

    def display_forward(self):
        """Display the list forward - O(n)"""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " <-> ".join(elements) + " <-> None"

    def display_backward(self):
        """Display the list backward - O(n)"""
        elements = []
        current = self.tail
        while current:
            elements.append(str(current.data))
            current = current.prev
        return " <-> ".join(elements) + " <-> None"

    def __str__(self):
        """String representation"""
        return self.display_forward()

    def __iter__(self):
        """Make the list iterable (forward)"""
        current = self.head
        while current:
            yield current.data
            current = current.next

    def reverse_iter(self):
        """Iterate backward"""
        current = self.tail
        while current:
            yield current.data
            current = current.prev

    # ----------------------------------
    # ADVANCED OPERATIONS
    # ----------------------------------

    def reverse(self):
        """Reverse the doubly linked list in place - O(n)"""
        current = self.head
        self.head, self.tail = self.tail, self.head

        while current:
            current.prev, current.next = current.next, current.prev
            current = current.prev  # Move to next (which is now prev)


# ----------------------------------
# CIRCULAR LINKED LIST
# ----------------------------------

class CircularLinkedList:
    """Circular Singly Linked List"""

    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        """Check if list is empty - O(1)"""
        return self.head is None

    def insert_at_beginning(self, data):
        """Insert at the beginning - O(n) to find last node"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            # Find last node
            current = self.head
            while current.next != self.head:
                current = current.next

            new_node.next = self.head
            current.next = new_node
            self.head = new_node

        self.size += 1

    def insert_at_end(self, data):
        """Insert at the end - O(n)"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next

            current.next = new_node
            new_node.next = self.head

        self.size += 1

    def display(self):
        """Display circular list - O(n)"""
        if self.head is None:
            return "Empty"

        elements = []
        current = self.head

        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break

        return " -> ".join(elements) + " -> (back to head)"

    def __str__(self):
        return self.display()


# ----------------------------------
# COMMON LINKED LIST PATTERNS AND ALGORITHMS
# ----------------------------------

# 1. Reverse a Linked List (Iterative)
def reverse_list_iterative(head):
    """Reverse linked list iteratively - O(n) time, O(1) space"""
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

# 2. Reverse a Linked List (Recursive)
def reverse_list_recursive(head):
    """Reverse linked list recursively - O(n) time, O(n) space"""
    if head is None or head.next is None:
        return head

    new_head = reverse_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return new_head

# 3. Find Middle Element (Slow/Fast Pointer)
def find_middle(head):
    """Find middle element - O(n) time, O(1) space"""
    if head is None:
        return None

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

# 4. Detect Cycle (Floyd's Cycle Detection)
def has_cycle(head):
    """Detect cycle in linked list - O(n) time, O(1) space"""
    if head is None:
        return False

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False

# 5. Find Cycle Start Node
def detect_cycle_start(head):
    """Find where cycle starts - O(n) time, O(1) space"""
    if head is None:
        return None

    slow = fast = head
    has_cycle = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            has_cycle = True
            break

    if not has_cycle:
        return None

    # Reset slow to head, move both one step at a time
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow

# 6. Merge Two Sorted Lists
def merge_sorted_lists(l1, l2):
    """Merge two sorted linked lists - O(n + m) time, O(1) space"""
    dummy = Node(0)
    current = dummy

    while l1 and l2:
        if l1.data <= l2.data:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 if l1 else l2
    return dummy.next

# 7. Remove Nth Node From End
def remove_nth_from_end(head, n):
    """Remove nth node from end - O(n) time, O(1) space"""
    dummy = Node(0)
    dummy.next = head
    fast = slow = dummy

    # Move fast n+1 steps ahead
    for _ in range(n + 1):
        if fast is None:
            return head
        fast = fast.next

    # Move both until fast reaches end
    while fast:
        fast = fast.next
        slow = slow.next

    # Remove the node
    slow.next = slow.next.next
    return dummy.next

# 8. Find Intersection of Two Lists
def get_intersection_node(headA, headB):
    """Find intersection node of two lists - O(n + m) time, O(1) space"""
    if not headA or not headB:
        return None

    # Get lengths
    lenA = lenB = 0
    tempA, tempB = headA, headB

    while tempA:
        lenA += 1
        tempA = tempA.next
    while tempB:
        lenB += 1
        tempB = tempB.next

    # Align starting points
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Find intersection
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None

# 9. Palindrome Check
def is_palindrome(head):
    """Check if linked list is palindrome - O(n) time, O(1) space"""
    if not head or not head.next:
        return True

    # Find middle
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    # Reverse second half
    prev = None
    while slow:
        next_node = slow.next
        slow.next = prev
        prev = slow
        slow = next_node

    # Compare both halves
    left, right = head, prev
    while right:
        if left.data != right.data:
            return False
        left = left.next
        right = right.next

    return True

# 10. Add Two Numbers (represented as linked lists)
def add_two_numbers(l1, l2):
    """Add two numbers represented as linked lists - O(max(n, m))"""
    dummy = Node(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        current.next = Node(total % 10)

        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next

# 11. Rotate List
def rotate_right(head, k):
    """Rotate list to the right by k places - O(n)"""
    if not head or not head.next or k == 0:
        return head

    # Find length and last node
    length = 1
    old_tail = head
    while old_tail.next:
        old_tail = old_tail.next
        length += 1

    # Calculate actual rotations needed
    k = k % length
    if k == 0:
        return head

    # Find new tail (length - k - 1)th node
    new_tail = head
    for _ in range(length - k - 1):
        new_tail = new_tail.next

    # Perform rotation
    new_head = new_tail.next
    new_tail.next = None
    old_tail.next = head

    return new_head

# 12. Partition List
def partition(head, x):
    """Partition list around value x - O(n)"""
    before_head = before = Node(0)
    after_head = after = Node(0)

    while head:
        if head.data < x:
            before.next = head
            before = before.next
        else:
            after.next = head
            after = after.next
        head = head.next

    after.next = None
    before.next = after_head.next

    return before_head.next

# 13. Sort List (Merge Sort)
def sort_list(head):
    """Sort linked list using merge sort - O(n log n) time, O(log n) space"""
    if not head or not head.next:
        return head

    # Find middle
    slow = fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Split list
    prev.next = None

    # Recursively sort both halves
    left = sort_list(head)
    right = sort_list(slow)

    # Merge sorted halves
    return merge_sorted_lists(left, right)

# 14. Remove Duplicates from Sorted List
def delete_duplicates(head):
    """Remove duplicates from sorted list - O(n)"""
    current = head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head

# 15. Copy List with Random Pointer
class RandomNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def copy_random_list(head):
    """Deep copy list with random pointers - O(n) time, O(n) space"""
    if not head:
        return None

    # Create copy nodes
    mapping = {}
    current = head
    while current:
        mapping[current] = RandomNode(current.data)
        current = current.next

    # Set next and random pointers
    current = head
    while current:
        if current.next:
            mapping[current].next = mapping[current.next]
        if current.random:
            mapping[current].random = mapping[current.random]
        current = current.next

    return mapping[head]


# ----------------------------------
# PRACTICAL USE CASES
# ----------------------------------

# 1. Implementing Undo/Redo
class UndoRedoList:
    """Undo/Redo using doubly linked list"""
    def __init__(self):
        self.dll = DoublyLinkedList()
        self.current = None

    def add_action(self, action):
        if self.current:
            # Remove all actions after current
            self.current.next = None
        self.dll.insert_at_end(action)

    def undo(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.data
        return None

    def redo(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.data
        return None

# 2. LRU Cache
class LRUCache:
    """LRU Cache using doubly linked list + hash map"""
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key -> node
        self.dll = DoublyLinkedList()

    def get(self, key):
        if key not in self.cache:
            return -1
        # Move to front (most recently used)
        node = self.cache[key]
        self.dll.delete_at_position(node.position)
        self.dll.insert_at_beginning(node.data)
        return node.data

    def put(self, key, value):
        if key in self.cache:
            self.dll.delete_at_position(self.cache[key].position)

        if len(self.cache) >= self.capacity:
            # Remove least recently used (from end)
            removed = self.dll.delete_at_end()
            del self.cache[removed]

        self.dll.insert_at_beginning(value)
        self.cache[key] = self.dll.head

# 3. Music Playlist (Circular List)
class MusicPlaylist:
    """Circular playlist implementation"""
    def __init__(self):
        self.playlist = CircularLinkedList()
        self.current = None

    def add_song(self, song):
        self.playlist.insert_at_end(song)
        if self.current is None:
            self.current = self.playlist.head

    def next_song(self):
        if self.current:
            self.current = self.current.next
            return self.current.data
        return None

    def previous_song(self):
        if self.current:
            # Find previous in circular list
            temp = self.current
            while temp.next != self.current:
                temp = temp.next
            self.current = temp
            return self.current.data
        return None


# ----------------------------------
# PERFORMANCE COMPARISON: LINKED LIST vs ARRAY/LIST
# ----------------------------------

# TIME COMPLEXITY COMPARISON:
# Operation              | Array/List | Linked List (Singly) | Linked List (Doubly)
# -----------------------|------------|----------------------|---------------------
# Access by index        | O(1)       | O(n)                 | O(n)
# Search                 | O(n)       | O(n)                 | O(n)
# Insert at beginning    | O(n)       | O(1)                 | O(1)
# Insert at end          | O(1)*      | O(n) or O(1)**       | O(1)
# Insert at middle       | O(n)       | O(n)***              | O(n)***
# Delete at beginning    | O(n)       | O(1)                 | O(1)
# Delete at end          | O(1)       | O(n)                 | O(1)
# Delete at middle       | O(n)       | O(n)***              | O(n)***
#
# * Amortized O(1) due to occasional resizing
# ** O(1) if tail pointer is maintained
# *** O(1) if you have a reference to the node

# SPACE COMPLEXITY:
# - Array/List: O(n) contiguous memory
# - Linked List: O(n) but with extra space for pointers

# USE LINKED LISTS WHEN:
# ✓ Frequent insertions/deletions at beginning
# ✓ Frequent insertions/deletions in middle (if you have node reference)
# ✓ Don't know size in advance
# ✓ Don't need random access
# ✓ Memory fragmentation is concern (no need for contiguous memory)
# ✓ Implementing advanced data structures (queues, stacks, graphs)

# USE ARRAYS/LISTS WHEN:
# ✓ Need random access by index
# ✓ Frequent access operations
# ✓ Memory locality is important (cache-friendly)
# ✓ Size is relatively stable
# ✓ Simpler code and less memory overhead
# ✓ Most common choice in Python due to dynamic arrays


# ----------------------------------
# EXAMPLE USAGE
# ----------------------------------

if __name__ == "__main__":
    # Singly Linked List Example
    print("=== Singly Linked List ===")
    sll = SinglyLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_beginning(0)
    print(sll)  # 0 -> 1 -> 2 -> 3 -> None

    sll.delete_by_value(2)
    print(sll)  # 0 -> 1 -> 3 -> None

    print(f"Middle element: {sll.get_middle()}")  # 1

    # Doubly Linked List Example
    print("\n=== Doubly Linked List ===")
    dll = DoublyLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    print("Forward:", dll.display_forward())
    print("Backward:", dll.display_backward())

    # Circular Linked List Example
    print("\n=== Circular Linked List ===")
    cll = CircularLinkedList()
    cll.insert_at_end(1)
    cll.insert_at_end(2)
    cll.insert_at_end(3)
    print(cll)  # 1 -> 2 -> 3 -> (back to head)
