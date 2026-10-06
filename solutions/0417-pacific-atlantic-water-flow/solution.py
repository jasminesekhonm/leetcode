from collections import deque

class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m, n = len(heights), len(heights[0])

        moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def find_reachable(starts):
            q = deque([start for start in starts])

            visited = set()
            while q:
                r, c = q.popleft()
                visited.add((r,c))

                for (dr, dc) in moves:
                    nr, nc = r + dr, c + dc 
                    if not (0 <= nr < m and 0 <= nc < n) or (nr, nc) in visited or heights[nr][nc] < heights[r][c]:
                        continue 
                    q.append([nr, nc])

            return visited 


        pacific_starts = [[r,0] for r in range(m)] + [[0,c] for c in range(n)]
        atlantic_starts = [[r,n-1] for r in range(m)] + [[m-1,c] for c in range(n)]

        pacific_reachable = find_reachable(pacific_starts)
        atlantic_reachable = find_reachable(atlantic_starts)

        return list(pacific_reachable.intersection(atlantic_reachable))
            



