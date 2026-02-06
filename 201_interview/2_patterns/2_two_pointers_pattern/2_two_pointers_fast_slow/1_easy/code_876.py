from typing import Optional, List


# ============================================================
# PROBLEM: Middle of the Linked List (LeetCode 876)
# ============================================================
# Difficulty: Easy
# Pattern: Fast/Slow Pointers (Tortoise and Hare)
#
# Given the head of a singly linked list, return the middle node
# of the linked list. If there are two middle nodes, return the
# second middle node.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: head = [1, 2, 3, 4, 5]
#   Output: Node with value 3
#   Explanation: The middle node of the list is node 3.
#
# Example 2:
#   Input: head = [1, 2, 3, 4, 5, 6]
#   Output: Node with value 4
#   Explanation: There are two middle nodes 3 and 4, return the second one.
#
# Example 3:
#   Input: head = [1]
#   Output: Node with value 1
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the list is in the range [1, 100]
# - 1 <= Node.val <= 100
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Odd length: [1, 2, 3, 4, 5]
#
#   Step 0: slow=1, fast=1
#   Step 1: slow=2, fast=3
#   Step 2: slow=3, fast=5  <- fast reached end, slow is at middle
#
# Even length: [1, 2, 3, 4, 5, 6]
#
#   Step 0: slow=1, fast=1
#   Step 1: slow=2, fast=3
#   Step 2: slow=3, fast=5
#   Step 3: slow=4, fast=None <- fast.next is None, slow is at 2nd middle
#
# When fast reaches the end at 2x speed, slow is exactly halfway.
#


class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION (Array Conversion)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def middle_node_brute_force(head: Optional[ListNode]) -> Optional[ListNode]:
    pass

# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Fast/Slow Pointers)
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====

def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    pass

# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
# ============================================================

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": [1, 2, 3, 4, 5],
            "expected": 3
        },
        {
            "args": [1, 2, 3, 4, 5, 6],
            "expected": 4
        },
        {
            "args": [1],
            "expected": 1
        },
        {
            "args": [1, 2],
            "expected": 2
        },
    ]

    for test in test_cases:
        values = test["args"]
        expected = test["expected"]

        head1 = create_linked_list(values)
        head2 = create_linked_list(values)

        result1 = middle_node_brute_force(head1)
        result2 = middle_node(head2)

        assert result1 and result1.val == expected, f"Brute force failed for {values}: got {result1.val if result1 else None}, expected {expected}"
        assert result2 and result2.val == expected, f"Optimal failed for {values}: got {result2.val if result2 else None}, expected {expected}"

        print(f"values={values}, expected={expected}, brute_force={result1.val}, optimal={result2.val} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
