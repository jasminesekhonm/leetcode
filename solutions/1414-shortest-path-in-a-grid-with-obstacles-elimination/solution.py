from collections import deque

class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        moves = [(1,0), (-1,0), (0, 1), (0, -1)]

        q = deque([(0, 0, 0, k)])
        
        visited = set()
        visited.add((0, 0, k))

        while q:
            r, c, num_steps, obs = q.popleft()
            if (r, c) == (m-1, n-1):
                return num_steps

            for (dr, dc) in moves:
                nr, nc = r+dr, c+dc
                if (0 <= nr < m and 0 <= nc < n):
                    nrem = obs-grid[nr][nc]
                    if not nrem < 0 and not (nr, nc, nrem) in visited:
                        q.append((nr, nc, num_steps+1, nrem))
                        visited.add((nr, nc, nrem))
        return -1
                    
# O(V+E)
