
# -----------------------
# Reverse Linked List II (LeetCode 92)
# -----------------------

# Difficulty: Medium

# Problem: Given the head of a singly linked list and two integers left and
# right where left <= right, reverse the nodes of the list from position left
# to position right, and return the reversed list. Positions are 1-indexed.

# -----------------------

# Input:  1 -> 2 -> 3 -> 4 -> 5,  left=2, right=4
# Output: 1 -> 4 -> 3 -> 2 -> 5


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def print_list(head):
    parts = []
    while head:
        parts.append(str(head.val))
        head = head.next
    print(" -> ".join(parts))


# Given: 1 -> 2 -> 3 -> 4 -> 5,  left=2, right=4
left = 2
right = 4

# ----------------------------------------------------
# One-pass solution (with dummy node)
#
# time complexity = O(n) - single pass through the list
# space complexity = O(1) - only a few pointers
#
# Key idea:
#   1. Walk to the node just before `left` (call it `before`)
#   2. Reverse the sublist of (right - left + 1) nodes in place
#   3. Reconnect: before.next -> new sublist head,
#                 old sublist head (now tail) -> node after `right`
# ----------------------------------------------------


def reverse_between(head, left, right):
    # Dummy node handles the edge case where left == 1 (no preceding node)
    dummy = ListNode(0, head)

    # Step 1 — move `before` to the node just before position `left`
    before = dummy
    for _ in range(left - 1):
        before = before.next

    # Step 2 — reverse (right - left + 1) nodes starting from before.next
    prev = None
    curr = before.next
    for _ in range(right - left + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # Step 3 — reconnect
    # before.next is still pointing at the old first node of the sublist
    # (which is now the tail of the reversed sublist)
    before.next.next = curr  # tail -> node after reversed section
    before.next = prev       # before -> new head of reversed section

    return dummy.next


# Example
head = build_list([1, 2, 3, 4, 5])
print_list(reverse_between(head, left, right))  # 1 -> 4 -> 3 -> 2 -> 5

# Edge case: left == 1
head = build_list([1, 2, 3, 4, 5])
print_list(reverse_between(head, 1, 3))  # 3 -> 2 -> 1 -> 4 -> 5

# Edge case: single element range
head = build_list([1, 2, 3, 4, 5])
print_list(reverse_between(head, 3, 3))  # 1 -> 2 -> 3 -> 4 -> 5


# ----------------------------------------------------
# Brute Force solution (extract to array, reverse, rebuild)
#
# time complexity = O(n) - two passes
# space complexity = O(n) - stores values in array
# ----------------------------------------------------


def reverse_between_brute_force(head, left, right):
    # Collect all values
    values = []
    curr = head
    while curr:
        values.append(curr.val)
        curr = curr.next

    # Reverse the subarray (convert to 0-indexed)
    values[left - 1 : right] = values[left - 1 : right][::-1]

    # Rebuild the list
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


# Example
head = build_list([1, 2, 3, 4, 5])
print_list(reverse_between_brute_force(head, left, right))  # 1 -> 4 -> 3 -> 2 -> 5
