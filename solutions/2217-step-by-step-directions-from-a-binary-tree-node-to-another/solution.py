# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # each node is uniquely assigned a value from 1 to n 
        # integer startValue --> start Node
        # integer destValue --> destination node 
        
        # shortest path starting from node s and ending at t 
        # 'L', 'R', 'U'
        
        # the shortest path will pass through their lowest common ancestor
        # 1. find lowest common ancestor
        # 2. traverse from root -> startNode
        # 3. traverse from root -> destNode
        # 4. find lowest common ancestor
        # 5. startNode -> LCA -> destNode
        
        graph = defaultdict(set)
        
        def recurse(node):
            
            if not node:
                return None
            
            if node.val == startValue:
                self.startNode = node 
                
            if node.val == destValue:
                self.destNode = node 
                
            if node.left:
                graph[node].add((node.left, 'L'))
                graph[node.left].add((node, 'U'))
                recurse(node.left)
            
            if node.right:
                graph[node].add((node.right, 'R'))
                graph[node.right].add((node, 'U'))
                recurse(node.right)
                
        
        recurse(root)
        
        q = collections.deque()
        q.append((self.startNode, ""))
        
        visited = set()
        
        while q:
            curr_node, curr_direction = q.popleft() 
            if curr_node == self.destNode:
                return curr_direction
            
            visited.add(curr_node)
            
            
            for neighbor in graph[curr_node]:
                if neighbor[0] not in visited:
                    q.append((neighbor[0], curr_direction + neighbor[1]))
                    
        return -1 
            
        
        
        
                

            
                
        
        
            
                
                
