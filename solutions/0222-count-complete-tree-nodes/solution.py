# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        count = 0
        
        if root is None:
            return count
        
        node = root
        q = []
        q.append(root)
        
        while q:
            node = q.pop()
            count+=1
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        return count
        
