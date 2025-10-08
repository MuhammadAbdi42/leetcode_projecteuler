from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []

        index = head
        while index != None:
            nodes.append(index)
            index = index.next

        slicing_indexes = list(range(0, len(nodes) - 1, k))
        if slicing_indexes == []:
            return nodes[0]
        if slicing_indexes[-1] + k > len(nodes):
            slicing_indexes.pop(-1)

        for i in slicing_indexes:
            for j in range(k):
                pivot = (i + k - 1) - j
                if pivot == i:
                    continue
                else:
                    nodes[pivot].next = nodes[pivot - 1]

        for i in slicing_indexes:
            if i != slicing_indexes[-1]:
                nodes[i].next = nodes[i + 2 * k - 1]
            else:
                if i + k <= len(nodes) - 1:
                    nodes[i].next = nodes[i + k]
                else:
                    nodes[i].next = None

        return nodes[k - 1]
