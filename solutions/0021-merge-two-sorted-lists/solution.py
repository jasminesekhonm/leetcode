# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # [1, 2, 4]
        # [1, 3, 4]
        
        # 1, 1, 2, 3, 4, 4
        
        # list1 pointer, l1 
        # list2 pointer, l2
        # elem1: list1[l1] and elem2: list1[l2]
        # do this until i have reached the end of both lists 
        # if elem1 < elem2 or elem2 is None:
        # append elem1 to the new linked list 
        # l1 += 1
        # else if elem2 < elem1 or elem1 is None:
        # l2 += 1
        
        dummyHead = ListNode(0)
        node1 = list1
        node2 = list2
        currNode = dummyHead
        while node1 is not None or node2 is not None:
            if node1 is None:
                currNode.next = node2
                node2 = node2.next 
            elif node2 is None:
                currNode.next = node1 
                node1 = node1.next 
            elif node1.val <= node2.val:
                currNode.next = node1 
                node1 = node1.next 
            elif node2.val < node1.val:
                currNode.next = node2 
                node2 = node2.next 
            currNode = currNode.next 
        return dummyHead.next 
            
        
