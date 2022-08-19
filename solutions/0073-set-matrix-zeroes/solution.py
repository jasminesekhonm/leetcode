class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        visited = set()
        
        def modifyElems(row, col):
            for i in range(m):
                if not (i, col) in visited:
                    visited.add((i, col))
            for j in range(n):
                if not (row, j) in visited:
                    visited.add((row, j))
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    modifyElems(i, j)
                    
        for (row, col) in visited:
            matrix[row][col] = 0
                    
                
            
        
