# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        bfs = [root]
        odd = False
        while bfs:
            nbfs = []
            for i in bfs:
                if i.val % 2 == odd:
                    return False
                if i.left:
                    nbfs.append(i.left)
                if i.right:
                    nbfs.append(i.right)
            for i in range(1,len(bfs)):
                greater = bfs[i].val > bfs[i-1].val
                less = bfs[i].val < bfs[i-1].val
                if odd:
                    if not less:
                        return False
                else:
                    if not greater:
                        return False
            odd = not odd
            bfs = nbfs
        return True

                    
