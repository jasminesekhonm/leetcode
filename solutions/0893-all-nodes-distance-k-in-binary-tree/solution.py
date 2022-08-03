# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        
        graph = defaultdict(list)
        
        def populate_graph(node, parent_node):
            if not node:
                return 
            if parent_node:
                graph[node].append(parent_node)
            if node.left:
                graph[node].append(node.left)
                populate_graph(node.left, node)
            if node.right:
                graph[node].append(node.right)
                populate_graph(node.right, node)
                
        
        populate_graph(root, None)
        
        q = collections.deque()
        q.append((target, 0))
        
        output = []
        visited = set()
        
        while q:
            curr_node, dist = q.pop() 
            if dist == k:
                output.append(curr_node.val)
            visited.add((curr_node))
            if dist < k:
                for neighbor in graph[curr_node]:
                    if neighbor not in visited:
                        q.append((neighbor, dist + 1))
                        
        
        return output
                    
                
                
            
            
                
            
            
            
                
                
                
        
        
