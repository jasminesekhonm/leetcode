# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:

        count = 0

        def traverse_tree(node):
            nonlocal count
            if node is None:
                return None
            left = traverse_tree(node.left)
            if left is not None:
                return left

            count += 1
            if count == k:
                return node.val

            return traverse_tree(node.right)


        return traverse_tree(root)
            



