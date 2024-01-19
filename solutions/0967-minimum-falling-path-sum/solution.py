class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row == 0:
                    dp[row][col] = matrix[row][col]
                elif ((col > 0) and (col < len(matrix[0])-1)):
                    dp[row][col] = matrix[row][col] + min(dp[row-1][col-1], dp[row-1][col], dp[row-1][col+1])
                elif ((col == 0)):
                    dp[row][col] = matrix[row][col] + min(dp[row-1][col], dp[row-1][col+1])
                elif ((col == len(matrix[0])-1)):
                    dp[row][col] = matrix[row][col] + min(dp[row-1][col-1], dp[row-1][col])

        return min(dp[-1])


