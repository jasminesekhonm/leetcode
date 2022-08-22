# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        i = 1
        node1, node2 = head, head
        while node2 is not None and node1 is not None:
            if i % 2 == 0:
                node1 = node1.next 
            node2 = node2.next 
            if node1 == node2:
                return True 
            i += 1
        return False
            
            
        
