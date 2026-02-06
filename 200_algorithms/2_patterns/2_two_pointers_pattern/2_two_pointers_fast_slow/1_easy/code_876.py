
# -----------------------
# Middle of the Linked List (LeetCode 876)
# -----------------------

# Difficulty: Easy

# Problem: Given the head of a singly linked list, return the middle node.
# If there are two middle nodes, return the second middle node.

# -----------------------
# VISUALIZATION
# -----------------------
#
# [1, 2, 3, 4, 5]
#
# Step 0: slow=1, fast=1
# Step 1: slow=2, fast=3
# Step 2: slow=3, fast=5  ← fast reached end, slow is at middle ✓
#
# When fast reaches the end at 2x speed, slow is exactly halfway.
#
# For even length [1, 2, 3, 4, 5, 6]:
# Step 0: slow=1, fast=1
# Step 1: slow=2, fast=3
# Step 2: slow=3, fast=5
# Step 3: slow=4, fast=None ← fast.next is None, slow is at second middle ✓
#
# -----------------------

from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ----------------------------------------------------
# Two Pointers solution (Fast/Slow)
#
# time complexity = O(n) - single pass, fast pointer traverses full list
# space complexity = O(1) - only using two pointers
# ----------------------------------------------------

def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps

    return slow


# ----------------------------------------------------
# Brute Force solution (Array)
#
# time complexity = O(n) - traverse list once to build array
# space complexity = O(n) - storing all nodes in array
# ----------------------------------------------------

def middle_node_brute_force(head: Optional[ListNode]) -> Optional[ListNode]:
    # Store all nodes in array
    nodes = []
    current = head

    while current:
        nodes.append(current)
        current = current.next

    # Return middle node
    return nodes[len(nodes) // 2]


# ----------------------------------------------------
# Helper function to create linked list from array
# ----------------------------------------------------

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    test_cases = [
        [1, 2, 3, 4, 5],       # Odd length -> middle is 3
        [1, 2, 3, 4, 5, 6],    # Even length -> second middle is 4
        [1],                   # Single element -> 1
        [1, 2],                # Two elements -> second middle is 2
    ]

    print("Middle of Linked List Results:")
    print("-" * 55)
    print(f"{'Input':<20} {'Two Pointers':<15} {'Brute Force':<15}")
    print("-" * 55)

    for values in test_cases:
        head1 = create_linked_list(values)
        head2 = create_linked_list(values)

        result1 = middle_node(head1)
        result2 = middle_node_brute_force(head2)

        print(f"{str(values):<20} {result1.val:<15} {result2.val:<15}")
