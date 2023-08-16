# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummyHead = ListNode(0)
        dummyHead.next = head 

        currNode = dummyHead
        i = 0
        while currNode.next:
            currNode = currNode.next
            i += 1

        lenlist = i 

        
        ptr = -int(i/2)
        currNode = dummyHead
        while ptr < 0 and currNode.next:
            currNode = currNode.next
            print(currNode.val)
            ptr += 1
        
        if currNode:
            currNode.next = currNode.next.next 
        return dummyHead.next

        
