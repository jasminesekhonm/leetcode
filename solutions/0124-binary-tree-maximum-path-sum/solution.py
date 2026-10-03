# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        self.max_sum = -float('inf')
        def traverse_tree(node):
            if not node:
                return 0 
            left = max(0, traverse_tree(node.left))
            right = max(0, traverse_tree(node.right))

            gain = node.val + left + right 
            if gain > self.max_sum:
                self.max_sum = gain 

            return node.val + max(left, right)

            
        traverse_tree(root)
        return self.max_sum
