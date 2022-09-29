# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        root = TreeNode(val=preorder[0])

        i = 1
        # populate left subtree
        leftSubtree = []
        while i < len(preorder) and preorder[i] < root.val:
            leftSubtree.append(preorder[i])
            i += 1
        if len(leftSubtree) > 0:    
            root.left = self.bstFromPreorder(leftSubtree)
        rightSubtree = []
        while i < len(preorder):
            rightSubtree.append(preorder[i])
            i += 1
        if len(rightSubtree) > 0:
            root.right = self.bstFromPreorder(rightSubtree)
        return root 
            
