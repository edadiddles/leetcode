from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = ListNode()
        while True:
            if head is None:
                break

            tail.val = head.val
            tail = ListNode(next=tail)
            head = head.next

        return tail.next
