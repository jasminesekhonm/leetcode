# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        node1, node2 = l1, l2 
        carry = 0 
        dummyHead = ListNode(0)
        prev_node = dummyHead
        while node1 or node2 or (carry > 0):
            sum_ = (node1.val if node1 is not None else 0) + (node2.val if node2 is not None else 0) + carry 
            sum_, carry = sum_ % 10, sum_ // 10
            new_node = ListNode(sum_)
            prev_node.next = new_node 
            prev_node = new_node 
            if node1 is not None:
                node1 = node1.next 
            if node2 is not None: 
                node2 = node2.next 
        return dummyHead.next 

