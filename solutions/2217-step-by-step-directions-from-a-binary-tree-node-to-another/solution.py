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
        
        graph = collections.defaultdict(list)
        queue = collections.deque([root])
        
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node.left.val].append((node.val, 'U'))
                graph[node.val].append((node.left.val, 'L'))
                
                queue.append(node.left)
                
            if node.right:
                graph[node.right.val].append((node.val, 'U'))
                graph[node.val].append((node.right.val, 'R'))
                
                queue.append(node.right)
                
        
        queue = collections.deque()
        queue.append((startValue, ""))
        
        visited = set()
        
        while True:
            val, path = queue.popleft()
            if val == destValue:
                return path 
            visited.add(val)
            for neighbor in graph[val]:
                if neighbor[0] in visited:
                    continue 
                queue.append((neighbor[0], path + neighbor[1]))
                
        return path
            
        
