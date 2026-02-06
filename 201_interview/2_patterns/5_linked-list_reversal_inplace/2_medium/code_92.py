from typing import Optional


# ============================================================
# PROBLEM: Reverse Linked List II (LeetCode 92)
# ============================================================
# Difficulty: Medium
# Pattern: Linked List Reversal In-Place (Partial Reversal)
#
# Given the head of a singly linked list and two integers left and right
# where left <= right, reverse the nodes of the list from position left
# to position right, and return the reversed list. Positions are 1-indexed.
#
# ============================================================
# EXAMPLES
# ============================================================
#
# Example 1:
#   Input: head = [1, 2, 3, 4, 5], left = 2, right = 4
#   Output: [1, 4, 3, 2, 5]
#   Explanation: Reverse nodes from position 2 to 4.
#
# Example 2:
#   Input: head = [5], left = 1, right = 1
#   Output: [5]
#
# ============================================================
# CONSTRAINTS
# ============================================================
#
# - The number of nodes in the list is n
# - 1 <= n <= 500
# - -500 <= Node.val <= 500
# - 1 <= left <= right <= n
#
# ============================================================
# VISUALIZATION
# ============================================================
#
# Input:  1 -> 2 -> 3 -> 4 -> 5,  left=2, right=4
#
# Step 1: Identify "before" node (node at position left-1)
#         before = node(1)
#
# Step 2: Reverse sublist from position 2 to 4:
#         1 -> [2 -> 3 -> 4] -> 5
#              becomes
#         1 -> [4 -> 3 -> 2] -> 5
#
# Step 3: Reconnect:
#         before.next = new head of reversed section (4)
#         old head of reversed section (2).next = node after right (5)
#
# Output: 1 -> 4 -> 3 -> 2 -> 5
#


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


# ============================================================
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====


def reverse_between_brute_force(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    pass


# ===== END CODE =====


# ============================================================
# PART 2 -- OPTIMAL SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====


def reverse_between(
    head: Optional[ListNode], left: int, right: int
) -> Optional[ListNode]:
    pass


# ===== END CODE =====


# ============================================================
# PART 3 -- TEST CASES
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


# ===== YOUR CODE =====

if __name__ == "__main__":
    test_cases = [
        {
            "args": ([1, 2, 3, 4, 5], 2, 4),
            "expected": [1, 4, 3, 2, 5]
        },
        {
            "args": ([5], 1, 1),
            "expected": [5]
        },
    ]

    for test in test_cases:
        values, left, right = test["args"]
        expected = test["expected"]

        result1 = list_to_array(reverse_between_brute_force(build_list(values), left, right))
        result2 = list_to_array(reverse_between(build_list(values), left, right))

        assert result1 == expected, f"Brute force failed for {test['args']}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {test['args']}: got {result2}, expected {expected}"

        print(f"args={test['args']}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
