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
                currVal = self.arr[current_index]
                parVal = self.arr[parent_index]

                self.arr[parent_index] = currVal
                self.arr[current_index] = parVal

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
            currVal = self.arr[current_index]
            smallestVal = self.arr[smallest_index]

            self.arr[current_index] = smallestVal
            self.arr[smallest_index] = currVal

            # Recursively bubble down the swapped value
            self.bubble_down(smallest_index)



# ==================== USAGE AND VALIDATION ====================

if __name__ == "__main__":
    print("=== Min Heap Implementation Test ===\n")

    # Test 1: Empty heap
    print("Test 1: Empty heap")
    heap = MyMinHeap()
    assert heap.arr == [], "FAIL: Heap should be empty"
    print("  ✓ Empty heap works correctly\n")

    # Test 2: Insert single element
    print("Test 2: Insert single element (10)")
    heap.insert(10)
    assert heap.arr == [10], "FAIL: Heap should contain [10]"
    print("  Heap array:", heap.arr)
    print("  ✓ Single element insertion works\n")

    # Test 3: Insert multiple elements - should maintain min heap property
    print("Test 3: Insert multiple elements (5, 15, 3, 8, 1)")
    heap2 = MyMinHeap()
    for val in [5, 15, 3, 8, 1]:
        heap2.insert(val)

    # Expected heap structure (min at root):
    #          1
    #        /   \
    #       3     5
    #      / \
    #     8  15

    print("  Expected tree structure:")
    print("           1")
    print("         /   \\")
    print("        3     5")
    print("       / \\")
    print("      8  15")
    print()
    print("  Heap array:", heap2.arr)

    assert heap2.arr[0] == 1, "FAIL: Root (minimum) should be 1"
    assert heap2.arr[1] <= heap2.arr[3], "FAIL: Parent should be <= left child"
    assert heap2.arr[1] <= heap2.arr[4], "FAIL: Parent should be <= right child"
    print("  ✓ Min heap property maintained after insertions\n")

    # Test 4: Insert elements in descending order
    print("Test 4: Insert elements in descending order (50, 40, 30, 20, 10)")
    heap3 = MyMinHeap()
    for val in [50, 40, 30, 20, 10]:
        heap3.insert(val)

    print("  Heap array:", heap3.arr)
    assert heap3.arr[0] == 10, "FAIL: Root should be minimum (10)"
    print("  ✓ Descending order insertion maintains heap property\n")

    # Test 5: Insert elements in ascending order
    print("Test 5: Insert elements in ascending order (1, 2, 3, 4, 5)")
    heap4 = MyMinHeap()
    for val in [1, 2, 3, 4, 5]:
        heap4.insert(val)

    print("  Heap array:", heap4.arr)
    assert heap4.arr[0] == 1, "FAIL: Root should be minimum (1)"
    print("  ✓ Ascending order insertion maintains heap property\n")

    # Test 6: Insert duplicate values
    print("Test 6: Insert duplicate values (5, 5, 5, 3, 3)")
    heap5 = MyMinHeap()
    for val in [5, 5, 5, 3, 3]:
        heap5.insert(val)

    print("  Heap array:", heap5.arr)
    assert heap5.arr[0] == 3, "FAIL: Root should be minimum (3)"
    print("  ✓ Duplicate values handled correctly\n")

    # ==================== REMOVE METHOD TESTS ====================

    # Test 7: Remove from empty heap
    print("Test 7: Remove from empty heap")
    empty_heap = MyMinHeap()
    empty_heap.remove(10)  # Should not raise an error
    assert empty_heap.arr == [], "FAIL: Empty heap should remain empty"
    print("  ✓ Remove from empty heap works correctly\n")

    # Test 8: Remove non-existent value
    print("Test 8: Remove non-existent value")
    heap6 = MyMinHeap()
    heap6.insert(5)
    heap6.insert(10)
    arr_before = heap6.arr.copy()
    heap6.remove(99)
    assert heap6.arr == arr_before, "FAIL: Heap should be unchanged"
    print("  ✓ Remove non-existent value works correctly\n")

    # Test 9: Remove single element (last element)
    print("Test 9: Remove single element from heap with one element")
    heap7 = MyMinHeap()
    heap7.insert(42)
    heap7.remove(42)
    assert heap7.arr == [], "FAIL: Heap should be empty after removing only element"
    print("  ✓ Removing single element works correctly\n")

    # Test 10: Remove the minimum (root) element
    print("Test 10: Remove minimum element (root)")
    heap8 = MyMinHeap()
    for val in [3, 10, 5, 15, 8]:
        heap8.insert(val)

    print("  Before removal - Heap array:", heap8.arr)
    print("  Minimum (root) is:", heap8.arr[0])

    heap8.remove(heap8.arr[0])  # Remove minimum

    print("  After removal - Heap array:", heap8.arr)
    assert heap8.arr[0] == min(heap8.arr), "FAIL: Root should be minimum after removal"
    print("  ✓ Root removal maintains heap property\n")

    # Test 11: Remove leaf node (last element in array)
    print("Test 11: Remove leaf node")
    heap9 = MyMinHeap()
    for val in [1, 5, 3, 10, 8]:
        heap9.insert(val)

    # Heap structure:
    #          1
    #        /   \
    #       5     3
    #      / \
    #    10   8

    print("  Before removal - Heap array:", heap9.arr)
    last_val = heap9.arr[-1]
    heap9.remove(last_val)
    print("  Removed leaf:", last_val)
    print("  After removal - Heap array:", heap9.arr)
    assert last_val not in heap9.arr, "FAIL: Removed value should not be in heap"
    print("  ✓ Leaf removal works correctly\n")

    # Test 12: Build heap and verify parent-child relationships
    print("Test 12: Verify parent-child relationships")
    heap10 = MyMinHeap()
    values = [20, 15, 30, 10, 5, 25, 35]
    for val in values:
        heap10.insert(val)

    print("  Inserted values:", values)
    print("  Heap array:", heap10.arr)

    # Verify each parent is smaller than or equal to its children
    for i in range(len(heap10.arr)):
        left_idx = heap10.getLeftChildIndex(i)
        right_idx = heap10.getRightChildIndex(i)

        if left_idx < len(heap10.arr):
            assert heap10.arr[i] <= heap10.arr[left_idx], \
                f"FAIL: Parent {heap10.arr[i]} > left child {heap10.arr[left_idx]}"
        if right_idx < len(heap10.arr):
            assert heap10.arr[i] <= heap10.arr[right_idx], \
                f"FAIL: Parent {heap10.arr[i]} > right child {heap10.arr[right_idx]}"

    print("  ✓ All parent-child relationships valid\n")

    # Test 13: Index calculation methods
    print("Test 13: Verify index calculations")
    heap11 = MyMinHeap()

    # Test parent index calculation
    assert heap11.getParentIndex(1) == 0, "FAIL: Parent of index 1 should be 0"
    assert heap11.getParentIndex(2) == 0, "FAIL: Parent of index 2 should be 0"
    assert heap11.getParentIndex(3) == 1, "FAIL: Parent of index 3 should be 1"
    assert heap11.getParentIndex(4) == 1, "FAIL: Parent of index 4 should be 1"
    assert heap11.getParentIndex(5) == 2, "FAIL: Parent of index 5 should be 2"

    # Test left child index calculation
    assert heap11.getLeftChildIndex(0) == 1, "FAIL: Left child of 0 should be 1"
    assert heap11.getLeftChildIndex(1) == 3, "FAIL: Left child of 1 should be 3"
    assert heap11.getLeftChildIndex(2) == 5, "FAIL: Left child of 2 should be 5"

    # Test right child index calculation
    assert heap11.getRightChildIndex(0) == 2, "FAIL: Right child of 0 should be 2"
    assert heap11.getRightChildIndex(1) == 4, "FAIL: Right child of 1 should be 4"
    assert heap11.getRightChildIndex(2) == 6, "FAIL: Right child of 2 should be 6"

    print("  ✓ All index calculations correct\n")

    # Test 14: Stress test with many insertions
    print("Test 14: Stress test with 100 insertions")
    import random
    heap12 = MyMinHeap()
    test_values = [random.randint(1, 1000) for _ in range(100)]

    for val in test_values:
        heap12.insert(val)

    assert heap12.arr[0] == min(test_values), "FAIL: Root should be minimum value"
    print(f"  Inserted 100 random values")
    print(f"  Minimum value: {min(test_values)}")
    print(f"  Root of heap: {heap12.arr[0]}")
    print("  ✓ Stress test passed\n")

    print("=== All tests passed! ===")
