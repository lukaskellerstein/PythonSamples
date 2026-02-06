from typing import Optional


# ============================================================
# PROBLEM: Reverse Nodes in k-Group (LeetCode 25)
# ============================================================
# Difficulty: Hard
# Pattern: Linked List Reversal In-Place (Group Reversal)
#
# Given the head of a linked list, reverse the nodes of the list k at
# a time, and return the modified list. k is a positive integer and is
# less than or equal to the length of the linked list. If the number of
# nodes is not a multiple of k, then the left-out nodes at the end
# should remain as-is. You may not alter the values in the nodes, only
# the nodes themselves may be changed.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: head = [1, 2, 3, 4, 5], k = 2
#   Output: [2, 1, 4, 3, 5]
#   Explanation: Reverse in groups of 2. Last node (5) remains as-is.
#
# Example 2:
#   Input: head = [1, 2, 3, 4, 5], k = 3
#   Output: [3, 2, 1, 4, 5]
#   Explanation: Reverse first group of 3. Remaining 2 nodes stay as-is.
#
# Example 3:
#   Input: head = [1, 2, 3, 4, 5], k = 1
#   Output: [1, 2, 3, 4, 5]
#   Explanation: No change when k = 1.
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the list is n
# - 1 <= k <= n <= 5000
# - 0 <= Node.val <= 1000
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Input:  1 -> 2 -> 3 -> 4 -> 5,  k = 3
#
# Group 1: [1 -> 2 -> 3] -> 4 -> 5
#   Check: 3 nodes available? Yes.
#   Reverse: [3 -> 2 -> 1] -> 4 -> 5
#   Reconnect: dummy -> 3 -> 2 -> 1 -> 4 -> 5
#              group_prev now points to node(1)
#
# Group 2: 3 -> 2 -> 1 -> [4 -> 5]
#   Check: 3 nodes available? No (only 2). Stop.
#
# Output: 3 -> 2 -> 1 -> 4 -> 5
#


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# ============================================================
# PART 1 — ITERATIVE SOLUTION
# ============================================================
# TODO: Describe your iterative approach (count ahead, reverse group, reconnect)
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def reverse_k_group(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    pass


# ============================================================
# PART 2 — RECURSIVE SOLUTION
# ============================================================
# TODO: Describe your recursive approach
#
# Time Complexity: O(???)
# Space Complexity: O(???)


def reverse_k_group_recursive(
    head: Optional[ListNode], k: int
) -> Optional[ListNode]:
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
