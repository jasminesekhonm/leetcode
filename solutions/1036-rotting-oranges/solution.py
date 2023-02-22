class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        moves = [(1,0), (0,1), (0,-1), (-1,0)]
        m, n = len(grid), len(grid[0])
        max_time = collections.defaultdict(int)

        def bfs(row, col):
            nonlocal max_time 
            q = deque()
            q.append((row, col, 0))
            max_time[(row, col)] = 0 
                
            visited = set()
            
            while q:
                row, col, curr_time = q.popleft()
                visited.add((row, col))

                for (drow, dcol) in moves:
                    new_row, new_col = row + drow, col + dcol 
                    if 0 <= new_row < m and 0 <= new_col < n and (new_row, new_col) not in visited and grid[new_row][new_col] == 1:
                        if (new_row, new_col) not in max_time:
                            max_time[(new_row, new_col)] = curr_time+1
                            q.append((new_row, new_col, curr_time+1))
                        elif max_time[(new_row, new_col)] > curr_time+1:
                            max_time[(new_row, new_col)] = curr_time+1
                            q.append((new_row, new_col, curr_time+1))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bfs(i,j)
                elif grid[i][j] == 0:
                    max_time[(i, j)] = 0 

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i, j) not in max_time:
                    return -1 

        return max(max_time.values())
            



