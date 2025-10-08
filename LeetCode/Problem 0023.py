# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists):
        new_list = []
        for head in lists:
            if head != None:
                new_list.append(head)
        lists = new_list
        if not lists:
            return None

        dummy_node = ListNode(-(10**5), None)
        last_node = dummy_node
        new_head = dummy_node

        pivots = []
        for head in lists:
            pivots.append(head)

        while True:
            least_value = float('inf')
            new_node_ind = 0
            for ind, pivot in enumerate(pivots):
                if pivot.val < least_value:
                    least_value = pivot.val
                    new_node_ind = ind

            if new_head == dummy_node:
                new_head = pivots[new_node_ind]
                last_node = new_head
            else:
                last_node.next = pivots[new_node_ind]
                last_node = pivots[new_node_ind]

            if pivots[new_node_ind].next == None:
                pivots.pop(new_node_ind)
            else:
                pivots[new_node_ind] = pivots[new_node_ind].next

            if len(pivots) == 0:
                break

        return new_head
