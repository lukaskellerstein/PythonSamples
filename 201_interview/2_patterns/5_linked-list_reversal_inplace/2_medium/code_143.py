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
# PART 1 -- BRUTE FORCE SOLUTION
# ============================================================

# ===== YOUR ANSWER =====
# Approach: ???
# Time Complexity: O(???)
# Space Complexity: O(???)
# ===== END ANSWER =====

# ===== YOUR CODE =====


def reorder_list_brute_force(head: Optional[ListNode]) -> None:
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


def reorder_list(head: Optional[ListNode]) -> None:
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
            "args": [1, 2, 3, 4],
            "expected": [1, 4, 2, 3]
        },
        {
            "args": [1, 2, 3, 4, 5],
            "expected": [1, 5, 2, 4, 3]
        },
    ]

    for test in test_cases:
        values = test["args"]
        expected = test["expected"]

        head1 = build_list(values)
        reorder_list_brute_force(head1)
        result1 = list_to_array(head1)

        head2 = build_list(values)
        reorder_list(head2)
        result2 = list_to_array(head2)

        assert result1 == expected, f"Brute force failed for {values}: got {result1}, expected {expected}"
        assert result2 == expected, f"Optimal failed for {values}: got {result2}, expected {expected}"

        print(f"values={values}, expected={expected}, brute_force={result1}, optimal={result2} ✓")

    print("\nAll tests passed!")

# ===== END CODE =====
