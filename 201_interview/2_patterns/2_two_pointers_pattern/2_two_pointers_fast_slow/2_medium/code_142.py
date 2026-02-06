from typing import Optional


# ============================================================
# PROBLEM: Linked List Cycle II (LeetCode 142)
# ============================================================
# Difficulty: Medium
# Pattern: Fast/Slow Pointers (Floyd's Cycle Detection)
#
# Given the head of a linked list, return the node where the
# cycle begins. If there is no cycle, return None. Do not modify
# the linked list.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: head = [3, 2, 0, -4], cycle at pos 1
#   Output: Node with value 2
#   Explanation: The tail connects to the node at index 1.
#
# Example 2:
#   Input: head = [1, 2], cycle at pos 0
#   Output: Node with value 1
#   Explanation: The tail connects to the node at index 0.
#
# Example 3:
#   Input: head = [1], no cycle
#   Output: None
#   Explanation: There is no cycle in the linked list.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the list is in the range [0, 10^4]
# - -10^5 <= Node.val <= 10^5
# - pos is -1 (no cycle) or a valid index in the linked list
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Example: 3 -> 2 -> 0 -> -4
#               ^           |
#               +-----------|
#
# The cycle begins at node with value 2.
#
# Floyd's Algorithm (Tortoise and Hare):
#   Phase 1: Detect cycle
#     - slow moves 1 step, fast moves 2 steps
#     - if they meet, a cycle exists
#
#   Phase 2: Find cycle start
#     - reset one pointer to head
#     - move both at same speed (1 step)
#     - they meet at the cycle start
#
# Why Phase 2 works:
#   Let D = distance from head to cycle start
#   Let C = cycle length
#   When slow and fast meet inside the cycle,
#   slow is D steps from the cycle start (going forward around the cycle).
#   So moving one pointer from head and one from meeting point
#   at the same speed, they meet at cycle start after D steps.
#


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (HashSet)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def detect_cycle_brute_force(head: Optional[ListNode]) -> Optional[ListNode]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Floyd's Cycle Detection)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def detect_cycle(head: Optional[ListNode]) -> Optional[ListNode]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

# ===== YOUR CODE =====

if __name__ == "__main__":
    # Test 1: Cycle at node with value 2
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    result1 = detect_cycle_brute_force(node1)
    result2 = detect_cycle(node1)
    assert result1 == node2, f"Brute force failed: expected node(2), got {result1}"
    assert result2 == node2, f"Optimal failed: expected node(2), got {result2}"
    print(f"Test 1 (cycle at 2): brute_force={result1.val}, optimal={result2.val} ✓")

    # Test 2: No cycle
    no_cycle = ListNode(1, ListNode(2, ListNode(3)))
    result1 = detect_cycle_brute_force(no_cycle)
    result2 = detect_cycle(no_cycle)
    assert result1 is None, f"Brute force failed: expected None, got {result1}"
    assert result2 is None, f"Optimal failed: expected None, got {result2}"
    print(f"Test 2 (no cycle): brute_force={result1}, optimal={result2} ✓")

    # Test 3: Single node with self-cycle
    single = ListNode(1)
    single.next = single
    result1 = detect_cycle_brute_force(single)
    result2 = detect_cycle(single)
    assert result1 == single, f"Brute force failed: expected node(1)"
    assert result2 == single, f"Optimal failed: expected node(1)"
    print(f"Test 3 (self-cycle): brute_force={result1.val}, optimal={result2.val} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
