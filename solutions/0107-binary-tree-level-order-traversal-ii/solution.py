# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = defaultdict(list)
        def traversal(node, depth=0):
            if node is None:
                return    
            res[depth].append(node.val)
            if node.left:
                traversal(node.left, depth-1)
            if node.right:
                traversal(node.right, depth-1)
        
        # 0: 3
        # 1: 9, 20
        # 2: 15, 7
        traversal(root)
        return [v for k, v in sorted(res.items())]
            
                
            
                
        
