# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = defaultdict(list)

        def traverse(node, currLevel):
            if node is not None:
                res[currLevel].append(node.val)
                if node.right is not None:
                    traverse(node.right, currLevel+1)
                if node.left is not None:
                    traverse(node.left, currLevel+1)
            
        traverse(root, 0)
        op = sorted(res.items(), key = lambda x: x[0])
        res = []
        for i, level_op in enumerate(op):
            if i % 2 == 0:
                res.append(level_op[1][::-1])
            else:
                res.append(level_op[1])
        
        return res 


                    
