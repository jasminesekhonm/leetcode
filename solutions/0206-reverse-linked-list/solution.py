# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        
        # 1 -> 2 -> 3

        # prev -> curr -> next

        # prev <- curr <- next

        prev, node = None, head

        while node:
            tmp = node.next
            node.next = prev
            prev, node = node, tmp

        return prev
            
