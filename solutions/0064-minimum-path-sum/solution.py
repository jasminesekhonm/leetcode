class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        print(dp)
        for i in range(m):
            for j in range(n):
                if (i == 0 and j != 0):# first row
                    print('went here!')
                    dp[i][j] = grid[i][j] + dp[i][j-1]
                elif (j == 0 and i != 0):
                    print('went here!!')
                    dp[i][j] = grid[i][j] + dp[i-1][j]
                elif (i != 0 and j !=0 ):
                    print('went here !!!')
                    dp[i][j] = min(dp[i-1][j] + grid[i][j], dp[i][j-1] + grid[i][j])
        print(dp)
        return dp[-1][-1]
                    
        
