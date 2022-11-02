# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = -n 
        dummyNode = ListNode(0)
        dummyNode.next = head 
        node = dummyNode
        while i < 0 and node.next:
            node = node.next
            i += 1
        secondNode = dummyNode 
        while secondNode.next and node.next:
            node = node.next 
            secondNode = secondNode.next 
        secondNode.next = secondNode.next.next 
        return dummyNode.next 
        
            
        
