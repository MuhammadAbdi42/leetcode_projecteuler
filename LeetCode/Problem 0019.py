from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummyNode = ListNode(-1, None)
        nodes = []
        if head != None:
            pivot: ListNode = head
        else:
            return None

        while pivot.val != -1:
            nodes.append(pivot)
            if pivot.next != None:
                pivot = pivot.next
            else:
                pivot = dummyNode

        index = len(nodes) - n

        if index - 1 >= 0:
            if index + 1 < len(nodes):
                nodes[index - 1].next = nodes[index + 1]
                return nodes[0]
            else:
                nodes[index - 1].next = None
                return nodes[0]
        else:
            if index + 1 < len(nodes):
                return nodes[index + 1]
            else:
                return None
