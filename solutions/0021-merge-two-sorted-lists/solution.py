# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        dummyHead = ListNode(0)
        node = dummyHead
        node1, node2 = list1, list2 
        while node1 and node2:
            if node1.val <= node2.val:
                node.next = node1
                node1 = node1.next 
            elif node2.val < node1.val:
                node.next = node2
                node2 = node2.next 
            node = node.next 
        if node1 or node2:
            node.next = node1 if node1 else node2 

        return dummyHead.next
        
