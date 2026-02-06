# ----------------------------------
# ----------------------------------
# QUEUE (FIFO - First In First Out)
# Queues are linear data structures following FIFO principle.
# Elements are added at the rear (enqueue) and removed from the front (dequeue).
# Python offers multiple implementations: collections.deque, queue.Queue, and list.
# collections.deque is the recommended implementation for most use cases.
# ----------------------------------
# ----------------------------------

# ----------------------------------
# IMPLEMENTATION OPTIONS
# ----------------------------------

# 1. collections.deque (Recommended for general use)
#    - Thread-safe for append and pop operations
#    - O(1) for enqueue and dequeue
#    - Double-ended queue (can be used as stack or queue)
#    - Memory efficient

# 2. queue.Queue (For multi-threaded applications)
#    - Fully thread-safe with locking
#    - Supports blocking operations
#    - Built for producer-consumer patterns
#    - Slightly slower due to locking overhead

# 3. list (Not recommended for queues)
#    - O(n) for dequeue operation (pop(0))
#    - Inefficient for large queues
#    - Only use for very small queues

# ----------------------------------
# QUEUE WITH collections.deque (RECOMMENDED)
# ----------------------------------

from collections import deque

# Create an empty queue
queue = deque()

# Create queue with initial elements
queue_with_items = deque([1, 2, 3, 4, 5])

# Create queue with maximum size (bounded queue)
bounded_queue = deque(maxlen=5)  # Automatically removes oldest when full

# ----------------------------------
# BASIC OPERATIONS - deque
# ----------------------------------

# Enqueue (add to rear) - O(1)
queue.append(10)
queue.append(20)
queue.append(30)

# Dequeue (remove from front) - O(1)
# Raises IndexError if queue is empty
first = queue.popleft()  # Returns 10

# Peek at front element without removing - O(1)
# Raises IndexError if queue is empty
front = queue[0]  # Returns 20

# Peek at rear element - O(1)
rear = queue[-1]  # Returns 30

# Check if queue is empty - O(1)
is_empty = len(queue) == 0

# Get queue size - O(1)
size = len(queue)

# ----------------------------------
# SAFE OPERATIONS - deque (with error handling)
# ----------------------------------

queue2 = deque()

# Safe dequeue (returns None if empty)
try:
    element = queue2.popleft()
except IndexError:
    element = None

# Safe peek
try:
    front_element = queue2[0]
except IndexError:
    front_element = None

# ----------------------------------
# ADVANCED OPERATIONS - deque
# ----------------------------------

queue3 = deque([1, 2, 3, 4, 5])

# Extend queue (add multiple elements) - O(k) where k is number of elements
queue3.extend([6, 7, 8])  # Adds to right (rear)
queue3.extendleft([0, -1, -2])  # Adds to left (front), in reverse order

# Remove specific element (first occurrence) - O(n)
queue3.remove(3)  # Removes first occurrence of 3

# Count occurrences - O(n)
count = queue3.count(2)

# Rotate queue (positive = rotate right, negative = rotate left) - O(k)
queue3.rotate(2)  # Move 2 elements from right to left
queue3.rotate(-1)  # Move 1 element from left to right

# Clear all elements - O(n)
queue3.clear()

# Reverse the queue - O(n)
queue4 = deque([1, 2, 3, 4])
queue4.reverse()  # [4, 3, 2, 1]

# ----------------------------------
# BOUNDED QUEUE - deque with maxlen
# ----------------------------------

# When queue reaches maxlen, oldest elements are automatically discarded
circular_queue = deque(maxlen=3)

circular_queue.append(1)
circular_queue.append(2)
circular_queue.append(3)
# Queue: [1, 2, 3]

circular_queue.append(4)
# Queue: [2, 3, 4] - 1 was automatically removed

circular_queue.appendleft(0)
# Queue: [0, 2, 3] - 4 was automatically removed

# ----------------------------------
# ITERATION - deque
# ----------------------------------

queue5 = deque([10, 20, 30, 40, 50])

# Iterate forward (front to rear)
for element in queue5:
    print(element)

# Iterate with index
for i, element in enumerate(queue5):
    print(f"Position {i}: {element}")

# Convert to list for indexing
queue_list = list(queue5)

# ----------------------------------
# QUEUE WITH queue.Queue (THREAD-SAFE)
# ----------------------------------

import queue

# Create an unbounded FIFO queue
thread_queue = queue.Queue()

