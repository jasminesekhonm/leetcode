from collections import deque

class Solution:
    def shortestDistance(self, grid: list[list[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        buildings = set([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 1])
        obstacles = set([(i, j) for i in range(m) for j in range(n) if grid[i][j] == 2])
        n_empty = m*n - len(buildings) - len(obstacles)
        
        if n_empty == 0:
            return -1

        moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        reach = [[0] * n for _ in range(m)]

        for b, (i, j) in enumerate(buildings):
            q = deque([(i, j, 0)])
            visited = set()
            
            while q:
                r, c, d = q.popleft()
                if len(visited) == n_empty:
                    break 
                for (dr, dc) in moves:
                    nr, nc = r + dr, c + dc 
                    if not (0 <= nr < m and 0 <= nc < n) or (nr, nc) in visited or (nr, nc) in buildings or (nr, nc) in obstacles:
                        continue 
                    q.append((nr, nc, d+1))
                    grid[nr][nc] = grid[nr][nc] + (d+1)
                    reach[nr][nc] += 1
                    visited.add((nr, nc))
            
            if not visited:
                return -1

        return min([grid[i][j] for i in range(m) for j in range(n) if (i, j) not in buildings and (i, j) not in obstacles and reach[i][j] == len(buildings)], default=-1)





