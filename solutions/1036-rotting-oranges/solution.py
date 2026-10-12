from collections import deque

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        
        m, n = len(grid), len(grid[0])

        q = deque([(i, j, 0) for i in range(m) for j in range(n) if grid[i][j] == 2])

        n_fresh = sum([1 for i in range(m) for j in range(n) if grid[i][j] == 1])
        
        if n_fresh == 0:
            return 0

        moves = [(1,0),(-1,0),(0,1),(0,-1)]

        visited = set()

        while q:
            curr_r, curr_c, curr_t = q.popleft()
            
            for (dr, dc) in moves:
                new_r, new_c = curr_r + dr, curr_c + dc 
                if not (0 <= new_r < m and 0 <= new_c < n) or grid[new_r][new_c] == 2:
                    continue
                elif grid[new_r][new_c] == 1 and not (new_r, new_c) in visited:
                    visited.add((new_r, new_c))
                    q.append((new_r, new_c, curr_t+1))
                    n_fresh -= 1
                    if n_fresh == 0:
                        return curr_t + 1
        
        return -1
