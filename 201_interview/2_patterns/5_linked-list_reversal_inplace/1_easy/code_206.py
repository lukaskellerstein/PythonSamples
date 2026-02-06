from typing import Optional


# ============================================================
# PROBLEM: Reverse Linked List (LeetCode 206)
# ============================================================
# Difficulty: Easy
# Pattern: Linked List Reversal In-Place
#
# Given the head of a singly linked list, reverse the list and return
# the reversed list. This is the foundational linked list problem --
# master it before attempting any other reversal variant.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: head = [1, 2, 3, 4, 5]
#   Output: [5, 4, 3, 2, 1]
#
# Example 2:
#   Input: head = [1, 2]
#   Output: [2, 1]
#
# Example 3:
#   Input: head = []
#   Output: []
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the list is in the range [0, 5000]
# - -5000 <= Node.val <= 5000
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Input:   1 -> 2 -> 3 -> 4 -> 5 -> None
#
# Step 1:  None <- 1    2 -> 3 -> 4 -> 5 -> None
#                 prev  curr
#
# Step 2:  None <- 1 <- 2    3 -> 4 -> 5 -> None
#                       prev curr
#
# Step 3:  None <- 1 <- 2 <- 3    4 -> 5 -> None
#                            prev curr
#
# Step 4:  None <- 1 <- 2 <- 3 <- 4    5 -> None
#                                 prev curr
#
# Step 5:  None <- 1 <- 2 <- 3 <- 4 <- 5
#                                      prev  curr=None
#
# Output:  5 -> 4 -> 3 -> 2 -> 1 -> None
#


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# ============================================================
# PART 1 — ITERATIVE SOLUTION
# ============================================================
# TODO: Describe your iterative approach (three-pointer technique)
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


# ============================================================
# PART 2 — RECURSIVE SOLUTION
# ============================================================
# TODO: Describe your recursive approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
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
