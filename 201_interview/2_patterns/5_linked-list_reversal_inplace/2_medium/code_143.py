from typing import Optional


# ============================================================
# PROBLEM: Reorder List (LeetCode 143)
# ============================================================
# Difficulty: Medium
# Pattern: Linked List Reversal In-Place (Find Middle + Reverse + Merge)
#
# Given the head of a singly linked list, reorder it to:
# L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
# You may not modify the values in the list's nodes. Only nodes
# themselves may be changed.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: head = [1, 2, 3, 4]
#   Output: [1, 4, 2, 3]
#
# Example 2:
#   Input: head = [1, 2, 3, 4, 5]
#   Output: [1, 5, 2, 4, 3]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the list is in the range [1, 5 * 10^4]
# - 1 <= Node.val <= 1000
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Input:  1 -> 2 -> 3 -> 4 -> 5
#
# Step 1: Find middle using slow/fast pointers
#         1 -> 2 -> 3    4 -> 5
#         (first half)   (second half)
#
# Step 2: Reverse second half
#         1 -> 2 -> 3    5 -> 4
#
# Step 3: Merge alternately
#         1 -> 5 -> 2 -> 4 -> 3
#
# Output: 1 -> 5 -> 2 -> 4 -> 3
#


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# ============================================================
# PART 1 — BRUTE FORCE SOLUTION
# ============================================================
# TODO: Describe your brute force approach (e.g., collect nodes into array, reorder)
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def reorder_list_brute_force(head: Optional[ListNode]) -> None:
    pass


# ============================================================
# PART 2 — OPTIMAL SOLUTION
# ============================================================
# TODO: Describe your optimal in-place approach (find middle, reverse, merge)
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def reorder_list(head: Optional[ListNode]) -> None:
    pass


# ============================================================
# PART 3 — TEST CASES
# ============================================================


def build_list(values: list) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def list_to_array(head: Optional[ListNode]) -> list:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


if __name__ == "__main__":
    # TODO: Write your test cases here
    pass
