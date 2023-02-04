# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        height = 0
        maxDepth = 0

        def traverse(node, height):
            nonlocal maxDepth 
            if node is None: 
                return 
            if node.left is not None:
                traverse(node.left, height+1)
            if node.right is not None:
                traverse(node.right, height+1)
            if node.right is None and node.left is None:
                maxDepth = max(maxDepth, height)
        
        traverse(root, 1)
        return maxDepth


            
            

            
