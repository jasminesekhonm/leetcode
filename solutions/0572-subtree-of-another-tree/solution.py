# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def is_equal(node1, node2):
            if node1 and not node2:
                return False 
            if node2 and not node1:
                return False
            if not node1 and not node2:
                return True
            return (node1.val == node2.val) and is_equal(node1.left, node2.left) and is_equal(node1.right, node2.right)

        
        def dfs(node):
            if node is None:
                return False
            elif is_equal(node, subRoot):
                return True 
            return dfs(node.left) or dfs(node.right)
            
        return dfs(root)
