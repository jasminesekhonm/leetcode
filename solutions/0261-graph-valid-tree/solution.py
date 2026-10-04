from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        
        graph_dict = defaultdict(list)

        for (a, b) in edges:
            graph_dict[a].append(b)
            graph_dict[b].append(a)


        visited = [0] * n 

        def dfs(i, parent):
            if visited[i]:
                return False
            visited[i] = True
        
            for ngbr in graph_dict[i]:
                if ngbr == parent:
                    continue 
                if not dfs(ngbr, i):
                    return False
            
            return True 
        

        return dfs(0, -1) and all(visited)
