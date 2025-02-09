# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode(0)
        currNode = dummyNode
        node1, node2 = list1, list2

        while node1 or node2:
            if node2 is None:
                currNode.next = node1 
                node1 = node1.next 
            elif node1 is None:
                currNode.next = node2
                node2 = node2.next
            elif node1.val <= node2.val:
                currNode.next = node1 
                node1 = node1.next 
            else:
                currNode.next = node2
                node2 = node2.next 
            currNode = currNode.next 

        return dummyNode.next 

                
        
