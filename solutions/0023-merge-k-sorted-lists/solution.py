# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        stack = []
        for linkedList in lists:
            node = linkedList
            while node:
                stack.append(node.val)
                node = node.next 
            
        stack = sorted(stack)
        
        dummyHead = ListNode(val=None)
        
        prev_node = dummyHead
        
        for i in range(len(stack)):
            node = ListNode(val=stack[i])
            prev_node.next = node 
            prev_node = node 
            
        return dummyHead.next 
            
            
            
        
        
                
                
                
            
        
