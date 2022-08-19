# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        depthDict = defaultdict(list)
        
        def getDepth(node, currDepth):
            if node is None:
                return 
            depthDict[currDepth].append(node.val)
            if node.left:
                getDepth(node.left, currDepth+1)
            if node.right:
                getDepth(node.right, currDepth+1)
                
        getDepth(root, 0)
        
        return depthDict.values()
        
            
        
