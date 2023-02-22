# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        nodes_in_B = set()

        node = headB 
        while node:
            nodes_in_B.add(node)
            node = node.next 

        node = headA 
        while node:
            if node in nodes_in_B:
                return node 
            node = node.next 
        return None 
