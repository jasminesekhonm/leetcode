# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        
        max_sum = -float('inf')

        def traverse_tree(node):
            nonlocal max_sum
            if node is None:
                return 0
            left_gain = max(0, traverse_tree(node.left))
            right_gain = max(0, traverse_tree(node.right))
            total = node.val + left_gain + right_gain
            max_sum = max(max_sum, total)
            return node.val + max(left_gain, right_gain)
        
        traverse_tree(root)
        return max_sum
