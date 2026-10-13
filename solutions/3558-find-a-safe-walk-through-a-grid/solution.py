from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        start = (0, 0)
        end = (m-1, n-1)

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        q = deque([(0, 0, health-grid[0][0])])

        visited = set()
        visited.add((0, 0))

        while q:
            r, c, rem_h = q.popleft()
            if (r, c) == end:
                return (rem_h >= 1)
            for (dr, dc) in moves:
                nr, nc = r + dr, c+dc 
                if not (0 <= nr < m and 0 <= nc < n) or (nr, nc) in visited:
                    continue 
                next_rem_h = rem_h - grid[nr][nc]
                if next_rem_h <= 0 :
                    continue 
                if next_rem_h == rem_h:
                    q.appendleft((nr, nc, next_rem_h))
                else:
                    q.append((nr, nc, next_rem_h))
                visited.add((nr, nc))

        return False 
