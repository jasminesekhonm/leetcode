# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        def build_tree(preorder, inorder):
            if len(inorder) == 0:
                return 
            
            split_index = inorder.index(preorder.popleft())
            node = TreeNode(inorder[split_index])

            left_tree = inorder[:split_index]
            right_tree = inorder[split_index+1:]
            node.left = build_tree(preorder,left_tree)
            node.right = build_tree(preorder, right_tree)

            return node

        preorder = deque(preorder)
        return build_tree(preorder, inorder)


            
        
