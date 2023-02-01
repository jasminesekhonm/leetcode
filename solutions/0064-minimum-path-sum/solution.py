class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (i, j) == (m-1, n-1):
                    dp[i][j] = grid[i][j]
                else:
                    candidates = []
                    if 0 <= j+1 < n:
                        candidates.append(dp[i][j+1])
                    if 0 <= i+1 < m:
                        candidates.append(dp[i+1][j])
                    if len(candidates) > 0:
                        dp[i][j] = grid[i][j] + min(candidates)
        
        return dp[0][0]



