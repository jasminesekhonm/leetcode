class Solution:
    
    WHITE = 1
    GRAY = 2
    BLACK = 3
    
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        
        graph = defaultdict(list)
        indegree = {}
        
        for c, pr in prereqs:
            graph[pr].append(c)
            indegree[c] = indegree.get(c, 0) + 1
            
        zero_indegree_queue = deque([k for k in range(numCourses) if k not in indegree])
        
        topological_sorted_order = []
        
        while zero_indegree_queue:
            
            vertex = zero_indegree_queue.popleft()
            topological_sorted_order.append(vertex)
            
            if vertex in graph:
                for neighbor in graph[vertex]:
                    indegree[neighbor] -= 1
                    
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)
                        
        return topological_sorted_order if len(topological_sorted_order) == numCourses else []
        
            
            
            
            
            
