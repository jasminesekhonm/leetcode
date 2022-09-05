# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def maxGain(node):
            if node is None:
                return 0
            nonlocal max_sum 
            right_gain = max(maxGain(node.right), 0)
            left_gain = max(maxGain(node.left), 0)
            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            return node.val + max(right_gain, left_gain)
        
        max_sum = -float('inf')
        maxGain(root)
        return max_sum
            
        
