# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        inorder = []

        def traverse(node):
            if node is None:
                return
            if node.left:
                traverse(node.left)
            inorder.append(node.val)
            if node.right:
                traverse(node.right)
        
        traverse(root)
        i, j = 0, len(inorder) - 1
        
        while i < j:
            currSum = inorder[i] + inorder[j]
            if currSum == k:
                return True
            elif currSum > k:
                j -= 1
            else:
                i += 1
        return False

                
