# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        # 5 -> 4 -> 2 -> 1
        # 5 + 1, 4 + 2 
        
        stack = []
        
        node = head 
        
        while node:
            stack.append(node.val)
            node = node.next
            
        # [5, 4, 2, 1]
        n = len(stack) # 4 
        
        maxSum = -float('inf')
        i = 0
        j = n - 1
        
        while i < j:
            maxSum = max(maxSum, stack[i] + stack[j])
            i += 1
            j -= 1
            
        return maxSum
            
        
