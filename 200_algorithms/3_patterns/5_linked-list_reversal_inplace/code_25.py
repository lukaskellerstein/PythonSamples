
# -----------------------
# Reverse Nodes in k-Group (LeetCode 25)
# -----------------------

# Difficulty: Hard

# Problem: Given the head of a linked list, reverse the nodes of the list k at
# a time, and return the modified list. k is a positive integer and is less than
# or equal to the length of the linked list. If the number of nodes is not a
# multiple of k then left-out nodes at the end should remain as-is.

# -----------------------

# Input:  1 -> 2 -> 3 -> 4 -> 5,  k=3
# Output: 3 -> 2 -> 1 -> 4 -> 5


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


# Given: 1 -> 2 -> 3 -> 4 -> 5,  k=3
k = 3

# ----------------------------------------------------
# Iterative solution
#
# time complexity = O(n) - each node is visited at most twice (count + reverse)
# space complexity = O(1) - only pointers
#
# Key idea:
#   1. Count ahead to check if k nodes remain
#   2. Reverse the group of k nodes (same as LeetCode 206 loop)
#   3. Reconnect the reversed group to the previous tail
#   4. Repeat until fewer than k nodes remain
# ----------------------------------------------------


def reverse_k_group(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy  # node before the current group

    while True:
        # Step 1 — check if k nodes remain
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next  # fewer than k nodes left, done

        group_next = kth.next  # node after the current group

        # Step 2 — reverse k nodes
        prev = group_next  # after reversal, first node should point here
        curr = group_prev.next
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3 — reconnect
        # group_prev.next still points to the old first node (now tail)
        old_first = group_prev.next
        group_prev.next = prev  # prev is now the head of the reversed group

        # Step 4 — advance group_prev to the tail of the reversed group
        group_prev = old_first

    return dummy.next


# Example
head = build_list([1, 2, 3, 4, 5])
print_list(reverse_k_group(head, k))  # 3 -> 2 -> 1 -> 4 -> 5

# Example with k=2
head = build_list([1, 2, 3, 4, 5])
print_list(reverse_k_group(head, 2))  # 2 -> 1 -> 4 -> 3 -> 5

# Edge case: k equals list length
head = build_list([1, 2, 3])
print_list(reverse_k_group(head, 3))  # 3 -> 2 -> 1


# ----------------------------------------------------
# Recursive solution
#
# time complexity = O(n) - each node visited at most twice
# space complexity = O(n/k) - recursion stack, one frame per group
# ----------------------------------------------------


def reverse_k_group_recursive(head, k):
    # Check if there are at least k nodes
    node = head
    count = 0
    for _ in range(k):
        if not node:
            return head  # fewer than k nodes, return as-is
        node = node.next
        count += 1

    # Reverse k nodes
    prev = None
    curr = head
    for _ in range(k):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # head is now the tail of the reversed group
    # Recursively reverse the rest and connect
    head.next = reverse_k_group_recursive(curr, k)

    return prev  # new head of this group


# Example
head = build_list([1, 2, 3, 4, 5])
print_list(reverse_k_group_recursive(head, k))  # 3 -> 2 -> 1 -> 4 -> 5
