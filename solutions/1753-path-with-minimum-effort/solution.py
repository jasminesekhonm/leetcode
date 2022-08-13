class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        m, n = len(heights), len(heights[0])
        
        diffMatrix = [[float('inf') for _ in range(n)] for _ in range(m)]
        
        diffMatrix[0][0] = 0
        visited = set()
        
        q = [(0, 0, 0)]
        
        while q:
            diff, x, y = heapq.heappop(q)
            print(x, y, diff)
            visited.add((x, y))
            for dx, dy in moves:
                next_x, next_y = x + dx, y + dy 
                if 0 <= next_x < m and 0 <= next_y < n and not (next_x, next_y) in visited:
                    current_diff = abs(heights[next_x][next_y] - heights[x][y])
                    maxDiff = max(current_diff, diffMatrix[x][y])
                    if diffMatrix[next_x][next_y] > maxDiff:
                        diffMatrix[next_x][next_y] =maxDiff
                        heapq.heappush(q, (diffMatrix[next_x][next_y], next_x, next_y))
        return diffMatrix[-1][-1]
            
