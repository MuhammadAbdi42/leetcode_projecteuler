from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        pivot = head
        while pivot.next != None:
            if pivot.val == pivot.next.val:
                if pivot.next.next != None:
                    pivot.next = pivot.next.next
                else:
                    pivot.next = None
            else:
                pivot = pivot.next

        return head
