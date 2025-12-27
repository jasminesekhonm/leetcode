# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        prevNode = dummy 

        while head and head.next:
            firstNode = head 
            secondNode = head.next 

            prevNode.next = secondNode
            firstNode.next = secondNode.next
            secondNode.next = firstNode 

            prevNode = firstNode
            head = firstNode.next 

        return dummy.next
