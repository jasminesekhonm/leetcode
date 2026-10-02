class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        moves = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        def dfs(i, j):

            q = [(i, j)]
            
            while q:
                curr_row, curr_col = q.pop()
                grid[curr_row][curr_col] = "0"

                for move in moves:
                    new_row, new_col = curr_row + move[0], curr_col + move[1]
                    if 0 <= new_row < m and 0 <= new_col < n and grid[new_row][new_col] == "1":
                        q.append((new_row, new_col))
                        



        num_islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i, j)
                    num_islands += 1 

        return num_islands

