class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m, n = len(matrix), len(matrix[0])
        
        col0 = any(matrix[i][0] == 0 for i in range(m)) 
        for i in range(m):
            for j in range(1,n):
                

                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0 
        

        for i in range(m-1,-1,-1):
            for j in range(n-1,0,-1):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0
            if col0:
                    matrix[i][0] = 0
                
        
