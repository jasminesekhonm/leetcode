class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m, n = len(matrix), len(matrix[0])
        
        def convert_row(rowNum):
            for col in range(n):
                if matrix[rowNum][col] != 0:
                    matrix[rowNum][col] = 'change'
        
        def convert_col(colNum):
            for row in range(m):
                if matrix[row][colNum] != 0:
                    matrix[row][colNum] = 'change'

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    convert_row(row)
                    convert_col(col)

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 'change':
                    matrix[row][col] = 0 
                    
