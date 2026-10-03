# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        preorder = deque(preorder)

        def helper(preorder, inorder):
            if not inorder:
                return None
            idx = inorder.index(preorder.popleft())

            root = TreeNode(inorder[idx])

            root.left = helper(preorder, inorder[:idx])
            root.right = helper(preorder, inorder[idx+1:])

            return root 



        return helper(preorder, inorder)

        
        
