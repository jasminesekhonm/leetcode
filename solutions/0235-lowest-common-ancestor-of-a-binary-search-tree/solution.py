# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        lo, hi = None, None
        if p.val <= q.val:
            lo = p
            hi = q
        else:
            lo = q
            hi = p

        node = root
        while node:
            if lo.val <= node.val <= hi.val:
                return node 
            elif lo.val > node.val:
                node = node.right
            else:
                node = node.left
            
     
