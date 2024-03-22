# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        listOfNodes = []
        node = head 
        while node:
            listOfNodes.append(node.val)
            node = node.next 

        return (listOfNodes == listOfNodes[::-1])
        
