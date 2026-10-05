from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:

        graph = defaultdict(list)

        for (a, b) in edges:
            graph[a].append(b) 
            graph[b].append(a)

        visited = set()

        def dfs(node):
            q = []
            traversed = set()
            q.append(node)
            while q:
                curr = q.pop()
                for ngbr in graph[curr]:
                    if not ngbr in traversed:
                        q.append(ngbr)
                        traversed.add(ngbr)
                

            return traversed, len(traversed)

        
        total_traversed = 0 
        n_components = 0
        for node in graph:
            if node in visited:
                continue 
            nodes, n_nodes = dfs(node)
            visited.update(nodes)
            total_traversed += n_nodes
            n_components += 1
            if total_traversed == n:
                return n_components

        return n_components + (n - total_traversed)
            

        


        

        
