# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        node1 =  head
        dummy = ListNode(0, head) 

        node2 = dummy
        for _ in range(n):
            node1 = node1.next 

        while node1:
            node1 = node1.next
            node2 = node2.next 

        node2.next = node2.next.next 
        return dummy.next 
