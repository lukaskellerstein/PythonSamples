# ----------------------------------
# ----------------------------------
# STACK (LIFO - Last In First Out)
# Stacks are linear data structures following LIFO principle.
# Elements are added and removed from the same end (top of stack).
# Push adds elements, pop removes elements, peek views the top element.
# Python offers multiple implementations: list, collections.deque, and queue.LifoQueue.
# list is the simplest and most commonly used for single-threaded stacks.
# ----------------------------------
# ----------------------------------

# ----------------------------------
# IMPLEMENTATION OPTIONS
# ----------------------------------

# 1. list (Recommended for most use cases)
#    - Simple and intuitive
#    - O(1) for push and pop (amortized)
#    - Built-in, no imports needed
#    - Most pythonic approach

# 2. collections.deque (For performance-critical applications)
#    - O(1) for all operations (not amortized)
#    - More consistent performance
#    - Thread-safe for append and pop operations
#    - Slightly more memory overhead

# 3. queue.LifoQueue (For multi-threaded applications)
#    - Fully thread-safe with locking
#    - Supports blocking operations
#    - Built for producer-consumer patterns
#    - Slower due to locking overhead

# ----------------------------------
# STACK WITH list (RECOMMENDED)
# ----------------------------------

# Create an empty stack
stack = []

# Create stack with initial elements
stack_with_items = [1, 2, 3, 4, 5]

# ----------------------------------
# BASIC OPERATIONS - list
# ----------------------------------

# Push (add to top) - O(1) amortized
stack.append(10)
stack.append(20)
stack.append(30)
# Stack: [10, 20, 30] (30 is on top)

# Pop (remove from top) - O(1)
# Raises IndexError if stack is empty
top = stack.pop()  # Returns 30
# Stack: [10, 20]

# Peek (view top element without removing) - O(1)
# Raises IndexError if stack is empty
top_element = stack[-1]  # Returns 20

# Check if stack is empty - O(1)
is_empty = len(stack) == 0
is_empty2 = not stack  # More pythonic

# Get stack size - O(1)
size = len(stack)

# ----------------------------------
# SAFE OPERATIONS - list (with error handling)
# ----------------------------------

empty_stack = []

# Safe pop (returns None if empty)
try:
    element = empty_stack.pop()
except IndexError:
    element = None

# Alternative: check before pop
if empty_stack:
    element = empty_stack.pop()
else:
    element = None

# Safe peek
try:
    top = empty_stack[-1]
except IndexError:
    top = None

# Alternative: check before peek
if empty_stack:
    top = empty_stack[-1]
else:
    top = None

# ----------------------------------
# ADDITIONAL OPERATIONS - list
# ----------------------------------

stack2 = [1, 2, 3, 4, 5]

# Access elements by index (not typical for stack, but possible)
# Index 0 is bottom, -1 is top
bottom = stack2[0]  # 1
second_from_top = stack2[-2]  # 4

# Search for element - O(n)
# Returns True if element exists
has_element = 3 in stack2

# Find index of element from bottom - O(n)
# Returns index if found, raises ValueError if not found
try:
    index = stack2.index(3)  # Returns 2
except ValueError:
    index = -1

# Count occurrences of element - O(n)
count = stack2.count(3)

# Clear all elements - O(n)
stack2.clear()

# ----------------------------------
# STACK WITH collections.deque
# ----------------------------------

from collections import deque

# Create an empty stack
deque_stack = deque()

# Create stack with initial elements
deque_stack_with_items = deque([1, 2, 3, 4, 5])

# Push - O(1)
deque_stack.append(10)
deque_stack.append(20)

# Pop - O(1)
# Raises IndexError if empty
top = deque_stack.pop()

# Peek - O(1)
# Raises IndexError if empty
top_element = deque_stack[-1]

# Check if empty
is_empty = len(deque_stack) == 0

# Size
size = len(deque_stack)

# Clear
deque_stack.clear()

# ----------------------------------
# BOUNDED STACK - deque with maxlen
# ----------------------------------

# Stack with maximum size
bounded_stack = deque(maxlen=5)

for i in range(10):
    bounded_stack.append(i)
# Stack only contains: [5, 6, 7, 8, 9] (oldest elements automatically removed)

