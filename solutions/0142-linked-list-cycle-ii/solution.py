# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seenNodes = set() 

        node = head 
        while node:
            if node not in seenNodes:
                seenNodes.add(node)
                node = node.next 
            else:
                return node 
        return None 
        
