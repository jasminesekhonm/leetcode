# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ptr1 = 0
        ptr2 = 0
        node1, node2 = list1, list2
        dummyNode = ListNode(0)
        newNode = dummyNode # ListNode(0)
        while node1 or node2:
            if node1 and (not node2 or (node1.val <= node2.val)):
                newNode.next = ListNode(node1.val)
                node1 = node1.next 
            else:
                newNode.next = ListNode(node2.val)
                node2 = node2.next 
            newNode = newNode.next 
        return dummyNode.next 
            
            
