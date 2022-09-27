# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        node = head 
        while node:
            arr.append(node)
            node = node.next 
        
        n = len(arr)
        return arr[n//2] 
