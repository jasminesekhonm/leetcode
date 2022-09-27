class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])
        
        visited = set()
        
        def modifyElems(row, col):
            for j in range(cols):
                if (row, j) not in visited and matrix[row][j] != 0:
                    visited.add((row, j))
                
            for i in range(rows):
                if (i, col) not in visited and matrix[i][col] != 0:
                    visited.add((i, col))
        
        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    modifyElems(row, col)
                    
        
        for (row, col) in visited:
            matrix[row][col] = 0
