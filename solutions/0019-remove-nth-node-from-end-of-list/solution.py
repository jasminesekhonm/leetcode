# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        
        first_node = dummy
        second_node = dummy
        
        i = 0
        while i <= n and first_node:
            first_node = first_node.next 
            i += 1
            
        while first_node and second_node:
            first_node = first_node.next 
            second_node = second_node.next 
        
        second_node.next = second_node.next.next 
        return dummy.next 