# ----------------------------------
# STACK WITH queue.LifoQueue (THREAD-SAFE)
# ----------------------------------

import queue

# Create an unbounded LIFO stack
thread_stack = queue.LifoQueue()

# Create a bounded stack (blocks when full)
bounded_thread_stack = queue.LifoQueue(maxsize=10)

# Push
thread_stack.put(10)
thread_stack.put(20)
thread_stack.put(30)

# Push with timeout (blocks for max timeout seconds if full)
try:
    bounded_thread_stack.put(40, block=True, timeout=2)
except queue.Full:
    print("Stack is full")

# Push without blocking (raises queue.Full if stack is full)
try:
    bounded_thread_stack.put_nowait(50)
except queue.Full:
    print("Stack is full")

# Pop (blocks until an item is available)
item = thread_stack.get()  # Returns 30 (LIFO)

# Pop with timeout (blocks for max timeout seconds)
try:
    item = thread_stack.get(block=True, timeout=2)
except queue.Empty:
    print("Stack is empty")

# Pop without blocking (raises queue.Empty if stack is empty)
try:
    item = thread_stack.get_nowait()
except queue.Empty:
    print("Stack is empty")

# Check stack size - O(1)
size = thread_stack.qsize()  # Approximate in multithreaded environment

# Check if stack is empty - O(1)
is_empty = thread_stack.empty()  # Not reliable in multithreaded environment

# Check if stack is full - O(1)
is_full = bounded_thread_stack.full()  # Not reliable in multithreaded environment

# ----------------------------------
# COMPARISON OF IMPLEMENTATIONS
# ----------------------------------

# list:
# ✓ Simple and intuitive
# ✓ No imports needed
# ✓ O(1) push and pop (amortized)
# ✓ Most pythonic
# ✓ Direct access to all elements
# ✗ Occasional O(n) when resizing
# ✗ Not thread-safe
# Best for: Most general use cases

# collections.deque:
# ✓ O(1) push and pop (not amortized)
# ✓ More consistent performance
# ✓ Thread-safe for append/pop
# ✓ Can set maxlen for bounded stack
# ✗ Slightly more memory overhead
# ✗ Requires import
# Best for: Performance-critical applications

# queue.LifoQueue:
# ✓ Fully thread-safe
# ✓ Blocking operations
# ✓ Task tracking
# ✗ Slower due to locking
# ✗ No direct element access
# ✗ More complex API
# Best for: Multi-threaded applications

# ----------------------------------
# ITERATION (NOT TYPICAL FOR STACK)
# ----------------------------------

stack3 = [10, 20, 30, 40, 50]

# Iterate from bottom to top
for element in stack3:
    print(element)

# Iterate from top to bottom (more stack-like)
for element in reversed(stack3):
    print(element)

# Iterate while popping (destructive)
while stack3:
    element = stack3.pop()
    print(element)  # 50, 40, 30, 20, 10

# ----------------------------------
# COMMON STACK PATTERNS
# ----------------------------------

# 1. Depth-First Search (DFS)
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Process node
            print(node)
            # Add neighbors to stack (in reverse order to maintain left-to-right)
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited

# 2. Balanced parentheses checker
def is_balanced(expression):
    """Check if parentheses are balanced"""
    stack = []
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in expression:
        if char in pairs:  # Opening bracket
            stack.append(char)
        elif char in pairs.values():  # Closing bracket
            if not stack or pairs[stack.pop()] != char:
                return False

    return len(stack) == 0

# Examples:
# is_balanced("()[]{}") -> True
# is_balanced("([)]") -> False
# is_balanced("((()))") -> True

# 3. Reverse a string/list
def reverse_with_stack(items):
    """Reverse using a stack"""
    stack = []
    for item in items:
        stack.append(item)

    reversed_items = []
    while stack:
        reversed_items.append(stack.pop())

    return reversed_items

# Note: Python's reversed() or [::-1] is more efficient

# 4. Evaluate Postfix (Reverse Polish Notation)
def evaluate_postfix(expression):
    """Evaluate postfix expression: "3 4 + 2 *" = 14"""
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression.split():
        if token in operators:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(a / b)
        else:
            stack.append(float(token))

    return stack[0]