# Create a bounded queue (blocks when full)
bounded_thread_queue = queue.Queue(maxsize=10)

# Create a LIFO queue (stack)
stack_queue = queue.LifoQueue()

# Create a priority queue (lowest priority value comes first)
priority_queue = queue.PriorityQueue()

# ----------------------------------
# BASIC OPERATIONS - queue.Queue
# ----------------------------------

# Enqueue (add to queue)
thread_queue.put(10)
thread_queue.put(20)
thread_queue.put(30)

# Enqueue with timeout (blocks for max timeout seconds if full)
try:
    bounded_thread_queue.put(40, block=True, timeout=2)
except queue.Full:
    print("Queue is full")

# Enqueue without blocking (raises queue.Full if queue is full)
try:
    bounded_thread_queue.put_nowait(50)
except queue.Full:
    print("Queue is full")

# Dequeue (blocks until an item is available)
item = thread_queue.get()  # Returns 10

# Dequeue with timeout (blocks for max timeout seconds)
try:
    item = thread_queue.get(block=True, timeout=2)
except queue.Empty:
    print("Queue is empty")

# Dequeue without blocking (raises queue.Empty if queue is empty)
try:
    item = thread_queue.get_nowait()
except queue.Empty:
    print("Queue is empty")

# Check queue size - O(1)
size = thread_queue.qsize()  # Approximate in multithreaded environment

# Check if queue is empty - O(1)
is_empty = thread_queue.empty()  # Not reliable in multithreaded environment

# Check if queue is full - O(1)
is_full = bounded_thread_queue.full()  # Not reliable in multithreaded environment

# ----------------------------------
# TASK MANAGEMENT - queue.Queue
# ----------------------------------

# Used in producer-consumer patterns to track task completion

# Mark task as done (should be called after processing each item from get())
thread_queue.task_done()

# Block until all tasks are done (waits for all task_done() calls)
thread_queue.join()

# Example producer-consumer pattern:
def producer(q):
    for i in range(5):
        q.put(i)
        print(f"Produced: {i}")

def consumer(q):
    while True:
        item = q.get()
        if item is None:  # Poison pill to stop consumer
            break
        print(f"Consumed: {item}")
        q.task_done()

# ----------------------------------
# PRIORITY QUEUE
# ----------------------------------

pq = queue.PriorityQueue()

# Add items with priority (lower number = higher priority)
pq.put((1, "High priority task"))
pq.put((5, "Low priority task"))
pq.put((3, "Medium priority task"))

# Retrieve items (returns lowest priority number first)
task1 = pq.get()  # (1, "High priority task")
task2 = pq.get()  # (3, "Medium priority task")
task3 = pq.get()  # (5, "Low priority task")

# Priority queue with custom objects
class Task:
    def __init__(self, priority, description):
        self.priority = priority
        self.description = description

    def __lt__(self, other):
        return self.priority < other.priority

pq2 = queue.PriorityQueue()
pq2.put(Task(1, "Important"))
pq2.put(Task(5, "Not urgent"))

# ----------------------------------
# QUEUE WITH LIST (NOT RECOMMENDED)
# ----------------------------------

# Using list as a queue (inefficient - for demonstration only)
list_queue = []

# Enqueue - O(1)
list_queue.append(10)
list_queue.append(20)

# Dequeue - O(n) - SLOW! All elements need to shift
first = list_queue.pop(0)

# This is why list is not recommended for queues
# Use collections.deque instead

# ----------------------------------
# COMPARISON OF IMPLEMENTATIONS
# ----------------------------------

# collections.deque:
# ✓ Fast O(1) append and popleft
# ✓ Memory efficient
# ✓ Thread-safe for append/pop operations
# ✓ Can be used as stack or queue
# ✓ Best for single-threaded or simple multi-threaded use
# ✗ No built-in blocking operations

# queue.Queue:
# ✓ Fully thread-safe with locks
# ✓ Blocking operations (put/get with timeout)
# ✓ Task tracking (task_done, join)
# ✓ Best for producer-consumer patterns
# ✗ Slightly slower due to locking overhead
# ✗ No direct access to elements

# list:
# ✓ Simple and familiar
# ✗ O(n) dequeue operation (pop(0))
# ✗ Inefficient for queues
# ✗ Only use for very small queues (<10 elements)

# ----------------------------------
# COMMON QUEUE PATTERNS
# ----------------------------------

