# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        listVals = []

        node = head 
        while node:
            listVals.append(node.val)
            node = node.next 
        
        return listVals == listVals[::-1]
