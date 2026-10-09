# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        
        dummy = ListNode(0)
        dummy.next = head 

        slow = fast = dummy 

        i = 0 
        while i < n and fast.next:
            fast = fast.next 
            i += 1
        
        while fast.next:
            fast = fast.next
            slow = slow.next 
        
        slow.next = slow.next.next

        return dummy.next

