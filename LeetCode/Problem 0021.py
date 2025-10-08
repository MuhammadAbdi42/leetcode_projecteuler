from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        elif list1 == None:
            return list2
        elif list2 == None:
            return list1
        else:
            dummy_node = ListNode(-1000, None)
            new_head = dummy_node
            list_1_index, list_2_index = list1, list2

            while True:
                if new_head == dummy_node:
                    if list_1_index.val <= list_2_index.val:
                        new_head = list_1_index
                        last_node = new_head
                        if list_1_index.next == None:
                            list_1_index = dummy_node
                        else:
                            list_1_index = list_1_index.next
                    else:
                        new_head = list_2_index
                        last_node = new_head
                        if list_2_index.next == None:
                            list_2_index = dummy_node
                        else:
                            list_2_index = list_2_index.next

                else:
                    if list_1_index == dummy_node and list_2_index == dummy_node:
                        return new_head
                    elif list_1_index == dummy_node and list_2_index != dummy_node:
                        last_node.next = list_2_index
                        return new_head
                    elif list_2_index == dummy_node and list_1_index != dummy_node:
                        last_node.next = list_1_index
                        return new_head
                    else:
                        if list_1_index.val <= list_2_index.val:
                            last_node.next = list_1_index
                            last_node = last_node.next
                            if list_1_index.next == None:
                                list_1_index = dummy_node
                            else:
                                list_1_index = list_1_index.next
                        else:
                            last_node.next = list_2_index
                            last_node = last_node.next
                            if list_2_index.next == None:
                                list_2_index = dummy_node
                            else:
                                list_2_index = list_2_index.next
