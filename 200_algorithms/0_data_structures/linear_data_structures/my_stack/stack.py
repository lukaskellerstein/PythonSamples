# Stack class - LIFO
class Stack:
    # Constructor to initialize the stack
    def __init__(self):
        self.items = []

    # push function
    def push(self, element):
        # Push element into the stack
        self.items.append(element)

    # pop function
    def pop(self):
        # Return and remove the topmost element from the stack
        # Underflow if stack is empty
        if len(self.items) == 0:
            return "Underflow"
        return self.items.pop()

    # peek function
    def peek(self):
        # Return the topmost element without removing it
        if len(self.items) == 0:
            return "Stack is empty"
        return self.items[-1]

    # isEmpty function
    def is_empty(self):
        # Return True if the stack is empty
        return len(self.items) == 0

    # printStack function
    def print_stack(self):
        # Print all elements of the stack
        return " ".join(map(str, self.items))

# Creating an object for the Stack class
stack = Stack()

# Testing is_empty and pop on an empty stack

# returns True
print(stack.is_empty())

# returns "Underflow"
print(stack.pop())

# Adding elements to the stack
stack.push(10)
stack.push(20)
stack.push(30)

# Printing the stack elements
# prints "10 20 30"
print(stack.print_stack())

# returns 30
print(stack.peek())

# returns 30 and removes it from the stack
print(stack.pop())

# returns "10 20"
print(stack.print_stack())
