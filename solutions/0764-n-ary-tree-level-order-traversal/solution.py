"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = defaultdict(list)
        
        def traverse(node, currDepth):
            if node is None:
                return 
            output[currDepth].append(node.val)
            for child in node.children:
                traverse(child, currDepth+1)
        
        traverse(root,0)
        return output.values()
        
