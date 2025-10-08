from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = 0, 0

        power = 0
        while l1 != None:
            n1 += l1.val * (10 ** power)
            power += 1
            l1 = l1.next

        power = 0
        while l2 != None:
            n2 += l2.val * (10 ** power)
            power += 1
            l2 = l2.next

        n = n1 + n2
        n = (str(n))[::-1]
        output = ListNode(int(n[0]), None)
        pivot = output
        for digit in n[1:]:
            dummy = ListNode(int(digit), None)
            pivot.next = dummy
            pivot = dummy
        return output
