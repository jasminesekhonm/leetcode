# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        
        dummy = ListNode(0)

        node1 = list1
        node2 = list2 

        node = dummy 
        while node1 and node2:
            if (node1.val <= node2.val):
                node.next = node1
                node1 = node1.next 
            else:
                node.next = node2
                node2 = node2.next 
            node = node.next
        if node1:
            node.next = node1 
        
        if node2:
            node.next = node2

        return dummy.next  


