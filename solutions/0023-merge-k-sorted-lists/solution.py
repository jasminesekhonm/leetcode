import heapq

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        

        dummy = ListNode(0)
        new = dummy

        min_heap = []

        for i, node in enumerate(lists):
            if node:
                min_heap.append((node.val, i, node))

        heapq.heapify(min_heap)

        
        while min_heap:
            (val, i, node) = heapq.heappop(min_heap)
            new.next = ListNode(val)
            new = new.next 
            if node.next:
                node = node.next 
                heapq.heappush(min_heap, (node.val, i, node))

        return dummy.next
