# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        
        def is_identical(root, sub_root):
            if root is None or sub_root is None:
                return root is sub_root 
            return (root.val == sub_root.val and is_identical(root.left, sub_root.left) and is_identical(root.right, sub_root.right))

        if root is None:
            return False

        if is_identical(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
