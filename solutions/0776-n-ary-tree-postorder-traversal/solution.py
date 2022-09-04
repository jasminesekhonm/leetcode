"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        output = []
        def traverse(node):
            if node is None:
                return 
            for child in node.children:
                traverse(child)
            output.append(node.val)
        
        traverse(root)
        return output
        
