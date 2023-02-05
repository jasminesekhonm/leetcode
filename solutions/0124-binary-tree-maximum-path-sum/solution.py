# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')

        def gain_from_subtree(node):
            nonlocal max_sum 
            if node is None: 
                return 0 
            max_gain_from_left_subtree = max(gain_from_subtree(node.left), 0)
            max_gain_from_right_subtree = max(gain_from_subtree(node.right), 0)
            max_sum = max(max_sum, node.val + max_gain_from_left_subtree + max_gain_from_right_subtree)
            return max(max_gain_from_left_subtree + node.val, max_gain_from_right_subtree + node.val)
        
        gain_from_subtree(root)
        return max_sum


