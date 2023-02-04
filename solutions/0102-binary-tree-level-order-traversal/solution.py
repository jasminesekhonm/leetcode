# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = {}

        def traverse(node, currLevel):
            
            if node is not None:
                if currLevel not in res:
                    res[currLevel] = []
                res[currLevel].append(node.val)
                traverse(node.left, currLevel + 1)
                traverse(node.right, currLevel + 1)

        
        traverse(root, 0)
        if len(res) == 0:
            return []

        op = sorted(res.items(), key = lambda x: x[0])
        op = [r[1] for r in op]
        return op 
        

