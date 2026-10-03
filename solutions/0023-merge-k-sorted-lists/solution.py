# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq 

class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        
        dummy = ListNode(0, None)

        heap = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(heap)
        
        tail = dummy
        
        while heap:
            min_node_val, i, min_node = heapq.heappop(heap)
            tail.next = ListNode(min_node_val, )
            tail = tail.next 

            if min_node.next:
                heapq.heappush(heap, (min_node.next.val, i, min_node.next))
        
        return dummy.next

        


        
    

            
            







        
