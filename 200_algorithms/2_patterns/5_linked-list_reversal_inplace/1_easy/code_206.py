
# -----------------------
# Reverse Linked List (LeetCode 206)
# -----------------------

# Difficulty: Easy (warm-up — master this before touching anything else)

# Problem: Given the head of a singly linked list, reverse the list, and return
# the reversed list.

# -----------------------

# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1


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
# Iterative solution (three-pointer)
#
# time complexity = O(n) - single pass through the list
# space complexity = O(1) - only three pointers
# ----------------------------------------------------


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next   # save next node
        curr.next = prev  # reverse the link
        prev = curr       # advance prev
        curr = nxt        # advance curr

    return prev


# Example
head = build_list([1, 2, 3, 4, 5])
print_list(reverse_list(head))  # 5 -> 4 -> 3 -> 2 -> 1


# ----------------------------------------------------
# Recursive solution
#
# time complexity = O(n) - visit each node once
# space complexity = O(n) - recursion stack
# ----------------------------------------------------


def reverse_list_recursive(head):
    # if empty list or single node
    if not head or not head.next:
        return head

    # Reverse the rest of the list
    new_head = reverse_list_recursive(head.next)

    # "make the node ahead of me point back to me" (reverse the arrow)
    head.next.next = head
    # "remove my forward pointer" (it'll get re-set by the caller above, except for the original head which should point to None)
    head.next = None

    return new_head


# Example
head = build_list([1, 2, 3, 4, 5])
print_list(reverse_list_recursive(head))  # 5 -> 4 -> 3 -> 2 -> 1
