from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        
        graph = defaultdict(list)

        for (node1, node2) in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)


        visited = [False] * n
        
        def dfs(i):
            q = [i]
            visited[i] = True
            while q:
                curr_node = q.pop()
                for ngbr in graph[curr_node]:
                    if not visited[ngbr]:
                        visited[ngbr] = True
                        q.append(ngbr)

        n_components = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                n_components += 1

        return n_components


        



        
