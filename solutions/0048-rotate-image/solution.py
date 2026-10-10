class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)

        def transpose(matrix):
            for i in range(n):
                for j in range(i+1,n):
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        def reflect(matrix):

            for i in range(n):
                matrix[i] = matrix[i][::-1]
                
        
        transpose(matrix)
        reflect(matrix)
