"""
LeetCode 19: Remove Nth Node From End of List
Difficulty: Medium
Pattern: Linked List (Two-Pointer Fixed Window with Sentinel)

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy

        # Advance fast ahead by n + 1 steps to establish invariant gap
        for _ in range(n + 1):
            fast = fast.next

        # Move both until fast runs off the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Splice target node
        slow.next = slow.next.next

        return dummy.next