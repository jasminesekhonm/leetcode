# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(0)
        op = dummyHead
        carry = 0
        node1, node2 = l1, l2
        while node1 != None or node2 != None or carry != 0:
        
            num = (node1.val if node1 else 0) + (node2.val if node2 else 0) + carry 
            if num < 10:
                new_node = ListNode(val=num)
                carry = 0
                
            else:
                new_node = ListNode(val=num % 10)
                carry = num // 10
                
            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None 
            op.next = new_node 
            op = new_node 
            
        return dummyHead.next 
            
        
        
                
        
