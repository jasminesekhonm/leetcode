# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        node1, node2 = head, head 
        i = 1
        while node1 and node2: 
            if i % 2 == 0:
                node1 = node1.next 
            node2 = node2.next 
            i += 1
            if node1 == node2:
                return True 
        return False 




