# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2 
        dummyNode = ListNode(0)
        node = dummyNode
        while node1 or node2:
            if (node1 and not node2) or (node1 and node2 and node1.val <= node2.val):
                node.next = ListNode(node1.val)
                node1 = node1.next
            elif (node2 and not node1) or (node1 and node2 and node1.val > node2.val):
                node.next = ListNode(node2.val)
                node2 = node2.next 
            node = node.next 
        return dummyNode.next
            


        
