# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ptr = -n 
        dummyNode = ListNode(0)
        dummyNode.next = head 

        node = dummyNode
        while ptr <= 0 and node:
            node = node.next 
            ptr += 1
        
        secondNode = dummyNode 

        while node:
            node = node.next 
            secondNode = secondNode.next 

        secondNode.next = secondNode.next.next 
        return dummyNode.next 
