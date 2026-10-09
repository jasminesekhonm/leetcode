# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        
        dummy_head = ListNode(0)

        min_heap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(min_heap, (node.val, i, node))
        
        new_node = dummy_head 

        while min_heap:
            (node_val, i, node) = heapq.heappop(min_heap)
            new_node.next = ListNode(node_val)
            new_node = new_node.next
            if node.next:
                node = node.next 
                heapq.heappush(min_heap, (node.val, i, node))
        
        return dummy_head.next 
            