# Example: evaluate_postfix("3 4 + 2 *") -> 14.0

# 5. Convert Infix to Postfix
def infix_to_postfix(expression):
    """Convert infix to postfix: "3 + 4 * 2" -> "3 4 2 * +" """
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    stack = []
    output = []

    for token in expression.split():
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '('
        elif token in precedence:
            while (stack and stack[-1] != '(' and
                   stack[-1] in precedence and
                   precedence[stack[-1]] >= precedence[token]):
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

# 6. Next Greater Element
def next_greater_element(arr):
    """For each element, find the next greater element to its right"""
    stack = []
    result = [-1] * len(arr)

    for i in range(len(arr) - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()

        if stack:
            result[i] = stack[-1]

        stack.append(arr[i])

    return result

# Example: next_greater_element([4, 5, 2, 10, 8]) -> [5, 10, 10, -1, -1]

# 7. Valid Parentheses with Multiple Types
def is_valid_parentheses(s):
    """Check if string has valid parentheses: (), [], {}"""
    stack = []
    mapping = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in mapping:  # Closing bracket
            if not stack or stack.pop() != mapping[char]:
                return False
        else:  # Opening bracket
            stack.append(char)

    return len(stack) == 0

# 8. Min Stack (stack with O(1) min operation)
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # Keeps track of minimum values

    def push(self, val):
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack.pop()
        if val == self.min_stack[-1]:
            self.min_stack.pop()
        return val

    def top(self):
        return self.stack[-1] if self.stack else None

    def get_min(self):
        return self.min_stack[-1] if self.min_stack else None

# 9. Stock Span Problem
def calculate_span(prices):
    """Calculate span: number of consecutive days before current day
    where price was less than or equal to current day's price"""
    stack = []  # Stack of indices
    span = []

    for i, price in enumerate(prices):
        # Pop elements while price is greater
        while stack and prices[stack[-1]] <= price:
            stack.pop()

        # Calculate span
        if not stack:
            span.append(i + 1)  # All previous days
        else:
            span.append(i - stack[-1])  # Days since last higher price

        stack.append(i)

    return span

# Example: calculate_span([100, 80, 60, 70, 60, 75, 85])
# Result: [1, 1, 1, 2, 1, 4, 6]

# 10. Binary Tree Traversal (Iterative DFS)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def preorder_traversal(root):
    """Pre-order: Root -> Left -> Right"""
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push right first, then left (so left is processed first)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

def inorder_traversal(root):
    """In-order: Left -> Root -> Right"""
    stack = []
    result = []
    current = root

    while current or stack:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left

        # Process node
        current = stack.pop()
        result.append(current.val)

        # Go to right subtree
        current = current.right

    return result

def postorder_traversal(root):
    """Post-order: Left -> Right -> Root"""
    if not root:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)

        # Push left first, then right
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    # Reverse the result
    return result[::-1]

# ----------------------------------
# PRACTICAL USE CASES
# ----------------------------------

# 1. Undo functionality
class TextEditor:
    def __init__(self):
        self.text = ""
        self.history = []

    def write(self, text):
        self.history.append(self.text)
        self.text += text

    def undo(self):
        if self.history:
            self.text = self.history.pop()

# 2. Browser history (back button)
class BrowserHistory:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = None

    def visit(self, url):
        if self.current:
            self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self):
        if self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
        return self.current

    def forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
        return self.current

# 3. Function call stack simulation
def factorial_iterative(n):
    """Calculate factorial using explicit stack"""
    stack = []
    result = 1

    # Push all numbers onto stack
    for i in range(1, n + 1):
        stack.append(i)

    # Pop and multiply
    while stack:
        result *= stack.pop()

    return result

# 4. Backtracking with explicit stack
def generate_parentheses(n):
    """Generate all valid combinations of n pairs of parentheses"""
    result = []
    stack = [("", 0, 0)]  # (current_string, open_count, close_count)

    while stack:
        current, open_count, close_count = stack.pop()

        if len(current) == 2 * n:
            result.append(current)
            continue

        if open_count < n:
            stack.append((current + "(", open_count + 1, close_count))

        if close_count < open_count:
            stack.append((current + ")", open_count, close_count + 1))

    return result

