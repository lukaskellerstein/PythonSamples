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
# TODO: Describe your brute force approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def middle_node_brute_force(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


# ============================================================
# PART 2 -- OPTIMAL SOLUTION (Fast/Slow Pointers)
# ============================================================
# TODO: Describe your optimal approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


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


if __name__ == "__main__":
    # TODO: Write your test cases here
    test_cases = [
        ([1, 2, 3, 4, 5], 3),       # Odd length -> middle is 3
        ([1, 2, 3, 4, 5, 6], 4),    # Even length -> second middle is 4
        ([1], 1),                    # Single element -> 1
        ([1, 2], 2),                 # Two elements -> second middle is 2
    ]

    pass
