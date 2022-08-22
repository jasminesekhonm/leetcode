# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        output = []
        currNode = head
        while currNode is not None:
            output.append(currNode.val)
            currNode = currNode.next 
        
        heapq.heapify(output)
        dummyHead = ListNode(None)
        currNode = dummyHead
        while output:
            val = heapq.heappop(output)
            newNode = ListNode(val)
            currNode.next = newNode 
            currNode = newNode 
        currNode.next = None 
        return dummyHead.next 
            
            
        
