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
            traverse(node.left, level+1)
            levelDict[level].append(node)
            traverse(node.right, level+1)

        traverse(root, 0)

        for (k, v) in levelDict.items():
            for i in range(len(v)-1):
                v[i].next = v[i+1]
            v[-1].next = None 

        return root 

        


