
# -----------------------
# Linked List Cycle II (LeetCode 142)
# -----------------------

# Difficulty: Medium

# Problem: Given the head of a linked list, return the node where the cycle begins.
# If there is no cycle, return None.

# -----------------------
# VISUALIZATION
# -----------------------
#
# Example: 3 → 2 → 0 → -4
#              ↑         ↓
#              └─────────┘
#
# The cycle begins at node with value 2.
#
# Floyd's Algorithm (Tortoise and Hare):
# 1. Use fast/slow pointers to detect cycle
# 2. When they meet, reset one pointer to head
# 3. Move both at same speed - they'll meet at cycle start
#
# -----------------------

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ----------------------------------------------------
# Two Pointers solution (Floyd's Cycle Detection)
#
# time complexity = O(n) - at most 2 passes through the list
# space complexity = O(1) - only using two pointers
# ----------------------------------------------------

def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    # Phase 1: Detect if cycle exists
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # 1 step
        fast = fast.next.next     # 2 steps

        if slow == fast:
            # Cycle detected, now find the start
            break
    else:
        # No cycle found
        return None

    # Phase 2: Find cycle start
    # Reset one pointer to head, move both at same speed
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow  # Both pointers meet at cycle start


# ----------------------------------------------------
# Brute Force solution (HashSet)
#
# time complexity = O(n) - single pass through the list
# space complexity = O(n) - storing all visited nodes
# ----------------------------------------------------

def detect_cycle_brute_force(head: Optional[ListNode]) -> Optional[ListNode]:
    visited = set()

    current = head
    while current:
        if current in visited:
            return current  # Found cycle start
        visited.add(current)
        current = current.next

    return None  # No cycle


# ----------------------------------------------------
# Test cases
# ----------------------------------------------------

if __name__ == "__main__":
    # Create linked list with cycle: 3 → 2 → 0 → -4 → (back to 2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # Creates cycle back to node2

    # Test Two Pointers solution
    result1 = detect_cycle(node1)
    print(f"Two Pointers: Cycle starts at node with value {result1.val if result1 else None}")  # 2

    # Test Brute Force solution
    result2 = detect_cycle_brute_force(node1)
    print(f"Brute Force: Cycle starts at node with value {result2.val if result2 else None}")  # 2

    # Test with no cycle
    no_cycle = ListNode(1, ListNode(2, ListNode(3)))
    print(f"\nNo cycle list:")
    print(f"Two Pointers: {detect_cycle(no_cycle)}")  # None
    print(f"Brute Force: {detect_cycle_brute_force(no_cycle)}")  # None
