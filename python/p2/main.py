from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        li = ListNode()
        output = li
        while True:
            if l1 is None and l2 is None:
                if carry > 0:
                    li.next = ListNode(val=carry)
                break

            v1 = 0
            if l1 is not None:
                v1 = l1.val
                l1 = l1.next

            v2 = 0
            if l2 is not None:
                v2 = l2.val
                l2 = l2.next

            li.next = ListNode(val=(v1+v2+carry) % 10)
            li = li.next
            carry = (v1+v2+carry) // 10

        return output.next
