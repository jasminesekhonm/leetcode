class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        
        pascalTr = [[1], [1, 1]]
        
        for n in range(2,numRows):
            currRow = [1] * (n+1)
            for i in range(1,n):
                currRow[i] = pascalTr[n-1][i-1] + pascalTr[n-1][i]
                
            pascalTr.append(currRow)
            
        return pascalTr
