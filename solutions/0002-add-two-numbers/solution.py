# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        node1 = l1
        node2 = l2 
        dummyNode = ListNode()
        prevNode = dummyNode
        while node1 or node2 or carry > 0:
            node1Val = 0 if node1 is None else node1.val
            node2Val = 0 if node2 is None else node2.val 
            sumVal = node1Val + node2Val + carry
            sumVal, carry = sumVal % 10, sumVal // 10
            currNode = ListNode(sumVal)
            prevNode.next = currNode
            prevNode = currNode
            if not node1 is None:
                node1 = node1.next 
            if not node2 is None:
                node2 = node2.next 
        return dummyNode.next
         
                
                
        
        
