# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:

        dummy_head = ListNode(0)
        dummy_head.next = head 
        slow = fast = dummy_head 

        length = 0
        while fast.next:
            fast = fast.next
            length += 1
        
        if length == 0:
            return head 
            
        k %= length
        for j in range(length-k):
            slow = slow.next 

        tmp = dummy_head.next 
        fast.next = tmp 

        dummy_head.next = slow.next 
        slow.next = None 

        return dummy_head.next




            



        

        
