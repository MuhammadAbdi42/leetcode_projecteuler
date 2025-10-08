from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None

        dummy_node = ListNode(-1, None)

        index = head
        while True:
            if index == None:
                return head
            if index == head:
                if index.next != None:
                    third_node = index.next.next
                    second_node = index.next

                    second_node.next = index
                    index.next = third_node

                    head = second_node
                    pre_index = index
                    index = third_node
                else:
                    return head
            else:
                if index.next != None:
                    third_node = index.next.next
                    second_node = index.next

                    second_node.next = index
                    index.next = third_node

                    pre_index.next = second_node

                    pre_index = index
                    index = third_node
                else:
                    return head
