from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        list_out = ListNode()
        linked_list = list_out
        while True:
            if list1 is None:
                list_out.next = list2
                break
            elif list2 is None:
                list_out.next = list1
                break

            if list1.val <= list2.val:
                next_node = ListNode(list1.val)
                list1 = list1.next
            else:
                next_node = ListNode(list2.val)
                list2 = list2.next

            # set next node and move list_out ptr to this node
            list_out.next = next_node
            list_out = list_out.next

        # return node after head since head is empty node
        return linked_list.next
