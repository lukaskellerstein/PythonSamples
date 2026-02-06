# Queue class - FIFO
class Queue:
    # List is used to implement a Queue
    def __init__(self):
        self.items = []

    # enqueue function
    def enqueue(self, element):
        # adding element to the queue
        self.items.append(element)

    # dequeue function
    def dequeue(self):
        # removing element from the queue
        # returns "Underflow" when called on an empty queue
        if self.is_empty():
            return "Underflow"
        return self.items.pop(0)

    # front function
    def front(self):
        # returns the front element of the queue without removing it
        if self.is_empty():
            return "No elements in Queue"
        return self.items[0]

    # is_empty function
    def is_empty(self):
        # return True if the queue is empty
        return len(self.items) == 0

    # print_queue function
    def print_queue(self):
        # returns a string representation of the queue
        return " ".join(str(item) for item in self.items)


# Creating an object for the Queue class
queue = Queue()

# Testing dequeue and front on an empty queue
# returns "Underflow"
print(queue.dequeue())

# returns True
print(queue.is_empty())

# Adding elements to the queue
# Queue contains [10, 20, 30, 40, 50, 60]
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)

# printing the elements of the queue
# prints "10 20 30 40 50 60" 
print(queue.print_queue())

# returns 10
print(queue.front())

# removes 10 from the queue
# Queue contains [20, 30, 40, 50, 60]
print(queue.dequeue())

# returns 20
print(queue.front())

# removes 20
# Queue contains [30, 40, 50, 60]
print(queue.dequeue())

# printing the elements of the queue
# prints "30 40 50 60"
print(queue.print_queue())
