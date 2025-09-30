# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # null -> 1 -> 2 -> 3 -> 4 -> 5
        # 1 -> 2 -> 3
        # curr = 1 
        # next = 2
        # tmp = next.next 
        # next.next = curr 
        # curr.next = prev 
        # curr = tmp 

        prev = None 
        curr = head 
        while curr:
            nextTemp = curr.next 
            curr.next = prev 
            prev = curr 
            curr = nextTemp
        
        return prev 

