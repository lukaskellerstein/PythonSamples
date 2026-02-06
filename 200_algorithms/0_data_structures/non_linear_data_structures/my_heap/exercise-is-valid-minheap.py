from min_heap import MyMinHeap


def is_valid_min_heap(arr):
    """Helper function to validate min heap property"""
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True



heap2 = MyMinHeap()
heap2.insert(5)
heap2.insert(15)
heap2.insert(3)
heap2.insert(8)
heap2.insert(1)


result = is_valid_min_heap(heap2.arr)
print(result)