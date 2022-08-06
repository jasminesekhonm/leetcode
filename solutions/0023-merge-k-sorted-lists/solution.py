class Solution(object):
    def mergeKLists(self, lists):
        stack = []
        for l in lists:
            node = l
            while node:
                stack.append(node.val)
                node = node.next 
                
        stack = sorted(stack)
        
        dummyHead = ListNode(val=0, next=None)
        
        node = dummyHead
        
        for other_node in stack:
            next_node = ListNode(other_node, next=None)
            node.next = next_node 
            node = next_node 
        return dummyHead.next 
            
