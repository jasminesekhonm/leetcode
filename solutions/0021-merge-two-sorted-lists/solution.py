# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2 = list1, list2
        dummyNode = ListNode(0)

        node = dummyNode

        while node1 or node2:
            if node1 is not None and node2 is not None: 
                if node1.val <= node2.val:
                    newNode = ListNode(node1.val)
                    node1 = node1.next 
                else:
                    newNode = ListNode(node2.val)
                    node2 = node2.next 
            elif node1 is None:
                newNode = ListNode(node2.val)
                node2 = node2.next 
            elif node2 is None:
                newNode = ListNode(node1.val)
                node1 = node1.next 
            node.next = newNode 
            node = newNode 
        return dummyNode.next 


