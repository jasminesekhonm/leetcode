# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if not root:
            return 
        
        stack = [root]
        prev = None
        
        while stack:
            node = stack.pop()
            
            if node:
                stack.append(node.right)
                stack.append(node.left)
                
                if prev:
                    prev.right = node 
                    prev.left = None
                    node.left = None 
                
                prev = node 
