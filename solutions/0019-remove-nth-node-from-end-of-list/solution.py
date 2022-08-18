# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # 1, 2, 3, 4, 5 
        # 1 -> 2 -> 3 -> 4 -> 5 -> None 
        # when I am at 5, the pointer is at 3, and my goal is to do node.next = node.next.next 
        dummy = ListNode(0)
        dummy.next = head 
        first = dummy
        second = dummy 
        for i in range(n):
            first = first.next 
        while first.next is not None:
            first = first.next 
            second = second.next 
        second.next = second.next.next 
        return dummy.next 
        
