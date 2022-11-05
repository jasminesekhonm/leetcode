# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelDict = defaultdict(list)

        def traverse(node, currLevel):
            if node is None:
                return 
            
            if node.right:
                traverse(node.right, currLevel + 1)

            if node.left:
                traverse(node.left, currLevel + 1)
            
            levelDict[currLevel].append(node.val)

        traverse(root, 0)
        res = []
        for k, v in sorted(levelDict.items(), key = lambda x: x[0]):
            if k % 2 == 0:
                res.append(v[::-1])
            else:
                res.append(v)
        return res