# 1. Simple FIFO queue
simple_queue = deque()
simple_queue.append("Task 1")
simple_queue.append("Task 2")
task = simple_queue.popleft()

# 2. Breadth-First Search (BFS)
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            # Process node
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

# 3. Sliding window
def max_sliding_window(nums, k):
    """Find maximum in each sliding window of size k"""
    result = []
    window = deque()

    for i, num in enumerate(nums):
        # Remove elements outside current window
        while window and window[0] <= i - k:
            window.popleft()

        # Remove smaller elements
        while window and nums[window[-1]] < num:
            window.pop()

        window.append(i)

        # Add to result once we have k elements
        if i >= k - 1:
            result.append(nums[window[0]])

    return result

# 4. Producer-Consumer with queue.Queue
import threading

def producer_consumer_example():
    q = queue.Queue(maxsize=10)

    def producer():
        for i in range(20):
            q.put(i)
            print(f"Produced: {i}")
        q.put(None)  # Poison pill

    def consumer():
        while True:
            item = q.get()
            if item is None:
                break
            print(f"Consumed: {item}")
            q.task_done()

    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

# 5. Level-order tree traversal
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def level_order_traversal(root):
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    return result

# 6. Recent counter (circular buffer)
class RecentCounter:
    def __init__(self):
        self.queue = deque()

    def ping(self, t):
        """Count requests in the last 3000ms"""
        self.queue.append(t)
        # Remove old requests
        while self.queue[0] < t - 3000:
            self.queue.popleft()
        return len(self.queue)

# ----------------------------------
# PRACTICAL USE CASES
# ----------------------------------

# 1. Task scheduling
task_queue = deque()
task_queue.append("Send email")
task_queue.append("Process payment")
task_queue.append("Update database")

while task_queue:
    current_task = task_queue.popleft()
    print(f"Processing: {current_task}")

# 2. Print queue simulation
print_queue = deque()
print_queue.append("Document1.pdf")
print_queue.append("Document2.pdf")
print_queue.append("Document3.pdf")

# Process print jobs
while print_queue:
    document = print_queue.popleft()
    print(f"Printing: {document}")

# 3. Message queue
message_queue = deque()
message_queue.append({"user": "Alice", "message": "Hello"})
message_queue.append({"user": "Bob", "message": "Hi there"})

# 4. Request buffering
class RequestBuffer:
    def __init__(self, max_size=100):
        self.buffer = deque(maxlen=max_size)

    def add_request(self, request):
        self.buffer.append(request)

    def process_requests(self):
        while self.buffer:
            request = self.buffer.popleft()
            # Process request
            pass

# 5. Undo/Redo with two queues
class UndoRedo:
    def __init__(self):
        self.undo_stack = deque()
        self.redo_stack = deque()

    def do_action(self, action):
        self.undo_stack.append(action)
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            action = self.undo_stack.pop()
            self.redo_stack.append(action)
            return action

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.undo_stack.append(action)
            return action

# ----------------------------------
# PERFORMANCE NOTES
# ----------------------------------

# Time Complexity (collections.deque):
# - append (enqueue):     O(1)
# - appendleft:           O(1)
# - pop:                  O(1)
# - popleft (dequeue):    O(1)
# - Access by index:      O(n) - slower than list
# - Length:               O(1)
# - Remove by value:      O(n)
# - Extend:               O(k) where k is number of elements
# - Rotate:               O(k) where k is rotation count

# Time Complexity (queue.Queue):
# - put:                  O(1) + locking overhead
# - get:                  O(1) + locking overhead
# - qsize:                O(1)

# Space Complexity:
# - All implementations:  O(n) where n is number of elements

# Use queues when:
# - You need FIFO (First In First Out) order
# - Processing tasks in order
# - Implementing BFS algorithms
# - Level-order traversals
# - Producer-consumer patterns
# - Message passing between threads
# - Buffering or streaming data

# Use collections.deque when:
# - You need a general-purpose queue
# - Single-threaded or simple multi-threaded scenarios
# - Performance is critical
# - You need both queue and stack operations

# Use queue.Queue when:
# - Working with multiple threads
# - Need blocking operations
# - Implementing producer-consumer patterns
# - Task coordination with task_done/join

# Use list when:
# - Queue is very small (<10 elements)
# - Simplicity is more important than performance
# - Generally NOT recommended for queues