# 5. Path tracking in maze/graph
def find_path(maze, start, end):
    """Find path in maze using DFS with stack"""
    stack = [(start, [start])]  # (position, path)
    visited = set()

    while stack:
        pos, path = stack.pop()

        if pos == end:
            return path

        if pos in visited:
            continue

        visited.add(pos)

        # Add neighbors to stack
        for neighbor in get_neighbors(maze, pos):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return None  # No path found

def get_neighbors(maze, pos):
    """Helper function to get valid neighbors"""
    # Implementation depends on maze structure
    pass

# 6. Expression evaluation
def evaluate_expression(expr):
    """Evaluate mathematical expression with precedence"""
    def apply_operation(operators, values):
        operator = operators.pop()
        right = values.pop()
        left = values.pop()

        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            values.append(left / right)

    values = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            values.append(int(expr[i:j]))
            i = j
        elif expr[i] in precedence:
            while (operators and operators[-1] in precedence and
                   precedence[operators[-1]] >= precedence[expr[i]]):
                apply_operation(operators, values)
            operators.append(expr[i])
            i += 1
        else:
            i += 1

    while operators:
        apply_operation(operators, values)

    return values[0]

# ----------------------------------
# STACK-BASED ALGORITHMS
# ----------------------------------

# 1. Largest Rectangle in Histogram
def largest_rectangle_area(heights):
    """Find largest rectangle in histogram"""
    stack = []
    max_area = 0
    index = 0

    while index < len(heights):
        if not stack or heights[index] >= heights[stack[-1]]:
            stack.append(index)
            index += 1
        else:
            top = stack.pop()
            width = index if not stack else index - stack[-1] - 1
            area = heights[top] * width
            max_area = max(max_area, area)

    while stack:
        top = stack.pop()
        width = index if not stack else index - stack[-1] - 1
        area = heights[top] * width
        max_area = max(max_area, area)

    return max_area

# 2. Trapping Rain Water
def trap_rain_water(height):
    """Calculate how much water can be trapped"""
    if not height:
        return 0

    stack = []
    water = 0

    for i in range(len(height)):
        while stack and height[i] > height[stack[-1]]:
            top = stack.pop()

            if not stack:
                break

            distance = i - stack[-1] - 1
            bounded_height = min(height[i], height[stack[-1]]) - height[top]
            water += distance * bounded_height

        stack.append(i)

    return water

# 3. Decode String
def decode_string(s):
    """Decode encoded string: "3[a2[c]]" -> "accaccacc" """
    stack = []
    current_num = 0
    current_string = ""

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack.append((current_string, current_num))
            current_string = ""
            current_num = 0
        elif char == ']':
            prev_string, num = stack.pop()
            current_string = prev_string + current_string * num
        else:
            current_string += char

    return current_string

# ----------------------------------
# PERFORMANCE NOTES
# ----------------------------------

# Time Complexity (all implementations):
# - Push:                 O(1)
# - Pop:                  O(1)
# - Peek:                 O(1)
# - Search:               O(n)
# - Access by index:      O(1) for list/deque, N/A for LifoQueue

# Space Complexity:
# - All implementations:  O(n) where n is number of elements

# Amortized vs Worst Case:
# - list: O(1) amortized, occasionally O(n) when resizing
# - deque: O(1) always
# - LifoQueue: O(1) + locking overhead

# Use stacks when:
# - You need LIFO (Last In First Out) order
# - Implementing recursion iteratively
# - Backtracking algorithms
# - Parsing expressions
# - Tree/graph traversal (DFS)
# - Undo/redo functionality
# - Function call tracking

# Choose list when:
# - General purpose stack
# - Single-threaded application
# - Simplicity is important
# - Most common choice

# Choose deque when:
# - Need consistent O(1) performance
# - Performance-critical applications
# - Want bounded stack (maxlen)

# Choose LifoQueue when:
# - Multi-threaded application
# - Need blocking operations
# - Producer-consumer pattern with LIFO

# Stack vs Queue:
# - Stack (LIFO): DFS, backtracking, expression evaluation, undo
# - Queue (FIFO): BFS, task scheduling, buffering, level-order traversal
