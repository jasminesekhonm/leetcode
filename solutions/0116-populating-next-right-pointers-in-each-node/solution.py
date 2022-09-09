"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        levelDict = defaultdict(list)
        
        def traverse(node, level):
            if node is None:
                return 
            if node.left:
                traverse(node.left, level+1)
            levelDict[level].append(node)
            if node.right:
                traverse(node.right, level+1)
                
        
        traverse(root, 0)
        
        for (level, nodes) in levelDict.items():
            i = 0
            prevNode = nodes[0]
            while i < len(nodes)-1:
                i += 1
                currNode = nodes[i]
                prevNode.next = currNode
                prevNode = currNode 
            prevNode.next = None 
            
        return root
        
