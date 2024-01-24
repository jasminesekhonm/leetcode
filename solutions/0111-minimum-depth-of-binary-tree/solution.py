class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        if left == 0:
            return right + 1
        elif right == 0:
            return left + 1
        return min(left, right) + 1
