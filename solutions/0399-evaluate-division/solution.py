class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        adj = defaultdict(defaultdict)
        
        for (num, denom), value in zip(equations, values):
            adj[num][denom] = value 
            adj[denom][num] = 1 / value 
            
        def dfs(num, denom):
            q = []
            q.append((num, 1.0))
            
            visited = set()
            while q:
                currNode, currVal = q.pop()
                if currNode == denom:
                    return currVal
                visited.add(currNode)
                for div in adj[currNode]:
                    if div not in visited:
                        q.append((div, adj[currNode][div] * currVal))
            return -1.0
                    
        results = []
        for (num, denom) in queries:
            
            if num not in adj or denom not in adj:
                results.append(-1.0)
                
            elif num == denom:
                results.append(1.0)
                
            else:
                ret = dfs(num, denom)
                results.append(ret)
                
        return results
                
