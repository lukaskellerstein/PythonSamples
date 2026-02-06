
# -----------------------
# Reorder List (LeetCode 143)
# -----------------------

# Difficulty: Medium

# Problem: Given the head of a singly linked list, reorder it to:
# L0 -> Ln -> L1 -> Ln-1 -> L2 -> Ln-2 -> ...
# You may not modify the values in the list's nodes, only the nodes themselves.

# -----------------------

# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 1 -> 5 -> 2 -> 4 -> 3


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


# ----------------------------------------------------
# Three-step in-place solution
#
# time complexity = O(n) - each step is O(n)
# space complexity = O(1) - only pointers
#
# Key idea — decompose into three subproblems:
#   1. Find the middle (slow/fast pointers)
#   2. Reverse the second half
#   3. Merge the two halves alternately
# ----------------------------------------------------


def reorder_list(head):
    if not head or not head.next:
        return head

    # Step 1 — find the middle using slow/fast pointers
    # After this, slow points to the last node of the first half
    slow, fast = head, head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    # Step 2 — reverse the second half (starting after slow)
    prev = None
    curr = slow.next
    slow.next = None  # cut the list in two

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    # prev is now the head of the reversed second half

    # Step 3 — merge two halves alternately
    first = head
    second = prev

    while second:
        # Save next pointers
        first_next = first.next
        second_next = second.next
        # Interleave
        first.next = second
        second.next = first_next
        # Advance
        first = first_next
        second = second_next

    return head


# Example (odd length)
head = build_list([1, 2, 3, 4, 5])
reorder_list(head)
print_list(head)  # 1 -> 5 -> 2 -> 4 -> 3

# Example (even length)
head = build_list([1, 2, 3, 4])
reorder_list(head)
print_list(head)  # 1 -> 4 -> 2 -> 3


# ----------------------------------------------------
# Brute Force solution (array-based)
#
# time complexity = O(n) - collect + rebuild
# space complexity = O(n) - stores all nodes in array
# ----------------------------------------------------


def reorder_list_brute_force(head):
    if not head:
        return head

    # Collect all nodes into an array
    nodes = []
    curr = head
    while curr:
        nodes.append(curr)
        curr = curr.next

    # Use two pointers from both ends
    left, right = 0, len(nodes) - 1

    while left < right:
        nodes[left].next = nodes[right]
        left += 1
        if left == right:
            break
        nodes[right].next = nodes[left]
        right -= 1

    # Terminate the list
    nodes[left].next = None

    return head


# Example
head = build_list([1, 2, 3, 4, 5])
reorder_list_brute_force(head)
print_list(head)  # 1 -> 5 -> 2 -> 4 -> 3
