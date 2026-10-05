class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose and then reflect or reflect then transpose

        n = len(matrix)
        def transpose(matrix):

            # 1 2 3
            # 4 5 6 
            # 7 8 9

            # 1 4 7
            # 2 5 8 
            # 3 6 9 
            for i in range(n):
                for j in range(i + 1, n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reflect(matrix):
            # 1 2 3
            # 4 5 6 
            # 7 8 9

            # 3 2 1
            # 6 5 4
            # 9 8 7 

            for j in range(n // 2):
                for i in range(n):
                    matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
            
        transpose(matrix)
        reflect(matrix)
        
