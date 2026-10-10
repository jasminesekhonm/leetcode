from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: list[list[int]]) -> bool:
        
        graph = defaultdict(list)

        for (node1, node2) in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)


        q = [(0, -1)]
        
        visited = [False] * n

        while q:
            i, parent = q.pop()
            if visited[i]:
                return False
            visited[i] = True

            
            for ngbr in graph[i]:
                if ngbr == parent:
                    continue 
                q.append((ngbr, i))

        
        return all(visited)


